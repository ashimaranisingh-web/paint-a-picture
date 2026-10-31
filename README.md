# Paint a Picture

A goal journal wrapped in a pixel-art world that each person builds from their own places: where they're from, where they want to live, study, work or explore. Describe the life you want in 10–15 years, set goals with deadlines, and log what you actually do each week. Places you've lived and where you live now are fully lit; places you want to get to start dark and come to life as you finish the goals linked to their dreams. Once a day you can see the whole picture for a minute. Miss one and you lose nothing.

## Run it
Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8000
```

## How it's built
- Onboarding (7 steps, resumable): welcome, name and optional email, destinations, dreams, character, first goal, world. Everything is editable later.
- The world is a 2D grid of districts, one per destination, placed roughly by latitude and longitude. Delhi, Mumbai, Los Angeles, Boston and Japan have their own art; anywhere else uses a neutral pack (city, coast, mountains & lakes, university town, small town) labelled with the place's name.
- Navigation: drag or two fingers to pan in any direction, pinch / wheel / +− to zoom, tap to move the lens, drag the lens itself to move it.
- Dream pictures come from a built-in library matched to the words of the dream, or an uploaded photo. Nothing is picked automatically.
- My Assets (menu): a personal archive in custom categories (create, rename, reorder, delete), each item with a note, date, status, link, cover and tags.
- Journal (menu): private notes with automatic date and time (editable), pins, favourites, All / Pinned / Favourites filters and search.
- This week: jump to any week by date and search everything logged (entries, reflections, goals, steps); past weeks are never reset.
- Accounts: guests keep everything in the browser. There is no sign-in yet and no email is asked for; the plan is Sign in with Apple plus iCloud in the App Store app. Inside claude.ai the data syncs to the viewer's own Claude account.
- One self-contained file: HTML, CSS and plain JavaScript. No build step.
- The world is drawn procedurally on a canvas in three layers: terrain (built once), dream landmarks (rebuilt only when dreams change) and per-frame life (character, traffic, water). Only the visible part is drawn each frame; the fog and lens are composited on a viewport-sized canvas.
- The player character is a pixel-art translation of the owner's character sheet, with front, back and side views and walk/idle frames.
- City landmarks: each place can show one recognisable landmark (28 drawn so far, from India Gate to the Golden Gate Bridge), matched to the dreams placed there and changeable in Edit place. Places without artwork get none rather than another city's monument.
- Character: two styles of the same character. Pixel art (girl or boy, with skin tone, top, cargos, boots, sunglasses and a cap) or Detailed 2D, the illustrated character sheet in `avatar/` (front, back and both sides) with skin, top, cargos and boots recoloured over its parts. Set in onboarding, changeable in Account.
- Data is saved in the browser (`localStorage`). When opened as a claude.ai artifact it also syncs to the owner's private store and can use Claude for goal matching; outside claude.ai it falls back to local keyword matching.

Live artifact: https://claude.ai/artifact/B4MDarDt35HqJsXJCguokv

## How goals unlock the world
- Each place has a stage: lived here before, live here now, or want to get to (`d.stage`). Past and current places are fully lit.
- A dream's progress is the share of its linked goals that are finished. A goal linked to several dreams counts 1/k towards each, so it's never counted twice. Let-go and deleted goals don't count; reopening a goal takes its share back.
- A future place's progress uses the same weighting over all goals linked to its dreams. The district lifts from dark as it rises, each dream lights by its own goals, and the place's landmark appears from 50% and is complete at 100%.
- Everything is calculated from the goals data, so the world can't drift out of step with it. The last level you saw is kept in `revealSeen`; when it has gone up, the change plays on the map the next time you open your world.
- Past places get a one-time review: tick the goals you achieved there and they move to Finished, marked "Achieved in …". Nothing is assumed, and they don't count as on-time finishes.
- Tapping a dream's card on the map steps inside it: its picture, description and the goals that build it.

## Backup
Account → Download backup saves everything (dreams, goals, steps, entries, reflections, device-only images) as one JSON file. Account → Restore from file loads it back, after a confirmation.
