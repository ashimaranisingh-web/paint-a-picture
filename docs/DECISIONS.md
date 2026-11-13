# Decisions

Product decisions and why. Newest first. Don't reverse one without the owner saying so, and when they do, add a new
line rather than editing the old one.

## 2026-11
- **Account header and name step (13 Nov, later):** the Account header is a pixel scene with the character, like
  onboarding (no pink); photo, name, email and place chips sit below it on white. When the header sticks at a quarter of
  the screen, the character stays (scaled to fit) so edits to it show live. The onboarding name step is headed
  "Let's Paint You!" with no sub-line (an owner-approved exception to "no exclamation marks"), and the name fields use
  the playful prompts again as placeholders: "What should we call you?", "Got a fancy middle name?", "Last name duh."
- **Account header collapses (13 Nov, later):** scrolling slides the pink header up until a quarter of the screen is
  left, then it stays; the character fades, the back button, photo, name, email and places stay. Places show as glass
  chips you can drag sideways; tapping one opens that place on My Picture.
- **Your Places (13 Nov, later):** "Places in your world (n)" is now "Your Places (n)", and Account lists your places
  under your name and email. Drop-downs keep room for their arrow so labels never run under it.
- **Card sizing (13 Nov, later):** card corners 12px at most, 12px padding inside, 12px between cards.
- **Your own photos on pieces (13 Nov, later):** a piece can hold up to 6 of the person's own photos (optional), added
  in the piece sheet above the picture library and shown as a strip when the piece is opened; tap one to see it large.
  Each is shrunk to 480px and saved with the world (`photos` on the piece), so it syncs like the rest.
- **First tab renamed My Picture (13 Nov, later):** the map tab is "My Picture" (was "My World").
- **Sync never asks (13 Nov, later):** when the device and the account both changed, the account (the email you
  sign in with) always wins, with no pop-up. The device's version is still kept on the device (`dreamLife.otherWorld`)
  and can be downloaded from Account. Replaces "ask only if both changed" in the sync rule below.
- **Account, simplified (13 Nov, later):** no joined date and no places/pieces/goals counts under the name; sections
  sit on the page with dividers (no cards); order is name, character, usage sharing, Sync, Help, then Delete account.
- **Cards back (13 Nov, later):** the lists-instead-of-boxes trial is reversed; content sits in the soft white cards
  again (faint ring, wide soft shadow, 20px corners) on the white page. The More list stays plain rows with dividers, no card.
- **Tab bar as a straight band (13 Nov, later):** square corners and a hairline along the top, still glass.
- **Tab bar, revised (13 Nov, later):** the bar sits on the bottom edge (rounded top corners, glass) instead of
  floating; the current tab is rose. Tabs renamed My World, Pieces, Goals, Journal, plus a fifth, **More**, that lists
  To-do, My Assets, Good things and Affirmations, so none is hidden inside another tab. Goals and Journal lose the
  To-do / Assets sub-tabs added earlier the same day.
