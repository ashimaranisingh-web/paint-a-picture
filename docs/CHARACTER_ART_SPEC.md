# 2D character art: what the app needs

How the app draws the 2D character today, so new artwork (tank top, below-knee cargos, heeled sandals / sneakers)
drops straight in. Written 16 Nov 2026 from the files in `avatar/` and the code in `index.html` (`DOLL_VIEWS`,
`dollSource`, `drawDoll`).

## Files, per character and view
Two characters (female has no prefix, male is `male-`) × four views = 8 pictures, each with a matching mask.

| View | Female | Male |
|---|---|---|
| Front | `front.webp` + `front-parts.png` | `male-front.webp` + `male-front-parts.png` |
| Back | `back.webp` + `back-parts.png` | `male-back.webp` + `male-back-parts.png` |
| Walking left | `side-left.webp` + `side-left-parts.png` | `male-side-left.webp` + `male-side-left-parts.png` |
| Walking right | `side-right.webp` + `side-right-parts.png` | `male-side-right.webp` + `male-side-right-parts.png` |

A second length (the 3/4 cargos as an option next to full length) needs its own 8 pairs, named with `-34`
(e.g. `front-34.webp`, `front-34-parts.png`). If the new art simply replaces today's look, keep the names above.

## The picture (`.webp`)
- Transparent background (alpha), no shadow on the ground; the app draws the shadow.
- Cropped tight: **top of the hair at the very top edge, soles of the shoes at the very bottom edge.** The app
  scales the whole picture to her height and stands her on the bottom edge.
- Today's sizes are about 160–230 px wide × 670–710 px tall. Same height across all four views of one character
  (within a few px) so she doesn't grow when she turns. 2× that (about 1400 px tall) is fine and looks sharper.
- Head upright and level in every view; same proportions, clothes and accessories in all four.

## The mask (`-parts.png`)
- **Exactly the same width and height as its picture,** pixel for pixel on top of it.
- 8-bit **greyscale** PNG, no alpha, no anti-aliasing (hard edges). Each pixel's value says which part it is:

| Value | Part | Recoloured from |
|---|---|---|
| 0 | not recoloured (background, hair, face details, eyes, accessories) | — |
| 1 | skin | Skin tone |
| 2 | top (tank top) | Top colour |
| 3 | bottoms (cargos) | Cargos colour |
| 4 | shoes (sandals / sneakers) | Shoes colour |

- Hair, sunglasses, bag, watch and jewellery stay value 0 today (they keep their painted colours). If hair colour
  should be choosable too, add value 5 for hair and tell me; the code needs a small change for it.
- Recolouring keeps the painted shading: it shifts each part's colour and keeps its light and dark relative to the
  part's own middle tone. So paint each part in **one even base colour with shading** (a pattern like camo works,
  but its light and dark patches will turn into light and dark of the new colour).

## Base colours the art is painted in
The app needs to know what colour each part is painted in, to recolour away from it. Today: female skin tan, top
pink, cargos grey, shoes white; male the same but a white top. For the new art (black tank, olive camo cargos,
black sandals / white sneakers) I'll set these to match once the files arrive.

## What the concept sheet is and isn't
`Paint_a_Picture_Updated_Character_Handoff/reference_sheets/updated_male_female_turnaround.png` is the look to aim
for. Its crops have a cream background, slightly different sizes per view, and the "colour masks" on the sheet are
illustrations, not pixel-aligned masks, so they can't be used as the files above.

## Checking a delivery
Put the 16 files in one folder and run:
```bash
python3 scripts/check_avatar.py path/to/folder
```
It checks names, transparency, tight crop, mask size and values, masks lining up with the character, and equal heights
across views. "All checks passed." means the files can go into `avatar/`; recolouring and turning are then checked in the
app. (Today's art passes except the male front, which is 15 px taller than his other views.)

16 Nov: the "Character Art Package" checked against this: 8 pictures with the background baked in (no transparency),
505–519 px tall, and no masks. It's a good visual target, not yet the files. Its "Left" view faces right, which is
the app's `side-right`; name files by the way the character faces.

## The 3/4 set (16 Nov)
`avatar/34/` holds a 3/4-length set (black tank, olive cargos, black sandals / white sneakers), cut from the owner's
concept sheet by `scripts/cut_character_sheet.py` (needs Pillow, NumPy and SciPy) with masks made by colour. It passes
the checker and recolours well, but it is test quality: the pictures are about 445–475 px tall (sharper art would be
~700+), and thin dark edges of the tank (straps, neckline, the back edge on his side views) don't take the new colour.
Clean art with exported masks can replace these files one for one; the app picks them up with no code change.

## Hairstyle sets (16 Nov)
Each 3/4 hairstyle is a full set of 8 files in `avatar/34/<hair>/` (her: long, bob, pixie; him: curly, short, buzz,
longwavy, shoulder), plus the original "Classic" set in `avatar/34/`. Cut with `scripts/cut_character_sheet2.py
sheet out_dir prefix heels|sneakers` from flat-background turnaround sheets (front, back, faces-right, faces-left), scaled
to 720 px tall; every set passes the checker. Base colours: black tank, camo cargos, black heels / white sneakers.
To add a style: cut it into a new folder, add it to `HAIR2D` in index.html.
