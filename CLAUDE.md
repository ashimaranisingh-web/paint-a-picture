# Paint a Picture: working rules

Claude Code reads this file at the start of every session in this folder. These rules come from the owner. They override
any default habit. If a rule here conflicts with a request in chat, follow the chat and suggest updating this file.

Related docs: [docs/DESIGN.md](docs/DESIGN.md) (look and voice), [docs/QUALITY.md](docs/QUALITY.md) (checks before
shipping), [docs/RELEASE.md](docs/RELEASE.md) (web, TestFlight, Supabase, PostHog), [docs/DECISIONS.md](docs/DECISIONS.md)
(what was decided and why: don't undo these quietly).

## What this is
- A goal journal inside a pixel-art world, built from the person's own places. One file: `index.html` (HTML, CSS, plain
  JavaScript, no build step). `ios/` wraps it in a WKWebView app. `supabase/` holds the database schema and the
  `delete-account` Edge Function.
- Live site: https://ashimaranisingh-web.github.io/paint-a-picture/ (GitHub Pages from `main`).
- Work happens on `world-expansion`; `main` is fast-forwarded to it when the owner says "push to main".

## The rules
1. **Only change what was asked.** Never remove features, categories, options or copy that the request didn't name.
   If something nearby looks wrong, mention it; don't fix it unasked.
2. **Never lose user data.** Preserve everything in `localStorage` (`dreamLifeBuilder.v1`) and in Supabase. Demo Data
   (`dreamLifeBuilder.demo.v1`) and the person's own world stay separate: never copy, merge or delete across them.
   Schema changes go through `normalize()` so old saves still load.
3. **Keep all ten city categories.** Never use the word "dream" in visible copy (it's fine in old storage keys).
4. **Real places only.** Anything on the map must be a real, mappable place (a city, island, region or landmark),
   never a vibe like "By the sea" or "A small town".
5. **Ask before:** a TestFlight build, pushing to `main`, anything sent to an outside service, deleting anything.
6. **Secrets never go in the app or in chat.** Only the Supabase *publishable* key and the PostHog *project* token
   (`phc_…`) belong in `index.html`. The Supabase secret / service_role key and any PostHog personal API key stay in
   their dashboards.
7. **Check it in the browser before saying it works.** Use a separate tab (port 8776), never the owner's preview tab
   (8771). Phone width (390×844), a fresh profile *and* an existing one. Look at the console. Then share a screenshot.
8. **Say what's verified and what isn't.** If something couldn't be tested (an email, the iPhone, App Store review),
   say so plainly.
9. **Plain, short replies.** Explain in everyday words; the owner is a designer, not an engineer. No jargon without a
   one-line meaning.

## Code habits that prevent known breakages
- **No `//` comments inserted in the middle of a line.** It has broken the script three times. Use `/* … */` or put the
  comment at the end of the line.
- **Check syntax with Node, not `new Function`:**
  ```bash
  python3 -c "import re;s=open('index.html').read();open('/tmp/pap.js','w').write('\n'.join(re.findall(r'<script>(.*?)</script>',s,re.S)))" && node --check /tmp/pap.js
  ```
- Watch template literals: a stray backtick inside `` `…` `` ends the string.
- No top-level `const` that reads another `const` declared further down (the `LD_V` startup crash). Make it lazy.
- State changes go through `commit(fn)` so they save, sync and count usage. Don't write `S` and call `save()` by hand.
- New "create" actions for guests go behind `needAccount(then)`. Places and pieces stay open to guests.
- Anything `position:sticky` inside the page scroller needs `top:calc(-1 * var(--safe-top))` and that much extra top padding, or content shows through the notch strip above it (seen in the desktop frame and on iPhone).
- On the map canvas, set `globalCompositeOperation` right before every `drawImage`. A mode left on from an earlier layer ("screen" from the streetlight glow) turned the evening sea white.
- The 8776 test tab is signed in to the owner's account, so test edits sync to her real world. Snapshot before testing and undo every change after.
- Anything that applies a synced world must not change the screen you're on unless the incoming data truly calls for it (a blanket "onboarding done → go Home" kept throwing people out of a replayed introduction).
- The owner's Mac has Reduce Motion on: a gentle version of an animation (fade, small scale) should still play, or she never sees it.
- Respect Reduce Motion (`prefers-reduced-motion`) for every new animation.
- Usage events: add to `track()` calls only with the consent check already inside it; never send names, emails, goal
  text or journal text. Demo mode is never tracked.

## Pushing
Commits and pushes use the owner's GitHub account `ashimaranisingh-web`:
```bash
T=$(gh auth token --user ashimaranisingh-web); H="AUTHORIZATION: basic $(printf 'x-access-token:%s' "$T" | base64)"; git -c credential.helper= -c http.https://github.com/.extraheader="$H" push
```
For `main`: `git push origin world-expansion:main` with the same header, only after the owner asks.

## Keeping these docs alive
- When the owner makes a product decision or reverses one, add a line to `docs/DECISIONS.md` in the same commit.
- When a new visual rule appears ("pink only for…", "corners never more than…"), add it to `docs/DESIGN.md`.
- When a bug teaches a lesson, add it to "Code habits" above.
- Session recordings keep `maskAllInputs: true`, `maskTextSelector: "*"` with `maskTextFn: phMaskText` and `maskAttributeFn: phMaskAttr`: anything she wrote (found by `phPrivate()` from her saved world) and her photos stay hidden; app words, the map and her character show (owner's choice, 16 Nov). When adding a new kind of user text to the saved world, check `phPrivate()` still picks it up. Never loosen these.
- A brand-new world must come out of `normalize()` (migrate does `normalize(blankState())`). A field added only in normalize crashed My studio for first-time users (`S.building` missing).
- Never swap `S` for Demo Data (or any test world) in a tab that is signed in, even with `save` stubbed: sync (`syncWithAccount` on visibilitychange, `use()`, `upload()`) writes `S` to localStorage and Supabase on its own. Test demo content in Demo Data mode or a signed-out profile only. (16 Nov: the 8776 tab ended up holding demo content.)
- Gestures on the map: compare taps in screen coordinates. The first tap of a double tap can move the camera (a walk, a piece opening), so map coordinates drift between taps.
- The owner uses the test tabs too, so `127.0.0.1:8776` and `localhost:8776` may be signed in to her account at any time. Check `supaUser` first; for anything that changes data, use an address she hasn't used, such as `http://test.localhost:8776` (each address keeps its own storage, so it starts signed out and fresh).
- One account's world must never reach another account. Sync checks `worldOwner()` before uploading anything; keep that check in front of any new upload path. Server side, `worlds` is one row per user with "own row only" rules.
