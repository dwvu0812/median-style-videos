# Video 04 — "Why 23 People Is Enough" (birthday paradox)

- Channel: The Maths Inside (@themathsinside). Video 04 in the series.
- Format: Median-style black-board animation, English long-form, 1.0x (NO speedup).
- Voice: Muse TTS voice B Quivering Oak (avocado_v2:vd2_quivering_oak), speed 80.
- Core idea in one sentence: 23 people are enough for a better-than-even chance of a
  shared birthday, because the real count is not 23 people but 253 pairs.
- Target: 38 lines, ~1,090 words, ~9.5 min.

## Verified numbers (computed 2026-11-27, 365-day year unless stated)

| n people | P(shared birthday) | pairs C(n,2) |
|---|---|---|
| 10 | 11.69% | 45 |
| 15 | 25.29% | 105 |
| 20 | 41.14% | 190 |
| 22 | 47.57% | 231 |
| **23** | **50.73%** | **253** |
| 24 | 53.83% | 276 |
| 30 | 70.63% | 435 |
| 40 | 89.12% | 780 |
| 50 | 97.04% | 1225 |
| 57 | 99.01% | 1596 |
| 70 | 99.92% | 2415 |
| 100 | 99.99997% | 4950 |

- No-match chance at 23 people: 49.27% (so match = 50.73%). Chain: 365/365 × 364/365 ×
  363/365 × … × 343/365 (23rd person avoids 22 days: 343/365).
- Someone sharing YOUR birthday needs 253 OTHER people (254 including you) for 50%:
  1 − (364/365)^253 = 50.05%. Coincidence used in the script: 253 pairs = 253 others.
- With 366 days (leap year): P(23) = 50.63% — barely moves.
- 366 people = 100% guaranteed (pigeonhole: only 365 days).
- Expected matching pairs at 23 people is only 0.69 — NOT used in the script (too subtle);
  the script uses the no-match chain instead.
- Uneven birthdays (more births in some months) only INCREASE the chance — 50.7% is the
  cautious number.
- 1 µs-style phrasing rule from video 03 applies: write numbers as words for TTS
  ("fifty point seven percent", "two hundred and fifty-three").

## Chapters (timestamps filled in after the mix is measured)

1. Hook — the claim (lines 1–3)
2. Part 1 — The wrong question (lines 4–7)
3. Part 2 — Count the pairs (lines 8–12)
4. Part 3 — The maths (lines 13–19)
5. Part 4 — The curve (lines 20–25)
6. Part 5 — Why your brain says no (lines 26–30)
7. Part 6 — Try it yourself (lines 31–36)
8. Recap (lines 37–38)

## Script (spoken lines — TTS text exactly as in rag-video-04-audio/lines.txt)

