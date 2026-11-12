# Paint a Picture

A goal journal wrapped in a pixel-art world that each person builds from their own places: where they're from, where
they live, and where they want to live, study, work or explore. They describe the life they want as **pieces** of a
picture, set **goals** with **milestones**, and keep a **journal**. Places they've lived and live now are fully lit;
places they want to get to start in fog and come to life as the goals linked to their pieces are finished.

Live: https://ashimaranisingh-web.github.io/paint-a-picture/ · iOS: TestFlight (see [docs/RELEASE.md](docs/RELEASE.md))

## Run it
Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

## Project docs
- [CLAUDE.md](CLAUDE.md): working rules for anyone (or any AI session) changing this project
- [docs/DESIGN.md](docs/DESIGN.md): colours, type, motion and voice
- [docs/QUALITY.md](docs/QUALITY.md): checks before shipping, including the "no AI slop" list
- [docs/RELEASE.md](docs/RELEASE.md): website, TestFlight, Supabase and PostHog steps
- [docs/DECISIONS.md](docs/DECISIONS.md): what was decided and why
- [supabase/README.md](supabase/README.md): accounts, sync, account deletion and usage-count setup

## What's in the app
- **Onboarding:** a splash on the LA coast, the idea, how it works (milestones → goals → pieces → picture), what else
  is in the app, then **email or skip**, then the character.
  - Signed in: **Build my picture** (name → places → pieces → first goal → the locked picture with the first piece
    glowing) or **Skip to Home**.
  - Skipped email (guest): straight to Home.
  - Home starts with a short tour: drag, zoom, tap, walk, then where pieces, Goals and Journal live.
- **Guests** can add places and pieces. Goals, milestones, the journal, notes, to-dos, good things, affirmations and
  assets ask them to sign in first. Nothing they already have is hidden.
- **The world:** a light, endless daytime sea with land built from the person's real places (placed by latitude and
  longitude), filler land between them, roads, boats and dolphins. Fog sits on land only. Night follows local time.
  Drag or two fingers to pan, pinch / wheel / +− to zoom. A strip shows five places at a time.
- **Landmarks:** 35 drawn so far (India Gate to the Golden Gate Bridge), matched to the pieces placed there and
  changeable in Edit place. Places without artwork get none rather than another city's monument.
- **The clear view:** once a day, the whole picture without fog for one minute.
- **Journal:** one page, two tabs. **Weekly**: log what moved each week, a weekly review, jump to any week and search
  everything logged (past weeks are never reset). **Journal**: notes (pins, favourites, filters, search), three good
  things a day, and affirmations.
- **My Assets:** a personal archive in sections of cards (create, rename, reorder, edit, delete).
- **Account:** a full-height header with the character, photo and full name; character options (Pixel art or 2D,
  skin, hair, outfit; sunglasses on by default); Sync; Delete account.
- **Demo Data:** a separate sample world, kept apart from the person's own, available only to the owner's account.

## How it's built
- One self-contained file, `index.html`: HTML, CSS and plain JavaScript. No build step.
- The world is drawn on a canvas in layers: terrain (built once), landmarks (rebuilt only when pieces change) and
  per-frame life (character, boats, water). Only the visible part is drawn each frame.
- The character has two styles: pixel art, and a 2D figure cut from the sheets in `avatar/` (a woman, and `male-*`
  for a man), recoloured over its parts.
- `ios/` wraps the same page in a WKWebView app (`ios/project.yml`, generated with xcodegen).

## Data, accounts and privacy
- Everything is saved on the device first (`localStorage`).
- **Accounts** use Supabase with email code sign-in (no passwords). A signed-in person's world syncs to their account
  and across devices. When device and account differ, the side that changed since the last sync wins; if both
  changed, the app asks. The world not kept is saved on the device, never thrown away.
- **Account deletion** (Account → Delete account) removes the sign-in and the saved world, through the
  `supabase/functions/delete-account` Edge Function.
- **Usage counts** go to PostHog (EU) only if the person says yes. They're anonymous: event names only, never names,
  emails, goals or journal text. Demo mode is never counted.

## How goals light up the world
- Each place has a stage: lived here before, live here now, or want to get to (`d.stage`). Past and current places are
  fully lit.
- A piece's progress is the share of its linked goals that are finished. A goal linked to several pieces counts 1/k
  towards each, so it's never counted twice. Let-go and deleted goals don't count; reopening a goal takes its share
  back.
- A future place's progress uses the same weighting over all goals linked to its pieces. The place lifts out of the fog
  as it rises, and its landmark appears from 50% and is complete at 100%.
- Everything is calculated from the goals, so the world can't drift out of step with them. The last level seen is kept
  in `revealSeen`; when it has gone up, the change plays on the map the next time the world opens.
- Past places get a one-time review: goals achieved there move to Finished, marked "Achieved in …". Nothing is assumed,
  and they don't count as on-time finishes.
