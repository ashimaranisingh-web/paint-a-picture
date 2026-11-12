# Design and voice

How Paint a Picture looks and sounds. When a screen doesn't match this, fix the screen or update this file on purpose.
Never both drift.

## Feel
Calm, premium, a little playful. A gallery wall for a pixel-art world: neutral off-white around it, true black type, one
deep rose for what matters. The world brings the colour; the interface stays quiet.

## The design system (Nov 2026)
The last block of the stylesheet, "DESIGN SYSTEM", is the source of truth; older rules above it are layers it
overrides. New components use these, never new one-off styles.

- **One card:** white (`--card`), 16px corners (`--card-r`), no outline, one soft shadow (`--card-sh`).
- **One tab:** the segmented control (`.seg`): a light tray, the chosen tab white with a small lift.
- **One chip:** white with a hairline ring (`--ring`); chosen is **ink** with white text.
- **Pink is rare:** the main button on a screen, ticks, progress bars, unlocked pieces and the star. Links, quiet
  buttons, chosen chips, the tab bar and labels are ink or grey.
- **Type scale:** 28 page titles (serif), 22 sheet and pop-up titles (serif), 17 section and card titles (sans, bold),
  15 body, 13 small. Labels are 13px, normal case, grey: no all-capitals eyebrows.
- **Serif only** for page titles and big moments (onboarding headings, the weekly review line, good things,
  affirmations, the loader). Everything inside a page is the sans.
- **Spacing:** 8-point rhythm (8 / 12 / 16 / 24 / 32). 20px side margins everywhere. 24px between sections, 12px
  between cards, 16px inside cards.
- **Surfaces, not outlines:** a card has a shadow or a hairline, never both.
- **Motion:** one signature moment (a piece unlocking). Nothing loops; no wiggling icons or pulsing rings.
- **Copy:** at most one playful line per flow; no exclamation marks.

## Colour (tokens in `:root`, top of `index.html`)
| Token | Value | Use |
|---|---|---|
| `--paper` | `#f3f3f1` | page background: a neutral off-white, so the pixel art carries the colour |
| `--surface` / `--card` | `#ffffff` | cards and panels |
| `--ink` / `--ink-2` / `--muted` | `#141414` / `#424242` / `#6f6f6f` | text, strongest to softest (true neutrals, no tint) |
| `--line` / `--line-2` | `#e4e4e1` / `#d4d4d0` | borders and dividers |
| `--accent` / `--accent-strong` | `#d94a7a` / `#c4365f` | a deep rose: the main action and progress |
| `--accent-soft` | `#f9e6ec` | the rare pale-pink fill |
| `--amber` / `--amber-soft` | `#8f5c14` / `#f5ead6` | the honey tone: progress, warmth |
| `--sea` / `--sea-soft` | `#2c6a88` / `#e2edf2` | water, maps |
| `--danger` | `#9b3b2a` | delete and reset only |

Rules:
- **Pink is rare.** One pink button per screen at most, plus progress (ticks, bars, unlocked pieces). No pink backgrounds on pages.
- Titles and labels are near-black (`--ink`), not grey and not pink.
- Use the tokens. A new hex value in the code needs a reason.

## Type
- Headings: **Instrument Serif**, regular weight, no italics. Body and UI: **Manrope**.
- Sizes: see the type scale above. Onboarding headings stay 24px with 14px body.
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
- Pieces are pixel art: crisp edges, a thin dark outline, and hard shadows with no blur (`drop-shadow(0 3px 0 …)`).
  Never fade, feather or mask their edges.
- Shadows elsewhere are neutral (`rgba(20,20,20,…)`), never brown-tinted.
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
