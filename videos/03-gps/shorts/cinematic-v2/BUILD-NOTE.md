# GPS Short 1 — Cinematic v2 (vertical-native rebuild)

## What it is

A rebuild of the published GPS Short 1 ("Your GPS Would Lie to You by 11 km
a Day", https://youtube.com/shorts/01VTX6SlLPQ — 186 views, 4.1% stayed)
using the cinematic rules added to the video skill on 2026-11-28.
Same audio, same words, same 47.6 s — all-new visuals.

**The old Short's defect (animation audit, 2026-11-28):** a letterboxed
1080×607 strip on black, nothing moving in the first 2 seconds (first-5s
median frame-diff 0.17; the first 5 frames were literally identical).
The rebuild is vertical-native 1080×1920, full-bleed, motion in frame 1.

**DO NOT upload this file.** It is a proof of the new rules, not a
replacement for the published Short. The original Short, the GPS master
and every published file are untouched.

## Files

| File | What it is |
|---|---|
| `short-01-11km-a-day-cinematic-v2.mp4` | **The Short.** 1080×1920, 25 fps, H.264 + AAC 160k, yuv420p, faststart, 47.6 s, 2,289,249 bytes |
| `audio.m4a` | Audio extracted from the published Short (no re-record). 47.568 s |
| `build/short-01-cinematic-v2.html` | The player (single 1080×1920 SVG stage, 7 beats) |
| `build/audio.m4a` | Copy of the audio for the player |
| `build/export_short.py` | Playwright export: record 1080×1920, measure the real click offset, trim it, mux audio |
| `build/measure_framediff.py` | Frame-diff meter — same method as the audit (~1 fps, 320×180) |
| `frames/final_t{0,1,2,5,15,30,45,46}.png` | Verification frames from the final mp4 |

## The 7 beats (lines 23–24, master 432.2→479.768)

| Beat | Time | What happens (a new visual every 1–2 s) |
|---|---|---|
| B1 SUBTRACT | 0.0–8.7 | Chips +45 / −7 slide in from both sides; counter 0→38; marker travels the −7→+45→+38 scale, then patrols around +38 |
| B2 PARTS IN A MILLION | 8.7–15.87 | A dot traces the 0→1,000,000 line (4 s, linear); callout magnifies the 38; callout breathes after the trace |
| B3 PHONE NOTICES | 15.87–20.14 | Phone + spinning clock hand (6 s/rev); minutes count 1→4; holds the 1.2 s line gap |
| B4 TIME→DISTANCE | 20.14–29.69 | Morph: "38 µs/day" fades out as "11" counts in; pin travels the road leaving a mint trail; distance counter 0→11.0 km |
| B5 A WEEK, WRONG CITY | 29.69–36.89 | 7 day-dots arrive one by one; error counter 11→77 km; pin drops on the wrong block |
| B6 A MONTH, WRONG COUNTRY | 36.89–40.54 | 30 dots in 3 waves; counter 77→330 km; "wrong city" struck through, replaced by "wrong country" |
| B7 THE LIE + LOOP | 40.54–47.568 | Giant "11 km / day" restated; pin + trail; at 45.54 s the frame crossfades back to the Beat-1 composition, so the loop restarts on the same picture |

Captions: 14 cues, re-split from the shipped `.ass` to ≤34 chars/line,
≤2 lines, in the band y≈1335–1393 — above the bottom ~400 px safe zone.
No channel tag (the old one at y=1830 collided with YouTube's Shorts UI).
Top ~250 px kept empty. Crossfades 0.45 s, blur on the outgoing beat only.

## Frame-diff: old vs new (same meter, ~1 fps, 320×180)

| | Old Short | Cinematic v2 (shipped file) |
|---|---|---|
| Median second-to-second change | **0.18** | **1.21** grey levels (6.7×) |
| Mean | 0.84 | 2.07 |
| Max | 3.82 | 8.29 |
| Near-frozen seconds (<0.5) | **29 / 47 = 61.7%** | **9 / 47 = 19.1%** |
| First-5-seconds median | 0.1 (frames literally identical) | **1.0** |

Across the 5 export runs the new build measured median 1.10–1.38 and
frozen 17–34% (recording jitter); the shipped file is the 5th export
(median 1.21, frozen 19.1%). Remaining frozen seconds in the shipped
file: 5, 8, 10, 24, 25, 26, 27, 35, 44 — all at 0.2–0.5, i.e. slow
change, not the 0.0–0.1 identical frames the old Short had.

**The skill's bar (median ≥1.5, frozen ~0%) was NOT met.** Honest
account of why, after 4 improvement passes (linear counters/pins,
bigger marker/pins, mint trails, breathing callout + "38"):
the meter downscales 1080×1920 to 320×180, which squashes the vertical
axis 10.7× — any horizontal element thinner than ~11 px becomes
sub-pixel and stops registering, however visibly it moves. The remaining
frozen seconds are exactly the small-element-only stretches (a lone
marker, a lone pin, the trace dot's first second). Closing the last gap
needs bigger/taller moving masses — vertical motion, not just horizontal
travel — and real morphs (shared elements persisting across beats)
instead of full-frame crossfades. The meter is a proxy, not the viewer:
in the shipped file the picture visibly changes every second; the
meter just can't see thin horizontal motion at this downscale.

## Verification (final mp4)

- **Frames viewed:** t=0, 1, 2, 5, 15, 30, 45, 46.5 — all clean.
  t=0 is the full Beat-1 composition (chips, "= 0 µs/day", scale,
  marker at −7) — not black. t=2: "= 13" with the "=" clear of the
  number. t=15: trace done, callout "38 of 1,000,000". t=30: mid-crossfade
  B4→B5 (expected 0.45 s dissolve, not a defect). t=45: "11 km/day"
  with pin + mint trail. t=46.5: loop-back crossfade to the Beat-1
  composition. Captions in sync in every frame.
- **Whisper (base) on the final mp4 — PASS at all 3 points:** hook
  (0–9 s) heard word-for-word; middle (22.65–29.69 s) heard the right
  sentence ("error" misheard as "air"); end (40.54–47.6 s) heard the
  right sentence ("lie"→"light", "Einstein"→"Akinstein" — Whisper
  mishearings of the reused audio, not a sync fault). A/V sync correct.
- **Bugs found and fixed during the build:** (1) chip labels clipped by
  the chip border — chips made taller; (2) the trace dot ran ahead of
  its line (ease-in-out line vs linear dot) — line redrawn linear 4 s
  to match the SMIL dot; (3) "=" collided with two-digit counter
  values — "=" moved left, counter shrunk to 200 px; (4) frame 0 came
  out pure black (no beat active at load) — Beat 1 is now staged at
  load and the export waits 2 s before the click so the entrance has
  settled; (5) ease-out/ease-in-out tails read as frozen on the meter
  — all JS-driven motion is now linear.

## Honest rewatch verdict

Would I rewatch it? Beats 4–7, yes — the morph from 38 µs to 11 km,
the day dots, the month dots, the pin leaving its mint trail, and the
giant "11 km / day" restatement are satisfying to watch; the loop-back
makes the ending feel like a reset rather than a stop. The first 5
seconds now earn the next 5, which the old Short never did.

What still bores me: **Beat 2 is the weakest stretch** — 4 seconds of
one small dot on a long empty line before the callout arrives; on a
rewatch I'd skip it. Beat 1's tail (after the counter lands at 3.8 s)
is a marker wobbling on a line — the breathing "38" helps, but the
frame is mostly static text. The 0.45 s crossfades cost ~3 s of the
video in double-image blur; a real morph (shared elements carrying
across beats) would feel like Median and look less like a slideshow
with dissolves. And the content itself is one idea stretched over
48 seconds — beats 5–7 repeat the same number three times (11, 77,
330 km, then 11 again), so a viewer who got the point at 20 s may
still swipe before the loop.

Verdict: a 7× improvement on the meter and the frame-1 problem is
fixed, but not yet a Short I'd loop voluntarily. The next two fixes,
in order: (1) rebuild Beat 2 so the callout arrives with the dot
instead of 2 s after it; (2) replace full-frame crossfades with shared-
element morphs between beats.
