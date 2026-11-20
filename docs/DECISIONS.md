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
- **Year pill as glass, one date format (14 Nov):** the Journal year pill gets the frosted-glass look with grey arrows at the far ends; the M T W T F S S row above the year is removed. Dates everywhere read "Sat, Nov 1", including the date pill on a tapped day.
- **Apple-style glass (14 Nov):** the tinted pink glass pill read as heavy; the year pill is now clear Apple-style glass (near-white, hairline edges, soft shadow).
- **Year pill in the title row (14 Nov):** the year pill moves up beside "Journal", far right, and stays visible while scrolling. Tapping it lists this year back to the first year with an entry (at least last year); the arrows are gone.
- **iOS build 8 (14 Nov):** uploaded to TestFlight with the glass year pill in the title row and the "Sat, Nov 1" dates.
- **User testing via Tally (15 Nov):** tester answers are collected in a Tally form (a Claude-hosted form cannot take answers from public-link visitors). Questions and the tester call live in docs/TESTING.md. Account → Help gets a "Help test Paint a Picture" row that appears once `CFG.testFormUrl` holds the form link.
- **Pieces and goals in several places (15 Nov):** a piece can sit in more than one place (it becomes a landmark in each). A goal reaches every place its pieces are in; finishing a goal that spans several places asks "Where did it come true?" and only those places light up (changeable later from the goal card). Older saves load with their one place.
- **Goals get their own photos and pixel art (15 Nov),** like pieces; the goal card shows its own art, or its piece's if none is chosen.
- **High-resolution photos (15 Nov):** full quality is kept on the device (not synced; other devices see the smaller copy). Syncing full-size photos would need Supabase Storage, which isn't set up.
- **This week (15 Nov):** "Done this week" is gone; the search bar and the logged entries remain (Your days stays above).
- **My studio (15 Nov):** the fifth tab is renamed and opens the assets page directly. Your world on Pieces folds open and closed again (closed by default).
- **Onboarding fixes (15 Nov):** a sync no longer throws you out of onboarding to Home (it only does so when the incoming world finished onboarding this device hadn't). The first button reads "Get started". The how-it-works page tells why Ashima made the app, a line at a time in step with the animation. The splash star starts as a tiny spark and grows, gently even with Reduce Motion.
- **Home clock hidden for now (15 Nov).**
- **Account (15 Nov):** the character hero is back at the top, edge to edge under the status bar; name and email sit below it with a pencil that opens a drawer for first, middle and last name. The usage-sharing switch is removed: people answer once during onboarding. (Note: privacy law in the EU/UK expects a way to withdraw consent later; revisit before a public launch.)
- **My studio (15 Nov):** an easel icon in the tab bar. A pink "What are you building right now?" box at the top; each thing you add can become a new goal or a milestone in a goal you have, only if you choose to, or just stay listed there.
- **Onboarding story and name (15 Nov):** the story types itself out under "Paint the future you want, piece by piece" at reading pace, one line at a time (the last line stays); the milestones, goals and picture animation and the Get started button wait until it has finished. The name step shows a "Your name" label and three separate fields (first, middle, last), like Account.
- 15 Nov: Onboarding pieces open with a starter set of 13 broad pieces (own company, fitter body, more wealth, happy family, a pet, top-choice school, 100K subscribers, a career I love, peace of mind, a new skill, partner, world travel, own home) with no heading, then the existing categories below. People must pick at least 5 before moving on, so testers start with a fuller picture.
- 15 Nov: Onboarding progress over the scene: white track, pink fill, a glowing pink dot at its end. When the first piece shows up she says "Drag the pieces around for shits & giggles." beside the hand hint; with Reduce Motion the hand still slides, gently.
- 15 Nov: Dragged onboarding pieces stay where they are dropped (saved in the draft as `at`), instead of snapping to tidy spots. Dropping one on her makes it the first piece (pink ring) and it stays there too, in front of her. A drop never redraws the page, and the first drop pins every piece's spot so nothing reshuffles.
- 15 Nov: A places step is back in onboarding, before pieces ("Add your places"): a search bar and three ideas (Mumbai, New Delhi, New York). Her places rise out of the sea round her as islands, and she stands on a little sandy island of her own. Reverses the earlier "places can wait for the map". The goal step no longer says "Unlocks …" under the goal.
- 15 Nov: One bottom safe area (`--safe-bottom`, 34px in the desktop frame) used everywhere, so the iPhone home bar never covers content. Places step drops "And these are…" (where she lives is set on the pieces step). Pieces step shows only the ten starter pieces (plus any she already has) and Describe your own; no categories. Describe your own offers places added during onboarding. Goal step: "Milestones" list with Add milestone, like Goals; its skip says "Skip". Account step: Email me a code and Skip stacked, with a line that progress stays on this phone only. Tour card has no shadow. My studio icon is a gallery building.
- 15 Nov: Account shows a pink "Help test Paint a Picture" banner right under the hero, above your name, linking to the Tally form (once `CFG.testFormUrl` is set). The Help row stays too.
- 15 Nov: The Tally testing form (https://tally.so/r/kbe21Z) is live in the app: the Account banner and the Help row open it.
- 15 Nov: iOS build 9 uploaded to TestFlight (places step, starter pieces, milestones, studio hero, testing banner).
- 16 Nov: A privacy policy page (privacy.html on the website), linked as "Privacy policy" under Delete account in Account; its URL is used for TestFlight external testing. Contact goes through TestFlight feedback or the Help test form (no email on the page).
- 16 Nov: Account: your name and email sit inside the character scene, white over a soft shade under your character, and stay in the bar as you scroll; then the testing banner. Privacy policy link just above Sync.
- 16 Nov: Character editing moved out of Account into a Memoji-style sheet: big live preview on top, Pixel art | 2D, tabs (Body, Skin, Hair, Top, Cargos, Boots), one row of choices, Done. Account shows an "Edit character" row; tapping your character in the scene opens it too. "Character: Female/Male" is now "Body".
- 16 Nov: Account (signed in) drops the Sync section and its explanation; Sign out sits just above Delete account at the bottom. Signed out, the Sync sign-in box still shows.
- 16 Nov: Session recording on (PostHog, posthog-js 1.438.21 from jsDelivr), only after a yes and never in Demo Data; all text and inputs are masked on the phone, the map canvas is not recorded. Onboarding asks once, right after the story ("Help make Paint a Picture better": Allow / Not now); the first-open pop-up stays for anyone who never answered. Privacy page updated.
- 16 Nov: Recordings now show the map and character (canvas at 4 fps) and the app's own words; everything she wrote and her photos stay hidden (matched against her saved world). Permission page and privacy page say the map can show place and piece names. Owner's choice over recording "everything".
- 16 Nov: The permission page, the pop-up and the privacy page list plainly what we can never see (name and email, anything typed, pieces, goals, milestones, journal, notes, to-dos, photos) and say "write freely".
- 16 Nov: Reverses the 15 Nov "permission only in onboarding": Account has a "Usage data and recordings" switch card under Edit character, so people can turn it on or off any time (turning off stops recording at once). The pop-up line "You can change this any time in Account" is true again.
- 16 Nov: The story screen is interactive: people tick the six milestones themselves; each tick lights a piece, every three finish a goal, all six bring the picture together (tap again to untick). The first box nudges once the story is told; Get started never waits on it. Places on the sea drag and stay where dropped, like pieces (a place never becomes the first piece).
- 16 Nov: Goal step starts empty: no goal or milestones filled in; the chosen piece's ideas show as "e.g." hints. Place chips on the places step wrap onto more lines again (reverses one-line).
- 16 Nov: Story screen footer: 8px between Get started and "I already have an account", 16px above the home bar.
- 16 Nov: All buttons are rounded rectangles (12px corners), including Get started and the editor's Done; no pill-shaped buttons. Fixed: a brand-new world crashed My studio (missing building list).
- 16 Nov: The places step gets the same drag hint as pieces: the hand slides an island and she says "Drag the islands around for shits & giggles." Shown once for islands and once for pieces.
- 16 Nov: Removed the "Here's your picture" step; after saving (or Skip) onboarding goes straight to building her world, and her picks are saved as that starts. Account step: the warning line, Email me a code and Skip sit at the bottom, 8px apart.
- 16 Nov: The onboarding world-building loader is now a ~3 second moment instead of a checklist: her character in the middle, her own pieces (and first goal) appear around her one by one where she placed them, one line names each ("Placing Mumbai and New Delhi", "Adding a pet"), a thin pink progress line, then "Your world is ready. Light it up, piece by piece." and it grows and fades into Home. Reduce Motion: fades only. The old checklist loader still serves Demo Data switching.
- 16 Nov: My studio is a gallery: square picture tiles (your photo, or matching app art), tap one for a big view (picture, how making it felt, date, folder, tags, words, link) with Edit. Categories became tags (each old category added once as a tag; catId kept), tags filter in one sliding row, folders (new folder icon in the header; covers made from their pictures). Each piece can have a face drawn like a Journal day for how making it felt. Category sections, "Add New Category" and Move up/down are gone. Save step: no Email me a code button; the keyboard Send key sends the code.
- 16 Nov: The "Sign in to save this" sheet puts its buttons together at the bottom right: Not now | Email me a code, then Not now | Sign in.
- 16 Nov: Studio items take up to 6 photos like goals (field right under Name; small copy synced, full quality on the phone). The tile shows the first photo with a count; the big view is a swipeable slideshow with dots, and a tap opens full screen with zoom. An older single picture stays as the first photo.
- 16 Nov: Drawn faces (Journal days and studio items) are drawn as smooth curves with a light averaging; new strokes keep tenths. A studio face badge sits on a light tint of its own colour.
- 16 Nov: Studio detail header: a bigger face (52px, light tint of its colour, no shadow) beside the name, the date under the name; the separate "How making it felt" row is gone. Face badges have no shadow. Photo viewer fetches sharp copies of the photo and its neighbours ahead (no blurry flash on swipe) and keeps sliding photos inside the viewer; the detail slideshow uses sharp copies too.
- 16 Nov: New 2D character look (tank tops, below-knee cargos, heeled sandals / sneakers, Full / 3/4 choice) waits for clean art made to docs/CHARACTER_ART_SPEC.md; the concept sheet is not used as sprites.
- 16 Nov: Added scripts/check_avatar.py to check new 2D character files before they replace avatar/. The Character Art Package is still concept art (no transparency, no masks); live art unchanged.
- 16 Nov: 2D character Length choice in Edit character → Cargos: Full (today's art, the default) or 3/4 (new tank-top art in avatar/34/, cut from the owner's concept sheet with scripts/cut_character_sheet.py; masks made by colour). Test-quality: passes scripts/check_avatar.py; thin dark tank edges and a strip on the male side views don't recolour. Olive added to cargo colours.
- 16 Nov: Onboarding's character step also offers Cargos: Full length / 3/4 (2D only), under "You are".
- 16 Nov: 2D 3/4 now has hairstyles (her: Classic, Long, Bob, Pixie; him: Classic, Curly, Short, Buzz, Long, Shoulder), each its own set in avatar/34/<hair>/ cut from the owner's camo sheets with scripts/cut_character_sheet2.py; a Hair tab in Edit character and a Hair row in onboarding (portrait tiles). Cargo colours add Camo (painted on the new sets, printed on Classic) and Zebra (printed); both only for 2D 3/4. Character pictures now load per set when needed. Full-length cargos and boots wait for the owner's next sheets.
- 16 Nov: Removed the first 3/4 set ("Classic", cut from the earlier sheet with clipped heels). 3/4 uses only the 8 sets from the owner's camo sheets: her Long (default), Bob, Pixie; him Curly (default), Short, Buzz, Long, Shoulder.
- 16 Nov: Full / 3/4 removed for now: 2D is always the new tank-top art (the earlier full-length art returns when its new version arrives). Her Shoulder hairstyle added (4 for her: Long, Shoulder, Bob, Pixie). Onboarding's character step uses the same editor as Account (Pixel art | 2D, tabs, one row of choices; her figure is the preview), and she is drawn a bit bigger there.
- 16 Nov: Character editor (onboarding and Account): Pixel art | 2D and Female | Male sit side by side in one row; the Body tab is gone, tabs start at Skin.
- 16 Nov: Zebra cargo print removed everywhere (anyone who picked it gets Camo). iOS build 10 sent to TestFlight.
- 16 Nov: The 8776 test tab's world had become Demo Data content (from tests that swapped in demo with sync still on) and the account's saved world was empty. Restored from the owner's iPhone (its copy fills an empty account on open). The test tab's demo copy is kept as dreamLife.testBackup.16nov.
- 17 Nov: Every city is open and in full colour on Home; only pieces still to earn are greyed and darkened (soft shade), and earned pieces get a subtle warm glow. The places strip follows the order in Your world. Names: any one of first, middle or last is enough (onboarding and Account); greetings and initials use the first name given and update everywhere when changed.
- 17 Nov: The splash screen shows the 2D girl (Long hair) and boy (Curly) standing together under the star, instead of the walking pixel character.
- 17 Nov: On the splash the girl is drawn 5'5" and the boy 6' (she is 65/72 of his height); after the light opens they take a short walk apart in profile and come back to face you, then the story screen follows (splash ~0.8 s longer). The walk plays with Reduce Motion too, as the pixel walk did.
- 17 Nov: Story screen shows Get started and I already have an account from the start. Sign-in says why a code could not be sent (rate limit, wait, bad address, or the server's message) and offers "I already have a code". iOS build 11 sent to TestFlight.
- 17 Nov: Removed the grey shade over locked pieces (they look as they are); unlocked pieces get a soft pink glow.
- 17 Nov: Double tap on the map (close in on your character) is measured on the screen, not the map, and allows 400 ms: the first tap often moved the camera, so the second landed elsewhere and the double tap was missed.
- 17 Nov: Any screen with two buttons shows them side by side: the main one on the right, the other (Skip, Cancel, Not now, I have an account, Don't share) on the left. Covers onboarding, the story screen, sign-in, restore and consent.
- 17 Nov: Ticking a goal's box from its piece asks first ("Finish this goal?") and lists the milestones that will be ticked off with it.
- 17 Nov: Account shows "Another version of your world is on this device" when the device kept its own world after taking the account's copy; Use this version switches to it (and keeps the one it replaces), Save a copy downloads it.
- 17 Nov: The iPhone app lets the 2D character's pictures be recoloured (they were blocked as "from another site", so only the shadow drew); if recolouring ever fails the plain picture shows instead.
- 17 Nov: The splash plays on every launch, signed in or not, then goes to Home (or back to the introduction step she was on). The story screen has a back arrow to the splash.
- 17 Nov: The second button of a pair is plain text, with no fill or outline (replaces the white outlined button from earlier today).
- 17 Nov: "Where do you live now?" in onboarding suggests only places she has already added; anything else is searched. "Add a place that isn't listed" and the six city ideas are gone from that sheet (the Add place sheet in the app keeps them). "Leave it out" is now "Skip".
- 17 Nov: The onboarding sign-in step: "Skip to home"; the "Without an email…" note sits under the email, left aligned; no "I already have a code" link there.
- 17 Nov: Pieces on the map have no glow. Locked: light pink star with a lock. Unlocked: bright pink star. The same star and lock show in the map card and the Pieces list.
- 17 Nov: A piece or goal she's sent to opens fully in view (centred below the header when it fits). Goals has an "Active" header like "Finished".
- 17 Nov: Log progress is one scrolling page (how much it moved things first) instead of three steps. My studio shows an item's photos as small square tiles instead of a slideshow.
- 17 Nov: A double tap on the map undoes the walk the first tap started, then closes in on her facing you. The 2D figure shows only its own soft shadow.
- 17 Nov: "I already have a code" is removed everywhere (sign-in sheet and onboarding); the code field appears once a code is sent.
- 17 Nov: The back arrow on the story screen is removed again (the splash already plays on every launch).
- 17 Nov: Account has a Reset button to the left of Delete account: after a confirm it empties the world (places, pieces, goals, milestones, journal) on this device and in the account, and starts the introduction again; the account, name and character stay. A copy of the old world is kept on the device (dreamLife.resetBackup). Not shown in Demo Data, which has its own reset.
- 17 Nov: Removed the "Another version of your world is on this device" card from Account (it replaced the owner's newer work). When both sides changed, the account's copy still wins.
- 17 Nov: Each device remembers which account its world belongs to (dreamLife.owner). If a different account signs in on that device, the old world is never uploaded into the new account: it's put aside on the device, and the new account gets its own world (or a fresh start). A world made before signing in still goes into the account it signs in to.
- 20 Nov: 2D wardrobe. The character editor's 2D tabs are Skin, Hair, Top, Bottoms and Shoes, each a row of picture tiles cut from the outfit that has it. Each outfit ("look") is one complete drawing from the owner's sheets (avatar/w/, listed in art/wardrobe.json and WLOOKS in index.html); the earlier 3/4-cargo sets stay as looks too. Picking a tile switches to the look with that item that keeps the most of what's worn; tiles that also need another part to change are shown softer and say so. Colours appear only for plain items (plain tops, white/beige trousers, white shoes); stripes and camo are never recoloured, so the old blotchy "camo in another colour" is gone. Colour choices are kept when switching looks. True mix-and-match waits for layered art drawn on one base body (girl: the medium-hair sheet, boy: the buzz-cut sheet).
- 20 Nov: After the splash, a new page answers "What is Paint a Picture?", "Why?" (Ashima's story, no longer typed out) and "How?", with I have an account | Next. The interactive milestones page after it is now titled "How it works" (back | Get started). The permission page puts its heading and line beside the icon. In the character editor 2D comes first and is the default for a new character (existing characters keep their style).
- 20 Nov: The bald girl base body (art/base/) is the base for layered clothes. The existing outfit sheets were drawn on a different body (wider shoulders, longer torso, bigger head), so their clothes and hair can't be moved onto it; each item needs drawing on the base itself. art/base/README.md says how.
- 20 Nov: On the two intro pages the back button sits left of the heading (the first one goes back to the splash); their footers hold only the main buttons.
- 20 Nov: The first page after the splash follows Apple's Welcome pattern: "Welcome to Paint a Picture", a picture of a little world, then three rows (icon, bold claim, one grey line): Your goals, as a world · Made for real life · Tick, finish, light up. Ashima's full story sits behind "Why I made this". Rows fade in one after another (a plain fade with Reduce Motion).
- 20 Nov: Back arrows have no background anywhere.
- 20 Nov: One top line for every page: the first row starts 8px below the status bar (20px minimum on the web), 44px tall, centred.
- 20 Nov: On the splash the girl and boy start at random spots each launch (her on the left, him on the right), wander via a random point and meet under the star, facing the way they walk (side, back or front); they end facing you.
- 20 Nov: The sign-in sheet is titled "Sign in with email", with just the email box (no line about codes, no Email label) and Cancel | Send code. The button reads "Send code" wherever the sign-in form appears.
- 20 Nov: After a code is sent, the sentence naming the email ends with an "Edit" text button that goes back to the email step with the address filled in.
- 20 Nov: The tab bar shows icons only; the selected tab grows into a soft pink pill with its name to the right of the icon (it slides open; with Reduce Motion the name fades in). The places strip on Home has the same frosted background as the tab bar.
- 20 Nov: Splash walk: each character walks to the star in straight lines with turns (across, then up or down, a random route each launch) at an even pace, with a small step lift and sway, instead of gliding diagonally.
- 20 Nov: Your pieces has a back arrow left of its title (back to the picture), and no tab is selected while it's open.
- 20 Nov: Add places picks several at once: each picked place joins a list under the search with its own status dropdown (Travel by default, Study for universities) and a remove button; the single Status block is gone; "Add N places" adds them all.
- 20 Nov: The places strip on Home spreads its places across the full width, however many there are; it scrolls only when they no longer fit.
- 21 Nov: Bigger islands. Each place's cell grew from 400 × 560 to 720 × 960; the city's own drawing sits in the middle and new outskirts in the city's style fill the land around it. Columns and rows with no place are narrower stretches of sea. Each island keeps its own picture instead of one world-sized canvas, so the world can grow past what an iPhone draws.
- 21 Nov: She never walks on water. Crossing the sea she's in a little red-and-white rowing boat (gently rocking, a wake behind her); a tap on the sea walks her to the nearest shore, where she still says one of the sea lines (not the drowning one).
- 21 Nov: LA has its own pieces: Craftsman bungalows and glass villas with pools mixed in with the Spanish houses on every street, its streets run on to the new shore, Mulholland with villas along the hills, the coast road and beach houses on stilts past the city. Tokyo, Boston and the rest get their own sets next.
- 21 Nov: Tokyo has its own pieces around the city: shop streets of narrow two- and three-floor shops with hanging signs and awnings (now and then a big screen), a canal lined with cherry trees, a main street with a scramble crossing where people cross every way at once, a temple hall with its lantern gate and a pagoda, and the bullet-train line carried on to both shores. The same set dresses any place drawn in the Japan style.
- 21 Nov: On land she walks the streets: a tap sends her along the roads and paths the shortest way, stepping off only for the first and last few steps. Where there's no road nearby she still walks straight; across the sea she takes the boat.
