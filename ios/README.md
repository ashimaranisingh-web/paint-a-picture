# Paint a Picture for iPhone

A small native app that shows the web app full screen. `../index.html` and `../avatar/` are bundled inside it
(with the fonts in `Fonts/`), served from the `paintapicture://` address, so it works offline and what's saved
on the phone stays put across updates. Data stays on the phone; nothing syncs yet.

- Bundle ID: `com.ashimasingh.paintapicture` · Team: Ashima Singh (`M8USK73B4P`) · iPhone only, portrait, iOS 16+
- Change `project.yml`, then run `xcodegen` here to regenerate `PaintAPicture.xcodeproj`. Web changes need no
  project change: the next build picks up the current `index.html`.
- For each new TestFlight build, raise `CURRENT_PROJECT_VERSION` in `project.yml` (1, 2, 3…).

## Getting it onto TestFlight

1. Install Xcode from the Mac App Store, open it once (accept the licence, let it add iOS), then in Terminal:
   `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer`
2. Xcode → Settings → Accounts → **+** → Apple ID → sign in with the developer account.
3. In App Store Connect (appstoreconnect.apple.com) → Apps → **+** → New App: iOS, name **Paint a Picture**
   (if it's taken, try "Paint a Picture: Dream Life"), bundle ID `com.ashimasingh.paintapicture`, SKU `paintapicture`.
   If the bundle ID isn't in the list yet, build once in Xcode with automatic signing and it will appear.
4. Open `ios/PaintAPicture.xcodeproj`, choose **Any iOS Device (arm64)**, then Product → **Archive**.
5. In the Organizer: **Distribute App** → **App Store Connect** → **Upload**. Processing takes 5–15 minutes.
6. App Store Connect → the app → **TestFlight** → Internal Testing → add yourself. Install the **TestFlight**
   app on your iPhone and accept the invite. Internal testing needs no review; external testers need a short
   Beta App Review first.