1. Twenty-three people. One room. And a better-than-even chance that two of them share a birthday. That sounds wrong. It is not.
2. Here is the claim, exactly. Put twenty-three strangers in a room, and the chance that two of them were born on the same day is fifty point seven percent. Better than a coin flip.
3. Your brain says no. Twenty-three people, three hundred and sixty-five days — how could a match be likely? Ask a room of twenty-three people, and most of them will say no. Ask a mathematician, and they will take your money.
4. First, the question your brain is actually answering. It is not the question I asked. Your brain hears: what are the chances that someone here shares MY birthday?
5. That is a different question — and a much harder one. For someone to match YOUR birthday, you would need about two hundred and fifty-three OTHER people in the room with you. More than ten times as many.
6. Why? Because there is only one of you. Every new person gets one chance to match your day — one out of three hundred and sixty-five. It adds up slowly. Two hundred and fifty-three other people, all hoping to match one single day.
7. But the real question is not about you at all. It is about ANY two people matching EACH OTHER. And that changes everything.
8. So forget birthdays for a second, and count pairs. You, and the person next to you — that is one pair. You, and the person by the window — that is another.
9. Every person can pair with every other person. With twenty-three people, that is twenty-three times twenty-two, divided by two. Two hundred and fifty-three pairs.
10. Two hundred and fifty-three chances for a match — not twenty-three. Your brain counted the people. The maths counts the pairs.
11. And here is a coincidence worth noticing. Two hundred and fifty-three is also the number of OTHER people you would need for someone to match YOUR birthday. Same number, two different questions.
12. And each pair is a small chance. One pair matching is unlikely — one in three hundred and sixty-five. But you do not have one pair. You have two hundred and fifty-three.
13. So how do we turn two hundred and fifty-three chances into one number? We ask the opposite question. What is the chance that NO pair matches at all?
14. Take the first person. Any birthday is fine — three hundred and sixty-five out of three hundred and sixty-five. The second person must avoid that one day: three hundred and sixty-four out of three hundred and sixty-five.
15. The third person must avoid two days now: three hundred and sixty-three out of three hundred and sixty-five. Each new person has one fewer safe day.
16. Write it out and it looks like this: three sixty-four over three sixty-five, times three sixty-three over three sixty-five, times three sixty-two over three sixty-five — twenty-three fractions, each one a little smaller than the last.
17. Multiply them all together — all twenty-three people — and the chance that nobody shares a birthday is forty-nine point three percent. Less than half.
18. So flip it. If there is a forty-nine point three percent chance of NO match, then there is a fifty point seven percent chance of at least one match. That is the whole paradox.
19. And it is not a trick of rounding. Add one more person — twenty-four — and the chance jumps to fifty-three point eight percent. The tipping point is exactly twenty-three.
20. That crossing is the whole story. Below twenty-three, a match is the underdog. Above it, a match is the favourite. One chair filled, and the favourite changes sides.
21. Watch what happens as the room fills up. Ten people: eleven point seven percent. Barely a chance. Fifteen people: twenty-five point three percent.
22. Twenty people: forty-one point one percent. Twenty-two people: forty-seven point six percent. Almost there — and still under half. Twenty-three people: fifty point seven percent. The line crosses fifty. One person walked in, and the odds flipped.
23. Thirty people: seventy point six percent. Forty people: eighty-nine point one percent. Fifty people: ninety-seven percent. The curve does not climb — it rockets.
24. Seventy people: ninety-nine point nine percent. At that point, betting against a shared birthday is like betting against the sun coming up.
25. Notice the shape: it starts flat, then bends, then flattens again near a hundred percent. The action is all in the middle — between fifteen and forty people.
26. So why does it feel impossible? Because your brain counts the wrong thing. It counts twenty-three people, and twenty-three feels small next to three hundred and sixty-five.
27. But pairs grow fast. Double the people, and the pairs roughly quadruple. Ten people make forty-five pairs. Twenty people make a hundred and ninety. Thirty people make four hundred and thirty-five.
28. Think of it like handshakes. In a room of twenty-three, there are two hundred and fifty-three handshakes. You counted the hands. The maths counts the handshakes.
29. That is the real shape of the problem — it is not a line, it is a curve that bends upward. Your intuition is linear. The pairs are not.
30. And one more honest check. Birthdays are not perfectly even — more babies are born in some months than others. That only makes matches MORE likely, not less. The fifty point seven percent is the cautious number.
31. So try it. A classroom of thirty: seventy point six percent. If your teacher bets there is a match, take the other side only if you like losing money.
32. A football team with the subs — twenty-three players, exactly the magic number. A party of fifty: ninety-seven percent. At a wedding of a hundred people, it is ninety-nine point nine nine nine nine seven percent. Basically certain.
33. And here is the ceiling. With three hundred and sixty-six people, a match is guaranteed — there are only three hundred and sixty-five days. That is not probability any more. That is the pigeonhole principle. Even leap years barely move it: with three hundred and sixty-six days, twenty-three people still give you fifty point six percent.
34. The trick works anywhere people gather. A lecture hall, a wedding, a football stadium — the bigger the crowd, the more certain the match. At seventy people, you can bet your lunch money on it.
35. This is not just a party trick. The same maths sits behind computer security — why two different files can end up with the same fingerprint, and why systems have to plan for collisions. Pairs grow faster than people, everywhere.
36. So the paradox is not that birthdays are magic. It is that pairs grow faster than people — and your brain was never built to feel that.
37. One more time, the whole thing in three numbers. Twenty-three people. Two hundred and fifty-three pairs. Fifty point seven percent. Not twenty-three chances — two hundred and fifty-three. Not your birthday — any two birthdays.
38. That is the birthday paradox. And the next time your gut says impossible, count the pairs. The maths is usually ahead of your gut — by about two hundred and thirty chances.

