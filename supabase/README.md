# Accounts, sync and usage

Both are built into `index.html` and stay off until their keys are filled in at the top of the
**ACCOUNTS AND USAGE** section (search for `const CFG`).

## Accounts and sync (Supabase)

1. Create a project at supabase.com (pick a region near your users).
2. **SQL Editor → New query**: paste `schema.sql` from this folder and run it. Each person can only read and
   write their own world; the rules are in the database, not the app.
3. **Authentication → Sign In / Providers → Email**: keep Email on.
4. **Authentication → Emails → Magic Link** template: make sure the email shows the code, e.g.
   `Your Paint a Picture code is {{ .Token }}`. People type that code into the app; there's no link to open,
   which is what makes sign-in work inside the iPhone app.
5. **Project Settings → API**: copy the **Project URL** into `supabaseUrl` and the **anon public** key into
   `supabaseAnonKey`. The anon key is meant to be public; the table's row rules are what protect the data.

Signing in on a device that already has a world: if one side is empty, the other one is used. If both have
something, the app asks which to keep, and saves the other as a file first (and in this browser), so nothing
is lost. Demo Data is never synced.

## Usage (PostHog)

1. Create a project at posthog.com (EU hosting matches `posthogHost`; for US, change it to
   `https://us.i.posthog.com`).
2. **Project settings**: copy the **Project API key** (starts with `phc_`) into `posthogKey`.

The first time the app opens, it asks once. Only people who say yes are counted, and they can change it on
the Account page. Events never include names, place names, goals, notes or anything typed:

| Event | When |
|---|---|
| `app_opened` | the app starts |
| `onboarding_step` | each onboarding step (step name) |
| `place_added` | a place is picked (suggested or search, scenery type) |
| `piece_picked` | a library piece is picked (its id) |
| `first_piece_set` | a piece is dropped on the character |
| `onboarding_completed` | counts of places and pieces, whether a goal and journal line were set |
| `goal_created` | a goal is added |
| `milestone_ticked` | a milestone is ticked |
| `piece_unlocked` | a piece unlocks |
| `journal_entry_saved` | a note, weekly entry or good thing is saved |
| `account_signed_in` | someone signs in |

Remember to update the App Store privacy details for the iPhone app once these are switched on.

## Account deletion (Edge Function)

Apple requires apps that offer sign-up to let people delete their account in the app. **Account → Delete account**
calls the `delete-account` function, which deletes the person's saved world and their sign-in. It only ever deletes
the caller: it works out who they are from their own sign-in token.

Deploy it once, from the dashboard: **Edge Functions → Deploy a new function → Via Editor**, name it
`delete-account`, paste `functions/delete-account/index.ts`, and click **Deploy function**. Keep **Verify JWT** on.
(Or with the Supabase CLI: `supabase functions deploy delete-account`.)

## How sync decides

The device remembers the last moment it and the account agreed (when the account copy was saved, and a fingerprint of
the world then). When the app opens, or comes back to the front, it compares both sides with that moment: only the
device changed → upload; only the account changed → download; nothing changed → carry on; both changed → ask. Edits
made offline upload the next time it can reach the account.