- **Floating tab bar, four tabs (13 Nov):** World, Picture, Goals, Journal, the same on every screen. To-do sits
  inside Goals (milestones and to-dos are both things to do), Assets inside Journal (records of what you've built). The
  menu is no longer opened: Account is your photo at the top right, Help moved into Account. Every "Journal" now opens
  the same page, on the tab last used. Replaces the Home Goals/Journal buttons and the two-item bar on pages.
- **Sunlight on the water (13 Nov):** the sea keeps its blue through the day; the time of day shows as the sun's
  reflection (a path of glints that moves from right to left and changes colour), not as a tint over the water.
- **Time of day on Home (13 Nov):** replaces the 7pm on/off night switch with gradual light: dawn, morning, sunny
  afternoon, golden hour, sunset, dusk and night, blended minute by minute from the phone's clock.
- **Drift circuit always on land (13 Nov):** the Japan island's random shore was cutting the track. The circuit now
  sits a little further inland and keeps a rounded shore of its own.
- **Goal dates (13 Nov):** "By when" offers the same ranges as pieces (Within 2 years, 2–5, 5–10, 10–15 years) or an
  exact date. Nothing is assumed for a new goal (it used to default to a month away). A range sets the deadline to the
  end of that range from today; `timeframe` is saved on the goal.
- **One text field style (13 Nov):** filled grey with rounded corners instead of an underline, because underlines
  doubled up with the row hairlines.
- **Menu order (13 Nov):** Paint a Picture, Journal, To-do list, My Assets | Account | How to explore, See the
  introduction again. It no longer touches the left edge.
- **Lists instead of boxes, on every screen (13 Nov, trial):** items sit on the white page with a hairline between
  them and space between groups, as in Apple's Photos and Music. Sheets, pop-ups, the menu and map controls keep their
  surface. Undo by removing the "lists, not boxes" block at the end of the stylesheet.
- **White page, soft cards (13 Nov):** the grey page (#f3f3f1) read as dull, with grey page, grey header and white
  cards too close in tone. The page is now white across the app; cards stay white with a faint ring, a wide soft shadow
  and 20px corners, after references from Fuse and Cal AI. Replaces the page colour from the Gallery palette (12 Nov).
- **Onboarding refinements (13 Nov, later):** footer is iOS-style: back top left beside the progress line, one
  full-width Continue at the bottom, "Not now" / "Skip" as quiet text under it. The character's scene runs to the top
  and both edges. "A woman / A man" sits above the name. Where you live is never assumed: the row asks, and the time
  zone only suggests a city inside the search. The first goal is written by the person: choose the piece, edit the
  goal, add/remove/edit milestones (the self-tick "Set my first goal" milestone is gone). The usage question is a
  centred pop-up with what's counted and what never is.
- **Onboarding rebuilt: value before asks (13 Nov):** splash (shorter) → one idea screen ("Paint the future you want,
  piece by piece." with the chain, button **Start my picture**, and "I already have an account") → **Who's in your
  picture?** (name, optional full name and photo, character on one page) → **Pick your pieces** with one line for
  where you live now, guessed from the time zone → **first goal**, where she ticks the first milestone ("Set my first
  goal") herself and its piece starts to come to life → **Save your picture** (email code, or Not now) → reveal →
  Home. Everyone, guests too, builds a picture first; the email ask comes once there's something to lose. Replaces
  "Onboarding reordered (12 Nov)": the separate intro screen, the features carousel and the "Where does it happen?"
  page are gone (pages explain themselves when empty; other places are added on the map). A guest who says Not now
  keeps the goal made during onboarding on the device.
- **Home hints cut from seven to two (13 Nov):** drag/zoom, then where Goals lives. The usage question waits until
  the hints are done, and never shows over onboarding.
- **Gallery palette and pixel-true pieces (12 Nov):** neutral off-white page (#f3f3f1), white cards, true black text,
  a deeper rose accent (#c4365f) instead of hot pink; all brown-tinted shadows made neutral. Pieces lose their fades and
  feathering: crisp edges, dark outline, hard shadow. Chosen from a side-by-side of four palettes and four piece styles.
- **Premium design pass (12 Nov):** one card, one tab and one chip style; pink only for the main action and
  progress; quieter labels and a short type scale; serif for titles only; 8-point spacing; shadows instead of outlines;
  no looping animations; calmer copy ("What should we call you?"). Details in docs/DESIGN.md.
- **Onboarding copy and layout (12 Nov, later):** intro is one line, "We all have a picture of the future we want,
  painted piece by piece." How it works: "A picture isn't painted in a day." with the chain as the visual's heading,
  and it must fit on one screen. The features screen is a carousel of little screens. The photo sits at the top of
  the name step with Replace and Remove. Pieces beside the character are 62px. The first-goal page shows: the piece
  to start with → the goal (and what it unlocks) → numbered milestones to tick later, with no checkboxes.
- **Onboarding reordered (12 Nov):** intro → how it works (on a sample picture) → what else is in the app (weekly
  log, journal, assets) → "Let's start painting your picture" with email → character. Guests go Home from the
  character. Signed-in people choose **Build my picture** (name → places → pieces → first goal → reveal) or **Skip to
  Home**. This replaces "explain it on her own picks": the explanation now comes before any picks. The onboarding
  journal step was dropped.
- **Home tour** gained three pointers after the gestures: adding pieces (menu), Goals and Journal.
- **Journal and Weekly Journal are one page** called Journal, with Weekly and Journal tabs. The Journal tab keeps
  Notes, Good things and Affirmations.
- **Intro line:** "The city or career we want. We paint that future piece by piece through milestones." (not "dream").
- **Project docs added** (CLAUDE.md, docs/). Rules live in the repo so every session follows them.
- **Account deletion** runs in a Supabase Edge Function (`delete-account`). It deletes the sign-in first; the saved
  world goes with it (cascade). Only the caller can be deleted, identified by their own token. Required by Apple.
- **Usage counts on PostHog EU Cloud**, moved from US. Opt-in with a short consent line; anonymous id; no personal
  text; Demo mode never counted.
- **Accounts with Supabase, email code sign-in** (no passwords, no magic links: codes work inside the iOS app).
- **Sign-in comes right after the intro**, with Skip. Guests choose A woman / A man, then go Home.
- **Guests can only add places and pieces.** Goals, milestones, journal, notes, to-dos, good things, affirmations and
  assets ask them to sign in first. Existing data is never hidden.
- **Sync rule:** when device and account differ, keep the side that changed since the last sync; ask only if both
  changed. The world not kept is saved on the device (`dreamLife.otherWorld`), never thrown away.
- **Account page:** a full-bleed header to the top of the screen with the character, photo and full name; character
  options in separate boxes; Sync at the bottom; Delete in a centred pop-up. The Data section was removed.
- **Demo Data** switch only for the owner's account (`app_metadata.demo_access`).
- **Sunglasses on by default** (reversed an earlier removal). Caps stay removed.
- **Gender back for guests** as "A woman / A man" (reversed the Hair Long/Short swap) so men see a relatable character.

## Earlier
- **Onboarding explains once, using the person's own data**: their places and pieces build the "how it works" puzzle.
- **First goal and a journal step** are in onboarding; the reveal stays locked with the first piece glowing.
- **Map:** light endless daytime sea, fog on land only, continuous land with filler between places, boats and dolphins,
  night by local time, places strip shows five at a time with full names.
- **Real places only:** "By the sea" and "A small town" were removed.
- **Ten city categories stay.** No "dream" in copy.
- **Demo Data and the person's world are always separate.**
