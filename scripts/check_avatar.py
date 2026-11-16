#!/usr/bin/env python3
"""Check a folder of 2D character art against docs/CHARACTER_ART_SPEC.md before it goes into avatar/.

Usage:  python3 scripts/check_avatar.py [folder]        (default: avatar/)

Checks, for the 8 views (female and male x front, back, side-left, side-right):
  1. the picture (.webp) and its mask (-parts.png) both exist, with the exact names
  2. the picture has real transparency and a character in it, cropped tight (hair at the top edge, soles at the bottom)
  3. the mask is exactly the same width and height as its picture
  4. the mask is 8-bit greyscale, no alpha, and only uses the values 0-4
  5. the four views of one character are the same height (within 2%)
  and that mask pixels sit on the character, not on empty background.
Recolouring and turning still need checking in the app itself (the spec says so too).

Needs nothing beyond macOS: WebP is read through `sips`, PNG with Python's zlib.
"""
import os, struct, subprocess, sys, tempfile, zlib

VIEWS = ["front", "back", "side-left", "side-right"]
SETS = {"female": "", "male": "male-"}


def read_png(path):
    """Returns (width, height, colour type, bit depth, rows of channel tuples)."""
    d = open(path, "rb").read()
    if d[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    i, idat, w = 8, b"", 0
    while i < len(d):
        n = struct.unpack(">I", d[i:i + 4])[0]; t = d[i + 4:i + 8]; c = d[i + 8:i + 8 + n]
        if t == b"IHDR":
            w, h, bd, ct, _, _, il = struct.unpack(">IIBBBBB", c)
        elif t == b"IDAT":
            idat += c
        i += 12 + n
    if bd != 8 or il:
        return w, h, ct, bd, None
    ch = {0: 1, 2: 3, 4: 2, 6: 4}.get(ct)
    if ch is None:
        return w, h, ct, bd, None
    raw, stride, rows, prev, p = zlib.decompress(idat), w * ch, [], bytearray(w * ch), 0
    for _ in range(h):
        f = raw[p]; p += 1; line = bytearray(raw[p:p + stride]); p += stride
        for x in range(stride):
            a = line[x - ch] if x >= ch else 0; b = prev[x]; c2 = prev[x - ch] if x >= ch else 0
            if f == 1: line[x] = (line[x] + a) & 255
            elif f == 2: line[x] = (line[x] + b) & 255
            elif f == 3: line[x] = (line[x] + ((a + b) >> 1)) & 255
            elif f == 4:
                pa, pb, pc = abs(b - c2), abs(a - c2), abs(a + b - 2 * c2)
                line[x] = (line[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c2)) & 255
        rows.append([tuple(line[x:x + ch]) for x in range(0, stride, ch)]); prev = line
    return w, h, ct, bd, rows


def webp_to_png(path):
    out = tempfile.mktemp(suffix=".png")
    subprocess.run(["sips", "-s", "format", "png", path, "--out", out], capture_output=True, check=True)
    return out


def check(folder):
    ok, bad, heights = [], [], {}
    for who, pre in SETS.items():
        for v in VIEWS:
            name, pic, mask = f"{who} {v}", os.path.join(folder, f"{pre}{v}.webp"), os.path.join(folder, f"{pre}{v}-parts.png")
            if not os.path.exists(pic):
                bad.append(f"{name}: missing {os.path.basename(pic)}"); continue
            try:
                pw, ph, pct, _, prow = read_png(webp_to_png(pic))
            except Exception as e:
                bad.append(f"{name}: picture can't be read ({e})"); continue
            if pct != 6:
                bad.append(f"{name}: picture has no transparency ({pw}x{ph}, background baked in)")
                heights.setdefault(who, {})[v] = ph
                if not os.path.exists(mask): bad.append(f"{name}: missing {os.path.basename(mask)}")
                continue
            alpha = [[px[3] for px in r] for r in prow]
            filled = [y for y, r in enumerate(alpha) if max(r) > 40]
            if not filled:
                bad.append(f"{name}: picture is empty"); continue
            top, bottom = filled[0], filled[-1]
            if top > ph * .02 or bottom < ph * .98 - 1:
                bad.append(f"{name}: not cropped tight (character spans rows {top}-{bottom} of {ph})")
            filled_corners = sum(1 for c in (alpha[0][0], alpha[0][-1], alpha[-1][0], alpha[-1][-1]) if c > 40)
            if filled_corners >= 2:  # one corner can be a toe or a curl touching the tight crop; two or more means background
                bad.append(f"{name}: corners aren't transparent (background left in?)")
            heights.setdefault(who, {})[v] = ph
            if not os.path.exists(mask):
                bad.append(f"{name}: missing {os.path.basename(mask)}"); continue
            mw, mh, mct, mbd, mrow = read_png(mask)
            if (mw, mh) != (pw, ph):
                bad.append(f"{name}: mask is {mw}x{mh}, picture is {pw}x{ph}"); continue
            if mct != 0 or mbd != 8:
                bad.append(f"{name}: mask isn't 8-bit greyscale without alpha (colour type {mct}, depth {mbd})"); continue
            vals = {px[0] for r in mrow for px in r}
            if not vals <= {0, 1, 2, 3, 4}:
                bad.append(f"{name}: mask uses values outside 0-4: {sorted(vals - {0, 1, 2, 3, 4})[:8]}"); continue
            parts = {1: "skin", 2: "top", 3: "bottoms", 4: "shoes"}
            absent = [parts[k] for k in parts if k not in vals]
            if absent:
                bad.append(f"{name}: mask has no {', '.join(absent)}")
            stray = sum(1 for y in range(ph) for x in range(pw) if mrow[y][x][0] and alpha[y][x] < 8)
            total = sum(1 for r in mrow for px in r if px[0])
            if total and stray / total > .02:
                bad.append(f"{name}: {stray / total:.0%} of mask pixels sit on empty background (mask not lined up?)")
            ok.append(f"{name}: {pw}x{ph}, mask values {sorted(vals)}")
    for who, hs in heights.items():
        if hs and (max(hs.values()) - min(hs.values())) > max(hs.values()) * .02:
            bad.append(f"{who}: views differ in height {hs} (the character would grow or shrink when turning)")
    return ok, bad


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "avatar")
    ok, bad = check(folder)
    print(f"Checked {os.path.abspath(folder)}")
    for line in ok: print("  read  ", line)
    for line in bad: print("  PROBLEM", line)
    print("All checks passed." if not bad else f"{len(bad)} problem(s).")
    sys.exit(1 if bad else 0)
