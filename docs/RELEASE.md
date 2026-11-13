# Releasing

Always ask the owner before each of these.

## Website (GitHub Pages)
1. Quality checklist done ([QUALITY.md](QUALITY.md)).
2. Commit on `world-expansion`, push (command in [CLAUDE.md](../CLAUDE.md)).
3. When the owner says "push to main": push `world-expansion:main` with the same command.
4. Wait ~1 minute, open https://ashimaranisingh-web.github.io/paint-a-picture/ and confirm the change is live.

## TestFlight (iOS)
1. Web change pushed and checked first; the app loads the same `index.html`.
2. Raise the build number: `CURRENT_PROJECT_VERSION` in `ios/project.yml` (one higher than the last upload).
3. Regenerate the project: `cd ios && xcodegen`.
4. Archive:
   ```bash
   xcodebuild -project ios/PaintAPicture.xcodeproj -scheme PaintAPicture -configuration Release -archivePath /tmp/PAP.xcarchive archive -allowProvisioningUpdates
   ```
5. Upload, with an `export.plist` (method `app-store-connect`, destination `upload`, teamID `M8USK73B4P`, automatic signing):
   ```bash
   xcodebuild -exportArchive -archivePath /tmp/PAP.xcarchive -exportOptionsPlist export.plist -exportPath /tmp/PAPexport -allowProvisioningUpdates
   ```
6. "Upload succeeded" means App Store Connect has it; it shows in TestFlight after processing (10–30 min).
7. Commit the build-number bump and note it in [DECISIONS.md](DECISIONS.md) if it shipped something notable.

Build history: 3, 4, 5 uploaded (5 on 13 Nov 2026: Gallery palette, pixel pieces, rebuilt onboarding). Next is 6.

## Supabase (accounts and sync)
- Project URL and publishable key live in `CFG` in `index.html`. Schema: `supabase/schema.sql`. Setup notes:
  `supabase/README.md`.
- Table changes: write them in `schema.sql` first, run them in the SQL editor, keep RLS ("own row only") on.
- `delete-account` function: edit `supabase/functions/delete-account/index.ts`, paste into the dashboard function
  editor (the file must be `index.ts`), deploy, then test with a throwaway `+test` email. "Verify JWT with legacy
  secret" stays off.
- Email sign-in uses Gmail SMTP and 6-digit codes (10-minute expiry). Move to a proper sender (e.g. Resend) once
  there's a domain.

## PostHog (usage counts)
- EU Cloud, host `https://eu.i.posthog.com`, project token in `CFG`. Nothing is sent without the person's "Yes".
- New events: add a `track("name")` call, list it in `supabase/README.md`, never include personal text.

## Before the App Store
- Privacy policy page (what's stored, where, how to delete).
- App Store privacy answers match: email (account), usage counts (optional, anonymous), no tracking.
- In-app account deletion works (it does: Account → Delete account).
