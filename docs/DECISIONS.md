# Decisions

Product decisions and why. Newest first. Don't reverse one without the owner saying so, and when they do, add a new
line rather than editing the old one.

## 2026-11
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
