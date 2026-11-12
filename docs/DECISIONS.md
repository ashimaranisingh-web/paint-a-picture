# Decisions

Product decisions and why. Newest first. Don't reverse one without the owner saying so, and when they do, add a new
line rather than editing the old one.

## 2026-11
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
