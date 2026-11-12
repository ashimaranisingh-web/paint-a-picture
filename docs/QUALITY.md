# Quality checklist

Run through this before calling anything done, and before every push. Copy it into the reply when the change is big.

## 1. Does it do what was asked, and only that?
- [ ] Every part of the request is handled. Anything skipped is named in the reply.
- [ ] Nothing else changed: no removed features, categories, options or copy. `git diff` reviewed line by line.
- [ ] Decisions in [DECISIONS.md](DECISIONS.md) still hold.

## 2. Does it work?
- [ ] Script passes `node --check` (command in [CLAUDE.md](../CLAUDE.md)).
- [ ] Opened in a separate tab (port 8776) at 390×844, no console errors.
- [ ] Tried on a **fresh profile** (cleared storage, full onboarding) and an **existing profile** (data still there).
- [ ] Tried as a **guest** and **signed in** if the change touches saving, sync or creating things.
- [ ] Demo Data untouched, and the change behaves in Demo mode.
- [ ] Reduce Motion on: still usable, no stuck animation.
- [ ] Screenshot shared.

## 3. Is the data safe?
- [ ] Old saves still load (`normalize()` handles missing fields).
- [ ] No cross-over between Demo Data and the person's world.
- [ ] No secret key, personal API key, name, email or journal text sent anywhere new.

## 4. No AI slop
Slop is work that looks finished but wasn't thought about. Reject any of these:
- **Copy:** filler ("Embark on your journey", "Unlock your potential", "Seamlessly"), the word "dream", exclamation
  marks, emoji, three-adjective lists, explaining the same idea twice.
- **Design:** generic purple/blue gradients, random new colours, more than one pink button, heavy shadows, centred body
  text, Lorem ipsum, placeholder icons left in, inconsistent corner sizes.
- **Content:** made-up places or vibes on the map, fake stats, invented features in replies or docs.
- **Code:** dead code left behind, duplicate functions doing the same job, commented-out blocks, `console.log` left in,
  "TODO" with no owner, catching errors and hiding them.
- **Replies:** claiming it works without having tried it, long recaps of what was said, jargon without a meaning.

## 5. Accessibility basics
- [ ] Buttons have labels (`aria-label` on icon buttons), tap targets at least 44px.
- [ ] Text contrast readable on its background (watch white text on pink, grey on paper).
- [ ] Pop-ups and sheets close with Escape and focus their first button.
