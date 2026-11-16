#!/usr/bin/env python3
"""Cut one character turnaround sheet (front, back, then the two profiles, on a flat background) into the app's four
2D views plus colour masks. Usage:
    python cut_character_sheet2.py sheet.webp out_dir prefix shoes
prefix: "" for her, "male-" for him.  shoes: "heels" (dark) or "sneakers" (light).
Needs Pillow, NumPy and SciPy. The sheet's 3rd figure faces right (the app's side-right), the 4th faces left.
Masks: 1 skin, 2 top, 3 bottoms, 4 shoes, 0 everything else (hair, face details, accessories, socks).
"""
import sys, os
import numpy as np
from PIL import Image
from scipy import ndimage as nd

sheet, OUT, PRE, SHOES = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
TARGET_H = 720
os.makedirs(OUT, exist_ok=True)
a = np.asarray(Image.open(sheet).convert("RGB")).astype(np.float32)
H, W, _ = a.shape
bg = np.concatenate([a[4:30, 4:30].reshape(-1, 3), a[4:30, -30:-4].reshape(-1, 3)]).mean(0)
d = np.sqrt(((a - bg) ** 2).sum(2))
r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
# the soft purple-pink ground shadow under the feet counts as background
shadow = (b - g > 6) & (r > 165) & (d < 80) & (np.arange(H)[:, None] > H * .6)
near = (d < 22) | shadow
lab, n = nd.label(near)
border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
sizes = nd.sum(near, lab, range(1, n + 1))
bgm = np.isin(lab, list(border)) | np.isin(lab, 1 + np.where(sizes > 120)[0])  # outside, plus enclosed gaps (arm to body)
fig = ~bgm
lab2, n2 = nd.label(nd.binary_opening(fig, iterations=1))
sz2 = nd.sum(fig, lab2, range(1, n2 + 1)); objs = nd.find_objects(lab2)
boxes = sorted([(o[1].start, o[1].stop) for i, o in enumerate(objs) if sz2[i] > 6000])
# merge pieces that overlap horizontally (feet, loose hair) into four figures
cols = []
for x0, x1 in boxes:
    if cols and x0 < cols[-1][1] + 12: cols[-1] = (cols[-1][0], max(cols[-1][1], x1))
    else: cols.append((x0, x1))
assert len(cols) == 4, f"expected 4 figures, found {len(cols)}: {cols}"
names = ["front", "back", "side-right", "side-left"]
# soft edge: alpha from distance to the background colour, then take the pink back out of the edge pixels
alpha = np.clip((d - 10) / 34, 0, 1)
alpha = np.where(bgm, 0, np.maximum(alpha, nd.binary_erosion(fig, iterations=2)))
alpha[shadow & ~nd.binary_erosion(fig, iterations=3)] = 0
safe = np.maximum(alpha, .05)[:, :, None]
rgb = np.clip((a - (1 - safe) * bg) / safe, 0, 255)
cuts = {}
for nm, (x0, x1) in zip(names, cols):
    sub = alpha[:, max(0, x0 - 12):x1 + 12]
    keep = sub > .1
    l3, n3 = nd.label(keep); s3 = nd.sum(keep, l3, range(1, n3 + 1))
    keepbig = np.isin(l3, 1 + np.where(s3 > s3.max() * .02)[0])
    ys, xs = np.where(keepbig & (sub > .35))
    cx0, cx1 = max(0, x0 - 12) + xs.min(), max(0, x0 - 12) + xs.max() + 1
    y0, y1 = ys.min(), ys.max() + 1
    al = np.where(keepbig, sub, 0)[y0:y1, xs.min():xs.max() + 1]
    cuts[nm] = np.dstack([rgb[y0:y1, cx0:cx1], al * 255])
Hs = max(c.shape[0] for c in cuts.values())
for nm in names:  # same height in every view: stand on the bottom edge
    c = cuts[nm]
    if c.shape[0] < Hs: cuts[nm] = np.concatenate([np.zeros((Hs - c.shape[0], c.shape[1], 4), np.float32), c], 0)


def hsv(rgb):
    mx = rgb.max(2) / 255; mn = rgb.min(2) / 255; dd = mx - mn + 1e-6
    return np.where(mx > 0, dd / (mx + 1e-6), 0), mx


def biggest(mm, share):
    l, k = nd.label(mm)
    if not k: return mm
    s = nd.sum(mm, l, range(1, k + 1)); return np.isin(l, 1 + np.where(s >= s.max() * share)[0])


