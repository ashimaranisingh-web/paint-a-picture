# User testing

## The call (post this to recruit)

> **Help test Paint a Picture (about 10 minutes).** One task: picture one thing you want in the next few years, then
> turn it into a goal with one first step. Afterwards, tell me where you got stuck. iPhone, via TestFlight.

The fitness app gets its own, separate call ("Which part of your current routine should it help with?").

## The Tally form

Build it at tally.so (free). In a new form, type each line below. Tally turns `/` commands into blocks; the block type
is in brackets. Mark only 1, 3, 4 and 9 as required.

**Title:** Help test Paint a Picture
**Intro text:** About 10 minutes. There are no wrong answers: if something confused you, that's the app's fault, not
yours.

### Before you start
1. How do you keep track of goals today? [Multiple choice: Notes app / A planner or notebook / A habit or goal app / In my
   head / I don't]
2. What usually makes you drop a goal? [Long answer]

### What Paint a Picture is
[Heading 2, then text blocks]
Paint a Picture is a goal journal set inside a small pixel world built from your own places. You picture the life you
want, and the world comes to life as you work towards it.
- Place: a real city or spot that matters to you, where you live, have lived or want to be.
- Piece: one part of the life you want, like "a home by the sea". Together your pieces make your picture.
- Goal: something you'll do to bring a piece to life, like "save for a deposit".
- Milestone: one small step inside a goal. Tick it off when it's done.
- Asset: something you've made or built along the way, kept in My stuff.

### The task
[Text blocks, one per line]
1. Open Paint a Picture.
2. Add a place you'd love to live.
3. Make one piece for it.
4. Give that piece a goal with one milestone.
5. Fill in today in Journal.
6. Note roughly how long it all took.

### After the task
3. Did you finish? [Multiple choice: Yes / Partly / No]
4. Roughly how long did it take? [Multiple choice: Under 5 minutes / 5–10 minutes / 10–20 minutes / I gave up]
5. Where did you hesitate or get stuck? What did you expect to happen? [Long answer]
6. In your own words, what is a "piece"? [Short answer]
7. What did you think of the map when you first saw it? One word is fine. [Short answer]
8. Journal: drawing a face felt… [Multiple choice: Fun / Silly / A chore / Didn't try it]
9. How easy was it overall? [Linear scale 1–5: 1 = Very hard, 5 = Very easy]
10. Would you open this again next week? Why? [Multiple choice: Yes / Maybe / No, then a Short answer "Why?"]
11. One thing you'd change or remove. [Long answer]
12. Happy to do a 15-minute follow-up call? Leave your first name and email. (Optional) [Short answer + Email]

**Thank-you page:** Thank you. This helps more than you'd think.

### Events 2 and 3, and the look and feel (added 15 Nov; the form in Tally is the source of truth)
The form now runs as three events, each with its own short steps and questions:
- **Event 1: setting up the place, piece and goal** (steps and "After the task" questions above, as edited in Tally).
- **Event 2: Writing in Journal.** Steps: go to Journal, double-tap today's dot, pick a colour and draw a face, write a
  line or two and save. Questions: drawing a face felt… (Fun / Silly / A chore / Didn't try it); Was it clear how to
  fill in today? (Yes, straight away / After a bit / No); What, if anything, was confusing in Journal?
- **Event 3: Logging this week's progress.** Steps: go to This week, tap "Log progress" and log one thing, look over the
  week's faces and "Done this week". Questions: Did logging your progress make sense? (Yes / Partly / No / I couldn't
  find it); Did seeing your week laid out make you want to keep going? (Yes / A little / Not really); What would make you
  log your progress every week?
- **The look and feel.** How do you feel about the 2D pixel-art world? (Love it / It's fine / Not for me); Did unlocking
  pieces and watching your world come to life feel like a game? (Yes, in a good way / A little / No, I didn't notice it /
  It felt like a distraction); Which parts felt fun? Pick any (map and walking around, unlocking pieces, drawing faces,
  your character, none); Did anything feel too childish or get in the way?
- Then the overall questions (ease 1–5, how often, favourite feature, one change, follow-up contact).
Required: only "How do you keep track of goals today?", "Did you finish?", "Roughly how long did it take?" and "How
easy was it overall?".

## After publishing
Published 15 Nov: https://tally.so/r/kbe21Z (set in `CFG.testFormUrl`).
Copy the form's share link (tally.so/r/…) into `CFG.testFormUrl` in `index.html`. The "Help test Paint a Picture" row
in Account → Help appears once it's set, and opens the form (in Safari on iPhone).

## Reading the answers
Questions 5 and 6 matter most: they show whether "pieces", "picture" and the map make sense without explanation. If
testers describe a piece in different ways, the word needs work.
