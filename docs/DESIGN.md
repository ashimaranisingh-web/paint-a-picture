# Design and voice

How Paint a Picture looks and sounds. When a screen doesn't match this, fix the screen or update this file on purpose.
Never both drift.

## Feel
Warm, calm, a little playful. A sunny coast in the afternoon, not a dashboard. Honey and paper tones, pixel art for the
world, clean type for everything around it.

## Colour (tokens in `:root`, top of `index.html`)
| Token | Value | Use |
|---|---|---|
| `--paper` | `#f7f4ee` | page background |
| `--surface` | `#fffdf9` | cards and panels |
| `--ink` / `--ink-2` / `--muted` | `#1f2420` / `#474c46` / `#686961` | text, strongest to softest |
| `--line` / `--line-2` | `#e6e0d4` / `#d6cfbf` | borders and dividers |
| `--accent` | `#f04f85` | the one primary action on a screen, and the person's picks |
| `--amber` / `--amber-soft` | `#8f5c14` / `#f5ead6` | the honey tone: progress, warmth |
| `--sea` / `--sea-soft` | `#2c6a88` / `#e2edf2` | water, maps |
| `--danger` | `#9b3b2a` | delete and reset only |

Rules:
- **Pink is rare.** One pink button per screen at most, plus things the person picked. No pink backgrounds on pages.
- Titles and labels are near-black (`--ink`), not grey and not pink.
- Use the tokens. A new hex value in the code needs a reason.

## Type
- Headings: **Instrument Serif**, regular weight, no italics. Body and UI: **Manrope**.
- Sizes: page titles 24px, body 14px. Labels in Title Case.
- Left-aligned text, except centred pop-ups.

## Shape and depth
- Corners 4, 8 or 12px (pills and round buttons stay round; the Account boxes and pop-up use 14 and 20).
- Shadows are soft and low: a 1px ring plus a gentle drop. No heavy glows.
- Map controls are light glass (blurred white), small and quiet.
- Padding: 24px around content in onboarding, 16px page gutter in the app.

## The world (canvas)
- Pixel art. More detail, not more complexity.
- The sea is light, daytime and endless. Fog sits on land only, never on the sea.
- Land is continuous; roads stay on land. Boats and dolphins on the water, nothing floating.
- Night comes from the person's local time (7pm to 6am).
- The character wears solid black sunglasses by default. No caps.

## Pieces (jigsaw)
- Every piece is a real jigsaw shape; no two neighbours repeat a shape.
- Pieces join into the finished picture; the reveal stays locked until earned, with the next piece glowing.

## Motion
- Slow and smooth: ease-out, nothing snappy. Things complete one at a time rather than all at once.
- Every animation has a Reduce Motion fallback (show the end state).

## Voice
- Short, warm, plain. Talk to the person ("your picture", "your places").
- Words we use: **picture, pieces, goals, milestones, places, journal**. Goals bring pieces; milestones are steps.
- Never "dream" in visible copy. No exclamation-mark cheerleading, no "unlock your potential", no emoji in UI copy.
- Error and empty states say what happened and what to do next, in one line.
