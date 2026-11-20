#!/usr/bin/env python3
"""Cut the owner's character sheets (art/wardrobe-sheets/) into the wardrobe looks in avatar/w/<id>/.

    python3 scripts/cut_wardrobe_sheet.py [look-id ...]

Reads art/wardrobe-configs/<id>.json for each look: the sheet, the order of the views on it, and, for a sheet holding two
looks (six figures), which figures belong to this look ("xranges" + "pick") and which side view to mirror. Writes four
pictures 720 px tall (front, back, side-right, side-left), all standing on the bottom edge. Then run
scripts/build_wardrobe_masks.py for their colour maps.

Why not cut_character_sheet2.py: that one decides "background" by closeness to the sheet's pale pink, and white
trousers are just as close, so big patches of them came out see-through. Here the background must also lean pink
(a little more blue than green); white and cream fabric never does, so it stays solid. Needs Pillow, NumPy, SciPy.
"""
import json, os, sys
import numpy as np
from PIL import Image
from scipy import ndimage as nd

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TARGET_H = 720


def cut(cfg):
    a = np.asarray(Image.open(os.path.join(ROOT, cfg["sheet"])).convert("RGB")).astype(np.float32)
    H, W, _ = a.shape
    bg = np.concatenate([a[4:30, 4:30].reshape(-1, 3), a[4:30, -30:-4].reshape(-1, 3)]).mean(0)
    d = np.sqrt(((a - bg) ** 2).sum(2)); r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    pinkish = (b - g) > 2
    shadow = pinkish & (r > 160) & (d < 80) & (np.arange(H)[:, None] > H * .6)  # the soft ground shadow under the feet
    near = ((d < 26) & pinkish) | shadow
    lab, n = nd.label(near)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    sizes = nd.sum(near, lab, range(1, n + 1))
    bgm = np.isin(lab, list(border)) | np.isin(lab, 1 + np.where(sizes > 6)[0])  # outside, plus every pink gap (between arm and body, between curls); white fabric is never pink, so it stays
    fig = ~bgm
    # soft edges only where the picture really blends into the pink; everything else is solid
    # edges: each edge pixel is part figure, part pink. Its figure colour is taken from the nearest solid pixel inside, and
    # how much pink it holds is measured along the line from the pink to that colour, so hair outlines lose their pink halo
    inner = nd.binary_erosion(fig, iterations=3)
    soft = fig & ~inner
    _, (iy, ix) = nd.distance_transform_edt(~inner, return_indices=True)
    F = a[iy, ix]; v1 = a - bg; v2 = F - bg
    k = np.clip((v1 * v2).sum(2) / np.maximum((v2 * v2).sum(2), 1), 0, 1)
    alpha = np.where(inner, 1.0, np.where(soft, k, 0.0))
    alpha[shadow & ~inner] = 0
    safe = np.maximum(alpha, .05)[:, :, None]
    rgb = np.where(soft[:, :, None], np.clip((a - (1 - safe) * bg) / safe, 0, 255), a)
    # the figures: given ranges, or found as columns of the figure mask
    if "xranges" in cfg:
        cols = [tuple(cfg["xranges"][i]) for i in cfg["pick"]]
    else:
        lab2, n2 = nd.label(nd.binary_opening(fig, iterations=1)); sz2 = nd.sum(fig, lab2, range(1, n2 + 1)); objs = nd.find_objects(lab2)
        boxes = sorted([(o[1].start, o[1].stop) for i, o in enumerate(objs) if sz2[i] > 6000]); cols = []
        for x0, x1 in boxes:
            if cols and x0 < cols[-1][1] + 12: cols[-1] = (cols[-1][0], max(cols[-1][1], x1))
            else: cols.append((x0, x1))
        assert len(cols) == len(cfg["figures"]), f"expected {len(cfg['figures'])} figures, found {len(cols)}"
    cuts = {}
    for nm, (x0, x1) in zip(cfg["figures"], cols):
        pad = 0 if "xranges" in cfg else 12  # given ranges are exact: on the two-look sheet neighbouring hands almost touch
        lo, hi = max(0, x0 - pad), min(W, x1 + pad)
        sub = alpha[:, lo:hi]; keep = sub > .1
        l3, n3 = nd.label(keep); s3 = nd.sum(keep, l3, range(1, n3 + 1))
        cx = nd.center_of_mass(keep, l3, range(1, n3 + 1))  # bits of the neighbouring figure in the margin are dropped
        main = int(np.argmax(s3)); bx = nd.find_objects(l3)[main][1]
        ok = [i + 1 for i in range(n3) if s3[i] > s3.max() * .02 and bx.start <= cx[i][1] <= bx.stop]
        big = np.isin(l3, ok)
        ys, xs = np.where(big & (sub > .35))
        y0, y1, xa, xb = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        cuts[nm] = np.dstack([rgb[y0:y1, lo + xa:lo + xb], np.where(big, sub, 0)[y0:y1, xa:xb] * 255])
    for to, src in cfg.get("mirror", {}).items(): cuts[to] = cuts[src][:, ::-1].copy()
    Hs = max(c.shape[0] for c in cuts.values())
    out = os.path.join(ROOT, cfg["out"]); os.makedirs(out, exist_ok=True)
    for nm, c in cuts.items():
        if c.shape[0] < Hs: c = np.concatenate([np.zeros((Hs - c.shape[0], c.shape[1], 4), np.float32), c], 0)  # stand on the bottom edge
        sc = TARGET_H / c.shape[0]
        im = Image.fromarray(np.clip(c, 0, 255).astype(np.uint8)).resize((max(1, round(c.shape[1] * sc)), TARGET_H), Image.LANCZOS)
        im.save(os.path.join(out, nm + ".webp"), "WEBP", quality=90, alpha_quality=100, method=6)
    return sorted(cuts)


def main():
    cdir = os.path.join(ROOT, "art", "wardrobe-configs"); only = set(sys.argv[1:])
    for f in sorted(os.listdir(cdir)):
        lid = f[:-5]
        if only and lid not in only: continue
        print(lid, cut(json.load(open(os.path.join(cdir, f)))))


if __name__ == "__main__":
    main()
