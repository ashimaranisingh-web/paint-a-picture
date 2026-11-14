# Decisions

Product decisions and why. Newest first. Don't reverse one without the owner saying so, and when they do, add a new
line rather than editing the old one.

## 2026-11
- **Horizon removed (13 Nov, late):** the 5/10/15-year Horizon picker on the Pieces page did nothing visible, so it's
  gone. The saved value (`profile.horizon`) is left in old saves untouched.
- **Pieces page and map polish (13 Nov, late):** the Pieces page header holds its intro above the line, with tabs
  **Your World** (places) | **Your Pieces**; the categories sheet drops piece counts; milestones are added only in the
  goal's Edit sheet (no inline field on the card); piece photos open as a full-screen slideshow; landmark cards show a
  pixel picture cut from the map; a double tap on the map closes in on the character. At night, revealed places keep
  only a little of their daytime colour so it reads as night.
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
- **Journal: "How was today?" (14 Nov):** the Notes tab opens with one writing box, dated automatically to the moment it's saved. After saving, a short reply congratulates a good day ("Well done") or encourages a hard one ("Keep going"). The mood is read on the device with a small word list (it understands "not bad"); journal text is never sent anywhere. Each entry keeps its mood and reply (`mood`, `reply` on the note, both optional, so old notes load as before). New note, search, pin and favourite all stay.
- **Journal page trimmed (14 Nov):** removed the subtitle, the Notes / Good things / Affirmations tabs and the All / Pinned / Favourites filter. The date sits on the right of "How was today?". Good things and Affirmations open from More, with their own title and a back arrow. Pin and favourite still exist inside a note.
- **One-page pieces, one goals list, lighter onboarding (14 Nov):**
  - Weekly: Log progress shows once (in the empty list when nothing's logged, top right otherwise). The Weekly review panel is removed.
  - Pieces page is titled "Your pieces". No tabs: "Your world" (places, no card) at the top, then pieces by category.
  - Goals: no Active / Finished tabs. Active goals first, Finished and Let go below. Each goal card shows its piece's pixel art.
  - Onboarding: buttons say "Next"; the photo is no longer asked (it stays in Account); Style sits above "You are"; the first-goal step has no sub-copy and asks for the goal plus one first step (more steps in Goals).
  - Fixed: the intro screen scrolled sideways on tall phones.
- **Intro screen trimmed (14 Nov):** only the headline above the animation (the sub-line and the "Milestones → Goals → Pieces → Picture" text are gone; the animated rows tell it). "Start my picture" fades in once the picture has come together (straight away with Reduce Motion or when coming back). The row labels are larger and dark so they read as a sequence.
- **Year in colour (Journal).** Each day can get one colour for how it felt, mixed with two sliders: colour (bright, not pastel) and light to dark. Tap any past day to colour it. The sliders are thin lines at 65% saturation (rich, not neon). Shown as one month at a time: a dot per day in the accent pink, and a coloured day becomes a hand-painted swatch (Week and Year views were tried and dropped). Saved as `days` (`{"YYYY-MM-DD": "#hex"}`) through `normalize()`. The colour is separate from the written entry.
- **New visual direction (14 Nov):** playful, hand-drawn, editorial (references: the "one year" app screens). Pink becomes the dominant UI colour: the accent changes from rose `#d94a7a` to electric raspberry `#d6005a` app-wide. Journal is the pilot for the full look: warm paper-grey page, everything in pink, Gaegu titles, DM Mono writing. Reverses "pink is rare" on pages that move over.
- **Home header and Account trimmed (14 Nov):** Account moves to the top left as your initials (pink circle) instead of your photo at the top right; the top right now shows a quiet 24-hour clock so the changing light makes sense. The Account page no longer shows the photo or the row of place chips beside your name.
- **Journal look reverted (14 Nov):** the hand-drawn trial on Journal (grey paper, all-pink text, Gaegu and DM Mono) is undone; Journal is white with the usual fonts again. The electric pink accent, the colour-your-day sliders and the month of dots stay.
- **Account character moved (14 Nov):** the big scene with the character at the top of Account is gone; the page opens with a plain "Account" title and back arrow, then your name. The character now stands in a small piece of her world inside "Your character", right above the choices that change her.
- **Accent tried as lilac (14 Nov):** the app-wide accent moves from electric pink to a lilac purple (`#9466f0`, darker `#7d4fdc` for buttons) as a trial. Pink illustrations (blossoms) stay as they are. Going back is one line in `:root`.
- **Lilac made bolder (14 Nov):** the first lilac (`#9466f0`) read as pastel. Now `#7f35d4` (hue 268 at 65% saturation, the same strength as the day-colour sliders and the purple in the year-app reference), so it's a pop colour, not a soft one.
- **Quiet button hover (14 Nov):** text-only buttons like "+ New" turn accent-coloured on a pale accent tint when hovered, instead of a grey wash.
- **Back to pink (14 Nov):** lilac is dropped. The accent is the bubblegum pink of the cat-toy reference (`#ea4c8e`, hue 336), with `#d0326f` behind white text so it stays readable.
- **Daily faces (14 Nov):** Journal opens on the year as circles (scrolled to this month). An entry needs a colour and a face drawn with your finger; a note and links to a goal, milestone or piece are optional. Weekly gets a "Your days" row of the week's faces plus what they were linked to, so weekly progress builds from the days; Log progress stays. The old "How was today?" box and the month view are replaced; earlier colour-only days keep their colour. Saved notes are untouched.
- **Faces are line doodles (14 Nov):** filled days are no longer solid colour; the day's colour draws a thin, slightly wobbly ring and the face, like the hand-drawn garden reference.
- **Day sheet simplified (14 Nov):** the sheet opens with "How are you feeling today?" and one colour slider (the light-to-dark slider is gone; colours are always full strength), then the face, then a long "Journal" page with the date beside it. The "Did something move today?" links and the hint line are removed from the sheet; links already saved stay and still show in Weekly. Journal no longer shows "+ New note" or the Notes list; saved notes are kept in your data, just not shown there.
- **Old notes stay hidden (14 Nov):** notes written before daily faces are kept in saved data but not shown anywhere in the app, by choice. Do not delete them.
- **Empty days are tiny dots (14 Nov):** instead of grey rings, so filled days (ring and face) stand out from a quiet field of dots, like the flower-memory reference.
- **Reading a day (14 Nov):** a filled day opens to read (its face and what you wrote) with Edit at the top; an empty day opens straight to edit. The sheet title is short ("Thurs, Nov 5") and the date is said only once. The question is always "How are you feeling today?", and the Journal box has no label above it. Cancelling an edit goes back to reading.
- **Journal year taps (14 Nov):** single tap shows the date pill, double-tap opens the day (keyboard Enter opens straight away). The Weekly | Journal switch is removed from Journal; a quiet "Weekly" link sits top right so Weekly stays reachable. Month names are now small grey capitals.
- **Year pill and automatic week (14 Nov):** the Journal year header is now a soft pink "2026" pill (DM Mono) with faint arrows; the "days filled" count and the tap hint are gone. Weekly gets "Done this week", filled in on its own from milestones, finished goals and to-dos ticked that week and days linked to something, with a count of days that have a face. Log progress stays below.
- **Sea lines (14 Nov):** when she's sent into the water she says something silly in her bubble ("Ahhh, I'm drowning!", "Look, a shark!", "Where is my yacht?" and a few more).
- **Pieces off the tab bar (14 Nov):** Pieces opens from a round puzzle button at the top right of Home; the tab bar has four tabs.
- **To-do by the day (14 Nov):** a week of days at the top (week pill, tap to return to today), the chosen day's list below. New to-dos go on the chosen day; undated and unfinished earlier ones roll on to today, marked "From Thurs, Nov 12". "By when" in the edit sheet is now "Day".
- **Five tabs, three features out (14 Nov):** tabs are My Picture, Goals, This week, Journal, My stuff (was More; now just My Assets). This week and Journal are separate tabs, so their switch and the "Weekly" link are gone. Good things, To-do and Affirmations are taken out of the app (no way in from anywhere); anything saved for them stays in your data and is not deleted. The Pieces button is a plain jigsaw piece with no circle behind it.
- **Map buttons (14 Nov):** the eye (clear view) moves into the Home header, left of the puzzle piece, as a plain icon (gold when ready or open, faded when used for the day). The bird's-eye map and "show me" buttons are taken out; the places strip still moves you between places.
- **Matched floating shadows (14 Nov):** the place card now uses the places strip's soft shadow, so it no longer greys the strip below it.
- **Places sit like a world map (14 Nov):** islands are placed by real longitude and latitude, west to east (the Americas on the left, Asia on the right; about 30° across and 8° down per place), and the places strip runs in the same order. No more land bridges: every place is its own island, even in the same country (Delhi and Mumbai). Existing worlds are re-laid out once (layoutV 2). Picking a place in the strip also zooms in on it.
- **iOS build 7 (14 Nov):** uploaded to TestFlight with the daily faces journal, This week, the new tab bar and the map-true layout.
