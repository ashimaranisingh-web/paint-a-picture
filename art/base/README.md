# Girl base body: making wardrobe layers that fit it

`girl-base-sheet.webp` is the owner's base body (20 Nov 2026): bald, white bandeau and briefs, front, back, facing left,
facing right, on a transparent background. `girl/` holds it cut into the app's four views (720 px tall, feet on the
bottom edge).

## Why the existing outfits can't be layered on it
`fit-test.png`: with neck and soles lined up, the outfit sheets were drawn on a different body. Shoulders are about a
third wider, the torso is longer, the head is bigger and the arms are held further out. A top or hairstyle cut from
them would float off this body or leave skin showing at the edges. Each item has to be drawn on this body.

## What to make, per item
For every hairstyle, top, bottom, pair of shoes and the sunglasses:

1. Start from `girl-base-sheet.webp` itself (same canvas size, 1024 × 1536, same four figures in the same places).
2. Draw only that item on the body, in all four views, exactly where it sits on her.
3. Export it on a transparent background, with nothing else: no body, no shadow, no other clothes.
4. Plain items in one flat colour with shading (they get recoloured in the app). Patterns (stripes, camo) as they
   should stay.

Name the files like `hair-long-wavy.png`, `top-spaghetti-plain.png`, `top-spaghetti-stripe.png`, `bottom-cargo-full-camo.png`,
`bottom-cargo-34-camo.png`, `bottom-wide-white.png`, `shoes-sneakers.png`, `shoes-boots.png`, `shoes-heels.png`,
`sunglasses.png`. Drop them in `art/base/layers/`; the cutter and the app pick them up from there.

## A prompt for an image tool (attach the base sheet)
> Using the attached character sheet as the exact template, draw ONLY [item, e.g. "a hot-pink spaghetti-strap crop top"]
> on the character, in all four views (front, back, facing left, facing right). Keep the canvas size, the figures'
> positions, pose and proportions identical, so the item lines up pixel for pixel with the body. Output the item alone
> on a fully transparent background: no body, no skin, no hair, no shadow, no other clothing. Same illustration style
> and lighting as the template.

Check a delivery by laying it over the base sheet: every edge should sit on the body with no gaps or overhang.
