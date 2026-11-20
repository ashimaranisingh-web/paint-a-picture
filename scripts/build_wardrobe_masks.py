#!/usr/bin/env python3
"""Build the colour maps (-parts.png) for the 2D wardrobe looks in avatar/w/, from art/wardrobe.json.

    python3 scripts/build_wardrobe_masks.py [look-id ...]

Needs Pillow, NumPy and SciPy. Reads each look's four pictures (front, back, side-right, side-left) and writes a map beside
each one: 1 skin, 2 top, 3 bottoms, 4 shoes, 0 everything else. Only items marked "plain" in wardrobe.json get a value;
patterned items (stripes, camo) stay 0, so the app can never recolour them.

How each part is found:
  skin    warm, fairly saturated and smooth; specks smaller than a fingertip are dropped (they're camo, not skin)
  dark    (black or brown tops) dark, smooth pixels inside the top's band. Hair is just as dark but full of strands, so
          the local "busyness" of the picture keeps it out; olive camo is kept out by its hue
  light   (white or beige trousers and shoes) every low-saturation pixel in the band, shadows and seams included, then
          holes filled, so the whole garment changes colour evenly instead of in blotches
"""
import json, os, sys
import numpy as np
from PIL import Image
from scipy import ndimage as nd

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
VIEWS = ["front", "back", "side-right", "side-left"]


def hsv(rgb):
    mx = rgb.max(2); mn = rgb.min(2); d = mx - mn
    s = np.where(mx > 0, d / np.maximum(mx, 1e-6), 0); v = mx / 255
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]; dd = np.maximum(d, 1e-6)
    h = np.where(mx == r, ((g - b) / dd) % 6, np.where(mx == g, (b - r) / dd + 2, (r - g) / dd + 4)) / 6
    return np.where(d > 0, h, 0), s, v


def keep_big(m, share=0.03, least=0):
    lab, n = nd.label(m)
    if not n: return m
    sz = nd.sum(m, lab, range(1, n + 1)); cut = max(least, sz.max() * share)
    return np.isin(lab, 1 + np.where(sz >= cut)[0])


def build(path, spec, view="front"):
    a = np.asarray(Image.open(path).convert("RGBA")).astype(np.float32)
    rgb, al = a[:, :, :3], a[:, :, 3]; H, W = al.shape; on = al > 40
    h, s, v = hsv(rgb); y = np.arange(H)[:, None] / H * np.ones((1, W))
    lum = rgb.mean(2); busy = nd.uniform_filter(np.hypot(nd.sobel(lum, 0), nd.sobel(lum, 1)), 7)
    # skin is much redder than the light patches of camo (red minus green about 57-75 against about 24), and a touch
    # more orange in hue, measured on these sheets (20 Nov)
    skin = on & (h < 0.085) & (s > 0.18) & (s < 0.78) & (v > 0.42) & (rgb[:, :, 0] - rgb[:, :, 1] > 34)
    skin = keep_big(nd.binary_opening(skin, iterations=1), 0, least=120)
    skin = nd.binary_fill_holes(nd.binary_closing(skin, iterations=1)) & on
    m = np.zeros((H, W), np.uint8)
    for part, val in (("bot", 3), ("shoe", 4), ("top", 2)):
        p = spec.get(part)
        if not p: continue
        if view.startswith("side") and "side" in p: p = {**p, **p["side"]}  # a sheet whose side views differ (other shoes)
        if view == "back" and part != "top" and "back" in p: p = {**p, **p["back"]}
        if part == "shoe": band = (y >= p["from"])
        else: band = (y >= p["band"][0]) & (y <= p["band"][1])
        if p["kind"] == "dark":
            olive = (h > 0.09) & (h < 0.3) & (s > 0.18) & (v > 0.21)  # camo; a near-black top can have an olive cast too, but it is darker
            # per look: a black top is greyer than the brown hair over it (smax), a brown top lighter and smoother (vmin, busy)
            lim = view != "front"  # only behind and beside her does long hair lie over the top; from the front it falls outside it
            if view == "back": p = {**p, **p.get("back", {})}  # from behind, the hair covers most of the top: stricter limits
            c = on & band & (v < 0.42) & ~olive & ~skin & (busy < (p.get("busy", 46) if lim else 80))
            if lim: c &= (v >= p.get("vmin", 0)) & (s <= p.get("smax", 1))
            c = nd.binary_opening(c, iterations=1)
            c = nd.binary_fill_holes(nd.binary_closing(c, iterations=3)) & on & band & ~skin & ~(olive & (v > 0.25))
            if lim and ("smax" in p or "vmin" in p):
                c &= (s <= p.get("smax", 1) + .08) & (v >= p.get("vmin", 0) - .03)  # closing must not pull hair back in
                c = nd.binary_fill_holes(nd.binary_closing(c, iterations=2)) & on & band & ~skin  # deep folds inside the top are top; hair is never enclosed by it
            c = keep_big(c, 0.12)
        else:
            c = on & band & (s < 0.3) & (v > 0.30) & ~skin
            c = nd.binary_fill_holes(nd.binary_closing(c, iterations=3)) & on & band & ~skin
            c = c & ~((s > 0.35) & (v > 0.25))  # a saturated top hem or a strap stays out
            c = keep_big(c, 0.05 if part == "bot" else 0.1)
        m[c] = val
    m[skin] = 1
    return m


def main():
    cfg = json.load(open(os.path.join(ROOT, "art", "wardrobe.json")))
    only = set(sys.argv[1:])
    for lk in cfg["looks"]:
        if only and lk["id"] not in only: continue
        spec = {k: v for k, v in lk.get("mask", {}).items()}
        for v in VIEWS:
            pic = os.path.join(ROOT, "avatar", "w", lk["id"], v + ".webp")
            m = build(pic, spec, v)
            Image.fromarray(m).save(os.path.join(ROOT, "avatar", "w", lk["id"], v + "-parts.png"))
        print(lk["id"], "done")


if __name__ == "__main__":
    main()