## Storyboard — one scene per line (800×450 stage, wordmark "birthday — 04" bottom-right)

Style notes (SKILL.md §2d): solid fills (#212120 main, #464845 bars, #3A3F45 top face /
#22262B side), 2-value face shading, dimension lines + ticks + labels, ≥8 drawn
elements/scene, accents as solid fills (periwinkle = the count/pairs, mint = the
answer), no gradients/glow, moving elements never cross text, hook visual in first 3s.

- S1 HOOK: eyebrow "WHY 23 PEOPLE IS ENOUGH". Giant serif "23" (120px) centre-left,
  ring of 23 small dots around it (one mint dot pulsing); mint "50.7%" (64px) right.
  f1: "23" arrives; f2: dots pop one by one (staggered, small); f3: "50.7%".
  SFX: whoosh + pop.
- S2: two-column: left panel "23 strangers" (23 dots in rows), right panel "50.7%"
  big mint + "share a birthday" below; a coin (circle, two faces grey/white) spinning
  slowly between them. f1 left, f2 coin, f3 right.
- S3: two boxes: left grey "most people say NO", right mint "the maths says YES"
  (mint = answer). Small person-dot row under each. f1 left, f2 right.
- S4: one filled person-dot centre ("YOU", mint ring), calendar grid 5×7 dots around
  it (365 = one highlighted day); label "MY birthday". f1 person, f2 calendar, f3 label.
- S5: crowd — grid of dots (16×16 = 256, three dimmed to read 253) + big "253
  people" + "1 in 365 each" caption. Density scene; dots solid #464845, you-dot mint.
- S6: one person-dot + one arrow to a calendar day: "1 person = 1 chance" bar
  (short grey bar) + "1 out of 365" label; dimension line under the bar.
- S7: group of 8 dots, TWO highlighted mint with a connecting line between them;
  label "ANY two" big; the rest grey. f1 group, f2 the two + line (draw), f3 label.
- S8: two dots + one line (1 pair), then a fan of lines to 4 more dots (pairs
  growing); counter "1 pair… 2 pairs…" — keep simple: 2 dots, then 5 dots with
  lines between every pair (10 lines, thin grey), label "count the pairs".
- S9 PEAK (worked calc, two-column): left: "23 × 22 ÷ 2" serif 64px; right: boxed
  result "253" mint 72px in a rect stroke; below: "23 × 22 = 506, ÷ 2 = 253"
  small grey. f1 formula arrives, f2 box, f3 sub-calc.
- S10 comparison pair: two horizontal bars — "23 people" short grey bar vs
  "253 pairs" long mint bar (11×, scale break mark); labels with dimension ticks.
- S11 two cards side by side, both headed "253": left "people to match YOUR
  birthday", right "pairs in a room of 23". Same number, two questions.
- S12: one pair (2 dots + line) with "1 in 365" chip; then "× 253" big mint
  appears right; small caption "one pair is unlikely — 253 pairs are not".
- S13: big "NO match?" serif 56px centre; a match-pair crossed out (two dots +
  line, red? NO — use grey X, no new colours); caption "ask the opposite question".
- S14: two fraction cards: "365/365" then "364/365", second card periwinkle
  border; a small person-dot above each card; arrow between them.
- S15: three fraction cards in a row "365/365 × 364/365 × 363/365"; third card
  arrives; caption "one fewer safe day each time".
- S16 PEAK (worked calc): horizontal chain "364/365 × 363/365 × 362/365 × … ×
  343/365" (first three + ellipsis + last, all serif 28px, drawn left→right);
  "23 fractions" label below with dimension line.
- S17: big grey "49.3%" (72px) + "nobody shares a birthday" + a row of 23 dots
  all grey (no match); caption "less than half".
- S18: worked flip "100% − 49.3% = 50.7%" serif 48px, "50.7%" mint boxed;
  caption "that is the whole paradox". SFX: chime.
- S19: the tipping point — a horizontal 50% threshold line with ticks; two dots
  above it: "23 → 50.7%" and "24 → 53.8%" (mint, the second slightly higher);
  caption "the tipping point is exactly twenty-three". f1: line, f2: 23 dot, f3: 24 dot.
- S20: underdog vs favourite — a balance beam (sway): left pan grey "below 23 —
  a match is the underdog", right pan mint "above 23 — a match is the favourite";
  one extra dot drops onto the right pan and it tips. f1 beam, f2 left, f3 right tips.
- S21: bar chart, two bars: "10 people — 11.7%" short, "15 people — 25.3%"
  taller; y-axis 0–50% with ticks; bars grow (grow class).
- S22: the crossing — a line chart (draw animation) rising through the 50% line;
  dots at 20 (41.1%), 22 (47.6%), 23 (50.7% mint, above the line); "one person
  walked in" label with arrow at the 22→23 step.
- S23: three bars 30/40/50 (70.6% / 89.1% / 97%) rising steeply, mint tops;
  caption "the curve does not climb — it rockets".
- S24: near-full bar "70 people — 99.9%" + big "99.9%" mint; sun icon? No — a
  small horizon line + "like the sun coming up" caption only (no literal sun).
- S25: full S-curve drawn (draw 2.5s) from 0% to 100%, with "flat / bends / flat"
  labels under the three segments; x-axis "people 0→70", y-axis "%".
- S26: wrong comparison: big grey "365" vs small "23" side by side, a "?" between;
  caption "your brain counts the wrong thing".
- S27: three bars growing: 45 (10 people), 190 (20), 435 (30) — periwinkle bars
  with labels; "×4" chip between 45 and 190.
- S28: handshake network — circle of 12 dots with lines between many pairs
  (thin grey, drawn), one mint pair highlighted; big "253 handshakes" below.
- S29: two curves: straight grey line "intuition" vs bending mint curve "pairs",
  same axes; the mint curve pulls away upward.
- S30: honest check — 12 month-bars of uneven heights (Jan–Dec, mid-grey) +
  "birthdays are not even" label + mint arrow up "more likely, not less".
- S31: classroom — 30 dots in 3 rows of 10 (filled #212120, stroke white) +
  "70.6%" mint chip top-right; caption "a classroom of thirty".
- S32: three groups: football team 23 dots + "50.7%", party 50 dots + "97%",
  wedding 100 dots (dense grid) + "99.99997%"; three columns, increasing density.
- S33: pigeonhole — a row of 365 ticks (dimension line, dense ticks) labelled
  "365 days", one extra mint dot above with an arrow down "person 366 → must
  match"; below: small "leap year: 50.6%" note. (Two-part scene: ceiling + leap.)
- S34: perspective field — three dot-fields growing: lecture hall (small dots,
  many), wedding (medium), stadium (large, dense) with "more people → more
  certain" caption; sizes 0.6 / 0.85 / 1.15.
- S35: security — two document rects (filled #212120) with hash lines, both
  pointing to ONE fingerprint chip (mint outline) "same fingerprint"; caption
  "pairs grow faster than people, everywhere".
- S36: two arrows: small grey "+1 person" vs big mint "+22 pairs"; the mint
  arrow 3× longer; caption "pairs grow faster than people".
- S37: recap three boxes: "23 people" / "253 pairs" / "50.7%" (third mint);
  SFX: tick ×3 then chime.
- S38: final — big "count the pairs" serif 48px centre + the 23-dot ring from S1
  returning (loop back to hook visual); wordmark "birthday — 04".

Scenes S1–S38, one per spoken line, in order. Line 33 (ceiling + leap year)
is a single two-part scene (S33).

## Audio / mix notes
- Lines rendered with voice B, speed 80. First line starts 0.8s, 1.2s gap after
  each line. TOTAL = last start + last duration.
- SFX (from rag-video-01-audio/): whoosh on big entrances (S1, S9, S16, S18),
  pop on dots (S1, S5, S27), tick on counting (S9, S20–S22, S36), thud on the
  "wrong question" hold (S4), chime on the flip + recap (S18, S36).
- Pad: 110 + 165 Hz sines, raised so pauses are not dead air (v2.2 lesson).
- Loudnorm toward −14 LUFS, TP ≤ −1 dBTP (voice crest factor may cap ~−16.8).

## Thumbnail (1280×720)
Black bg, giant "23" white serif left, "50.7%" mint right, small title
"WHY 23 PEOPLE IS ENOUGH" periwinkle below, 23-dot ring motif. No glow in-video;
thumbnail may use the same flat style (video 03 thumbnail used flat style too).

## Publish pack (draft — finalise after export)
- Title: Why 23 People Is Enough — The Birthday Paradox
- Category: Education. Language: English. Audience: not made for kids.
- Tags: birthday paradox, probability, maths, mathematics, statistics,
  combinatorics, paradox, 23 people, explained, science
- Description: hook + chapters + link to the GPS video as the previous video
  in the series. AFTER the chapters, add (a) one discussion question for the
  comments, and (b) a short source list for the numbers used — this is the
  format the reference channel Quaselo uses on its top videos (chapters +
  comment question + sources), and it is a trust signal this audience checks.
  - Discussion question: "Which number surprised you most — that 23 people is
    enough, that 253 pairs hide inside 23 people, or that 366 people make a
    match certain? Have you ever been in a room where two people shared a
    birthday? Tell us how many people were there."
  - Sources: the probability figures were computed directly from the standard
    birthday-problem formula (see Wikipedia, "Birthday problem"); the 366-person
    certainty is the pigeonhole principle. Full source list with URLs goes in
    rag-video-04-youtube-publish-pack.md.

## Changelog
- 2026-11-27: script + storyboard v1.0 (38 lines, ~1,090 words). Numbers verified
  by computation (see table above).
- 2026-11-27 ~12:55: v1.0 DELIVERED, draft for user approval. Voice B Quivering
  Oak speed 80, all 38 lines rendered first-pass clean (no duration flags).
  Correction during source check: lines 5/6/11 said "253 people in the room"
  for matching YOUR birthday — the exact figure is 253 OTHER people (254
  including you); re-rendered vo-05/06/11 and fixed script + lines.txt.
  Final: 1,188 words, TOTAL 627.608s (10:27.6), 113.6 wpm, 1.0x no speedup.
  Mix −15.72 LUFS / −1.18 dBTP. Export click offset 2.591s trimmed.
  Verification: 19 frames checked across all 8 chapters (hook, pairs, maths,
  curve, brain, try-it, recap) — no defects, no re-export; Whisper-small
  PASS on hook (line 1), middle (line 20) and end (line 38) — words heard at
  each timestamp match the scheduled line, A/V sync confirmed.
  Thumbnail 1280×720 (giant "23", mint "50.7%"). Publish pack includes the
  Quaselo-format additions: discussion question + source list after chapters.
  Mirrored to videos/04-birthday/ (md5 match). NOT uploaded anywhere.
