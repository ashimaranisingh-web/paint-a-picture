# Paint a Picture

A goal journal wrapped in a pixel-art world: one continuous map from Delhi and Mumbai, across the ocean, to Los Angeles. Describe the life you want in 10–15 years, set goals with deadlines, and log what you actually do each week. Your world starts in the dark; real progress on goals linked to a dream makes that place clearer. Meet a deadline and you earn a 10-second view of the whole picture. Miss one and you lose nothing.

## Run it
Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8000
```

## How it's built
- One self-contained file: HTML, CSS and plain JavaScript. No build step.
- The world is drawn procedurally on a canvas in three layers: terrain (built once), dream landmarks (rebuilt only when dreams change) and per-frame life (character, traffic, water). Only the visible part is drawn each frame; the fog and lens are composited on a viewport-sized canvas.
- The player character is a pixel-art translation of the owner's character sheet, with front, back and side views and walk/idle frames.
- Data is saved in the browser (`localStorage`). When opened as a claude.ai artifact it also syncs to the owner's private store and can use Claude for goal matching; outside claude.ai it falls back to local keyword matching.

Live artifact: https://claude.ai/artifact/B4MDarDt35HqJsXJCguokv

## Backup
Account → Download backup saves everything (dreams, goals, steps, entries, reflections, device-only images) as one JSON file. Account → Restore from file loads it back, after a confirmation.
