# Design and voice

How Paint a Picture looks and sounds. When a screen doesn't match this, fix the screen or update this file on purpose.
Never both drift.

## Feel
Calm, premium, a little playful. A gallery wall for a pixel-art world: a white page, true black type, one deep rose
for what matters. The world brings the colour; the interface stays quiet.

## The design system (Nov 2026)
The last block of the stylesheet, "DESIGN SYSTEM", is the source of truth; older rules above it are layers it
overrides. New components use these, never new one-off styles.

- **One card:** white on the white page (`--card`), 12px corners at most (`--card-r`), 12px padding inside and 12px
  between cards, set apart by a faint ring and a wide,
  very soft shadow (`--card-sh`), never a visible border. (Lists without cards were tried on 13 Nov and reversed.)
- **One tab:** the segmented control (`.seg`): a light tray, the chosen tab white with a small lift.
- **One text field:** a soft grey fill (#f3f3f2), 12px corners, no underline or border. Typing turns it white with a
  thin ink ring, never pink. Text 16px (smaller makes iPhone zoom in). Big onboarding moments (the name) may differ.
- **Navigation: a tab bar on the bottom edge** (a straight full-width band with a hairline on top, glass; dark glass over the world at
  night) with five tabs: **My Picture**, **Goals**, **This week**, **Journal**, **My stuff** (My Assets); **Pieces** opens from a plain jigsaw-piece icon (no background) at the top right of Home, beside the clock (To-do list, My
  Assets, Good things, Affirmations as a plain list). The current tab is in the rose accent. Tab pages have no back
  arrow; pages opened from More do. **Account** is a pink circle with your initials at the top left of Home (My Picture) only, beside the greeting; the top right shows the time in 24-hour form (the time the world's light follows); Help lives in Account. Journal reopens
  on the tab last used.
- **The menu** never touches the screen edges (at most 320px wide). Order: make (Paint a Picture) → keep (Journal,
  To-do list, My Assets) → you (Account) → help, with a divider between groups.
- **One chip:** white with a hairline ring (`--ring`); chosen is **ink** with white text.
- **Pink is rare:** the main button on a screen, ticks, progress bars, unlocked pieces and the star. Links, quiet
  buttons, chosen chips, the tab bar and labels are ink or grey.
- **Quiet buttons on hover** ("+ New", "Add goal" and other text-only buttons): accent text on the pale accent tint. Only on screens with a pointer; on iPhone they stay ink.
- **Type scale:** 28 page titles (serif), 22 sheet and pop-up titles (serif), 17 section and card titles (sans, bold),
  15 body, 13 small. Labels are 13px, normal case, grey: no all-capitals eyebrows.
- **Serif only** for page titles and big moments (onboarding headings, the weekly review line, good things,
  affirmations, the loader). Everything inside a page is the sans.
- **Spacing:** 8-point rhythm (8 / 12 / 16 / 24 / 32). 20px side margins everywhere. 24px between sections, 12px
  between cards, 16px inside cards.
- **Surfaces, not outlines:** a card has a shadow or a hairline, never both.
- **Motion:** one signature moment (a piece unlocking). Nothing loops; no wiggling icons or pulsing rings.
- **Copy:** at most one playful line per flow; no exclamation marks.

## New direction (14 Nov, being rolled out)
Playful, whimsical, editorial: hand-drawn children's-book illustration meets modern graphic design. Slightly imperfect
and expressive, never corporate-polished. **No** pastels, gradients, beige, muted earth tones or "wellness app" pink-and-
purple. One electric pink (`--accent`) is the dominant UI colour, the way cobalt leads the references. Bright raspberry,
orange, grass green and sky blue appear only in illustrations, painted days and celebrations, never across UI parts.
- A Journal trial of the full look (paper-grey page, all-pink text, hand-lettered Gaegu titles, DM Mono writing) was
  tried on 14 Nov and reverted the same day. Only the new pink stays.
- Where this conflicts with older rules below ("pink is rare", serif titles), the new direction wins on pages that
  have moved to it.

## Colour (tokens in `:root`, top of `index.html`)
| Token | Value | Use |
|---|---|---|
| `--paper` | `#ffffff` | page background: white, so the pixel art carries the colour (was `#f3f3f1` until 13 Nov) |
| `--surface` / `--card` | `#ffffff` | cards and panels |
| `--ink` / `--ink-2` / `--muted` | `#141414` / `#424242` / `#6f6f6f` | text, strongest to softest (true neutrals, no tint) |
| `--line` / `--line-2` | `#e4e4e1` / `#d4d4d0` | borders and dividers |
| `--accent` / `--accent-strong` | `#ea4c8e` / `#d0326f` | bubblegum pink from the cat-toy reference (hue 336); deeper one behind white text (lilac and electric raspberry were tried on 14 Nov, rose `#d94a7a` before that) |
| `--accent-ink` | `#c4286a` | accent-coloured text |
| `--accent-soft` | `#fde4ef` | the rare pale-pink fill |
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
- Home's top right holds, right to left: the puzzle piece (Pieces), the eye (clear view), the clock. Plain icons, no circles. There are no other map buttons.
- Padding: 24px around content in onboarding, 16px page gutter in the app.

## The world (canvas)
- Pixel art. More detail, not more complexity.
- The sea is light, daytime and endless. Fog sits on land only, never on the sea.
- Land is continuous; roads stay on land. Boats and dolphins on the water, nothing floating.
- The light follows the person's phone clock and changes gradually: night (about 8pm–5am), a blue hour and peach
  dawn (5–7am), clear morning, a warm sunny afternoon, golden hour (around 5pm), a pink sunset (6pm), a violet dusk, then
  night. Colours live in `LIGHT_KEYS`; `LIGHT_H` previews an hour.
- Revealed places stay lit after dark: they take only part of the night's darkness plus a warm streetlight glow, so at
  night they never look like the fog over future places.
- The water always reads as water: the land takes the full colour of the hour, the sea only a little. Light shows on
  the sea as reflection: a soft path towards the sun (rising right, setting left) broken into shimmering streaks, white
  at midday, gold at golden hour, orange-pink at sunrise and sunset, a few silver glints under the moon (`SEA_KEYS`).
- A place's drawing always sits on land: a pack can mark ground it needs (`keep`), so a random shore never cuts it.
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
- **Journal year, how it's used:** one tap on a day shows its date in a pink pill above it ("Thursday, 05.11", DM Mono); a double-tap opens the day. Month names are small, grey capitals so the dots lead.
- **Journal is a year of circles.** Empty days are tiny grey pen dots, nudged off-centre as if dotted by hand (the full 45px square is still the tap area); future days are fainter dots; and today sits on a pale pink disc (`--accent-soft`). A filled day is a doodle in its colour, like felt pen on paper: a slightly wobbly hand-drawn ring and the face's lines, thin, on white (no fill). A day linked to a goal, milestone or piece wears a small pink link badge at its top right, like the star on the map.
- Words we use: **picture, pieces, goals, milestones, places, journal**. Goals bring pieces; milestones are steps.
- Never "dream" in visible copy. No exclamation-mark cheerleading, no "unlock your potential", no emoji in UI copy.
- Error and empty states say what happened and what to do next, in one line.

## Onboarding character screens (13 Nov 2026)
- The page is white. The character stands on a pixel scene from the world (grass, a path, the sea) that runs to the
  top and both edges, never on a blank page. Back and the progress line float over it.
- Onboarding footers: one full-width primary button (52px, 14px corners); any second choice is quiet text under it.
- Permission-style questions (usage sharing) are a centred pop-up over a dimmed screen, never a banner. The rest of the app keeps the Gallery palette.
- How-it-works jigsaw: each piece is its cell plus a tab's width (a sixth) each side, so pieces sit inside the frame
  and lock together exactly.
- The welcome screen has no progress line; it isn't a step. Progress counts only the steps of making the picture.
- **One shadow for things that float over the map** (place card, places strip, chips): `0 1px 2px rgba(20,20,20,.06), 0 8px 22px -10px rgba(20,20,20,.28)`. A bigger shadow spills onto whatever sits just below it.
- **Dates:** a single day always reads "Sat, Nov 1" (short weekday, short month, day; "Tues" and "Thurs" spelled that way), with ", 2026" only where the year is needed. One helper (`fmt`) does it for the whole app.
- **Glass pill** (the Journal year), Apple style: mostly clear white with a whisper of pink, strong blur behind, a hairline bright edge with a brighter top rim, and a soft wide shadow. Never a solid coloured fill. It sits at the far right of the Journal title row (and stays there while scrolling); tapping it opens a small glass list of years. No arrows.