for nm, c in cuts.items():
    sc = TARGET_H / c.shape[0]
    im = Image.fromarray(np.clip(c, 0, 255).astype(np.uint8), "RGBA").resize((max(1, round(c.shape[1] * sc)), TARGET_H), Image.LANCZOS)
    c = np.asarray(im).astype(np.float32)
    Hh, Ww = c.shape[:2]; rgbc = c[:, :, :3]; al = c[:, :, 3]; on = al > 8
    s, v = hsv(rgbc); y = np.arange(Hh)[:, None] / Hh * np.ones((1, Ww)); warm = rgbc[:, :, 0] - rgbc[:, :, 2]
    gr = rgbc[:, :, 1] / (rgbc[:, :, 0] + 1)
    olive = on & (gr > .80) & (gr < 1.2) & (v > .16) & (s > .18) & (rgbc[:, :, 0] - rgbc[:, :, 1] < 26) & (rgbc[:, :, 2] < rgbc[:, :, 1] - 3) & (y > .3) & (y < .85)  # near-black tank with an olive cast is not cargo
    bot_rows = [rr for rr in range(Hh) if olive[rr].sum() > Ww * .08]; b0, b1 = min(bot_rows), max(bot_rows)
    bottoms = olive & (y >= b0 / Hh) & (y <= b1 / Hh + .01)
    skin_raw = on & (gr > .52) & (gr < .82) & (s > .16) & (v > .38) & (rgbc[:, :, 0] - rgbc[:, :, 1] >= 26)
    skin = on & (gr > .52) & (gr < .82) & (s > .16) & (s < .82) & (v > .38) & ~bottoms
    hairdark = on & (v < .40) & (warm >= 14)
    hairzone = nd.binary_closing(hairdark, iterations=4) & ~nd.binary_opening(skin, iterations=4)  # light strands inside the hair are hair, not skin
    skin &= ~hairzone
    black = on & (v < .46) & (warm < (15 if nm == "back" else 22)) & (s < .5)  # from behind, long hair covers the tank: stricter, so dark hair stays hair
    tr = [rr for rr in range(Hh) if .10 * Hh < rr < .5 * Hh and black[rr].sum() > max(3, Ww * .06)]
    t0, t1 = (min(tr), max(tr)) if tr else (int(.18 * Hh), int(.42 * Hh))
    top = black & (y >= t0 / Hh - .005) & (y <= t1 / Hh + .01)  # the cargos are painted over it afterwards
    if SHOES == "sneakers": shoes = on & (y > .88) & (s < .25) & (v > .5) & (al > 120)
    else: shoes = on & (y > .88) & (v < .34) & (warm < 24) & (al > 120)
    shoes &= ~skin

    def solid(mm, it): return nd.binary_fill_holes(nd.binary_closing(mm, iterations=it)) & on
    S2 = biggest(solid(skin, 2), .02); T2 = biggest(solid(top, 3), .25); B2 = biggest(solid(bottoms, 4), .05); F2 = biggest(solid(shoes, 2), .12)
    if SHOES == "sneakers":  # white socks sit above the shoe: only the lowest band of light pixels is shoe
        F2 &= (y > .91)
    core = biggest(nd.binary_opening(T2, iterations=3), .5); T2 &= nd.binary_dilation(core, iterations=3)
    for rr in range(Hh):
        xs = np.where(core[rr])[0]
        if len(xs) > 2: a0, a1 = xs.min(), xs.max(); T2[rr, a0:a1 + 1] |= on[rr, a0:a1 + 1] & ~S2[rr, a0:a1 + 1] & (v[rr, a0:a1 + 1] < .62)
    hem = np.where(core.any(0), Hh - 1 - np.argmax(core[::-1], 0), -1)  # lowest tank row in each column
    B2 &= np.arange(Hh)[:, None] > hem[None, :]  # the cargos never sit above the tank's hem in the same column
    m = np.zeros((Hh, Ww), np.uint8); m[S2] = 1; m[T2] = 2; m[B2] = 3; m[F2] = 4
    m[(m == 3) & skin_raw & S2] = 1  # a hand resting on a pocket is still a hand
    m[(m == 1) & on & (v < .4) & (warm >= 14)] = 0  # dark warm specks inside the skin are hair or brows
    Image.fromarray(c.astype(np.uint8), "RGBA").save(os.path.join(OUT, PRE + nm + ".webp"), "WEBP", quality=90, alpha_quality=100, method=6)
    Image.fromarray(m, "L").save(os.path.join(OUT, PRE + nm + "-parts.png"))
    print(PRE + nm, Ww, Hh, {p: int((m == p).sum()) for p in range(5)})
