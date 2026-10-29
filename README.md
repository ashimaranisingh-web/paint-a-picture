# Dream Life

A goal journal wrapped in a pixel-art world. Describe the life you want in 10–15 years, set goals with deadlines, and log what you actually do each week. Your world starts in the dark; real progress on goals linked to a dream makes that place clearer. Meet a deadline and you earn a 10-second view of the whole picture. Miss one and you lose nothing.

## Run it
Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8000
```

## How it's built
- One self-contained file: HTML, CSS and plain JavaScript. No build step.
- The world is drawn procedurally on a canvas; the fog and lens are composited per frame.
- Data is saved in the browser (`localStorage`). When opened as a claude.ai artifact it also syncs to the owner's private store and can use Claude for goal matching; outside claude.ai it falls back to local keyword matching.

Live artifact: https://claude.ai/artifact/B4MDarDt35HqJsXJCguokv
