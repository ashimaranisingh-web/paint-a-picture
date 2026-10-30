# Paint a Picture

A goal journal wrapped in a pixel-art world that each person builds from their own places: where they're from, where they want to live, study, work or explore. Describe the life you want in 10–15 years, set goals with deadlines, and log what you actually do each week. Your world starts in the dark; real progress on goals linked to a dream makes that place clearer. Meet a deadline and you earn a 10-second view of the whole picture. Miss one and you lose nothing.

## Run it
Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8000
```

## How it's built
- Onboarding (7 steps, resumable): welcome, name and optional email, destinations, dreams, character, first goal, world. Everything is editable later.
- The world is a 2D grid of districts, one per destination, placed roughly by latitude and longitude. Delhi, Mumbai, Los Angeles, Boston and Japan have their own art; anywhere else uses a neutral pack (city, coast, mountains & lakes, university town, small town) labelled with the place's name.
- Navigation: drag or two fingers to pan in any direction, pinch / wheel / +− to zoom, tap to move the lens, drag the lens itself to move it.
- One character, two render modes: the pixel sprite, or a detailed 2D figure drawn with vector paths on a crisp overlay that gains detail as you zoom in.
- Dream pictures come from a built-in library matched to the words of the dream, or an uploaded photo. Nothing is picked automatically.
- Accounts: guests keep everything in the browser. Email sign-in and cross-device sync are not built yet; the email field is stored locally only. Inside claude.ai the data syncs to the viewer's own Claude account.
- One self-contained file: HTML, CSS and plain JavaScript. No build step.
- The world is drawn procedurally on a canvas in three layers: terrain (built once), dream landmarks (rebuilt only when dreams change) and per-frame life (character, traffic, water). Only the visible part is drawn each frame; the fog and lens are composited on a viewport-sized canvas.
- The player character is a pixel-art translation of the owner's character sheet, with front, back and side views and walk/idle frames.
- Data is saved in the browser (`localStorage`). When opened as a claude.ai artifact it also syncs to the owner's private store and can use Claude for goal matching; outside claude.ai it falls back to local keyword matching.

Live artifact: https://claude.ai/artifact/B4MDarDt35HqJsXJCguokv

## Backup
Account → Download backup saves everything (dreams, goals, steps, entries, reflections, device-only images) as one JSON file. Account → Restore from file loads it back, after a confirmation.
