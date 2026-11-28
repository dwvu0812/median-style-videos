# GPS Short 1 — Cinematic v3 — BUILD NOTE

**File:** `short-01-11km-a-day-cinematic-v3.mp4` — 1080×1920, 25 fps, **47.60 s**,
2,669,982 bytes, H.264 + AAC 160k, yuv420p, faststart.
**Audio:** reused byte-for-byte from v2 (`audio.m4a`, 47.568 s, extracted from the
published Short) — no voice re-record. Click offset measured 2.543 s (trimmed).
**Player:** `build/short-01-cinematic-v3.html` (683 lines). Export: `build/export_short.py`
(Playwright 1080×1920 record, 2 s pre-click wait, trim measured offset, mux).
**Status:** proof of the cinematic rules. **NOT uploaded** — the published Short
(`short-01-11km-a-day.mp4`) is untouched, as are cinematic v2 and every published file.

## What changed vs v2 (the two named fixes + the two follow-ups)

1. **Beat 2 fixed — the callout arrives WITH the dot.** In v2 the dot traced for
   4 s before the callout appeared. In v3 the callout circle arrives at beat start
   (1.8 s), the "38" glides in and counts 0→38 *while* the dot traces (9.9–13.9 s),
   and the connector lines draw in sync (4 s linear). Verified at t=9 (callout "5",
   dot mid-glide), t=10 (callout "11", dot at the line start), t=15 (trace done,
   callout "38", "×26,316 magnification" visible).
2. **Shared-element morphs instead of full-frame crossfades.** One persistent
   `<g id="stage">` holds the chips, scale/million-line, trace trail, road, pin,
   marker-dot, "38", and the payoff. Every beat change is an explicit `MORPHS[]`
   tween (from/to, 1.2 s ease-out, pure function of elapsed time) — the scale
   *becomes* the million-line, the marker *becomes* the trace dot, the road
   *becomes* the grid street, the payoff *glides* from the bottom into the giant
   centre restatement and back down for the loop. Beat groups hold only labels and
   still fade 0.45 s (blur on the outgoing group only); the picture underneath
   never wholesale-swaps. The loop-back at 45.54 s is a morph back to the Beat-1
   state, not a crossfade to a duplicated group (v2's `#b7loop` duplicate is gone).
3. **Frame 1 carries the payoff.** "11 km / day" is huge and mint at the bottom of
   frame 1, integrated with the tug-of-war (+45 mint vs −7 periwinkle, "= 0 µs/day",
   the scale with the marker at −7). A feed viewer learns what the Short is about
   without waiting ~20 s. **Verdict: yes — frame 1 reads as the payoff at a glance.**
   (t=0 verified on the final mp4: payoff + chips + counter + marker + caption
   "Subtract one from the other," all present.)
4. **Full vertical height.** Every beat is composed for 1080×1920 (usable band
   y≈150–1330, captions 1335–1393, nothing below y≈1420). v2's compositions were a
   horizontal band with the top ~25% and bottom ~35% empty; v3 spreads eyebrow,
   main object, scale/road, and caption into separate vertical zones. The phone in
   Beat 3 is taller (300–1100), the signal dot travels *down* the phone's edge
   (vertical motion), Beat 4 has a vertical bar that grows upward in sync with the
   distance counter.
5. **Beat 4 camera push-in** (the one worked calculation): viewBox zoom 1.2× on
   the "11" (22.14–25.14 s, hold, out by 29.14 s). Captions live in an HTML overlay
   (`#capOverlay`) so the zoom does not move them. Verified at t=24/26/27: the zoom
   does not clip the "km / day" text or the pin.
6. **Caption staged at load** (`showCaption(0)` in the init): frame 1 of the export
   already carries the first caption (before this fix the first caption only
   appeared at the first 100 ms tick).

No `Write` primitive is used in v3 — no formula ≥48 px needs stroke-drawing here;
the template has Write (see the skill) and the note records the absence so the
next Short that needs it uses it.

## Numbers — old vs v2 vs v3 (fixed meter, `build/measure_framediff.py`)

Measured with the v3 meter: ~1 fps, mean absolute grey-level difference, reported
at BOTH scales. The meter itself was fixed during this build (see below), so all
three videos were re-measured with the same fixed meter — these are the canonical
numbers. (The v2 BUILD-NOTE's 1.21 median was measured with the old `fps=1`
meter; the comparable v2 number is 1.44.)

| metric (legacy 320×180) | old (published) | v2 | **v3** | bar |
|---|---|---|---|---|
| median frame-diff | 0.20 | 1.44 | **2.03** | ≥1.5 — **PASS** |
| mean frame-diff | 0.90 | 2.05 | **2.98** | — |
| max (burst size) | 4.10 | 7.73 | **10.64** | ≥25 — **FAIL** |
| near-frozen <0.2 | 51.1% | 0.0% | **0.0%** | ≤10% (hook) — **PASS** |
| near-frozen <0.5 | 61.7% | 21.3% | **12.8%** (6/47 s) | ~0% — improved, not met |
| first-5 s median | 0.33 | 1.44 | **1.25** | ≥1.0 (Shorts) — **PASS** |
| hook density (`check_density.py`) | — | 20 events | **61 events** | ≥6 — **PASS** |
| payoff spoken | — | 2.26 s | **2.26 s** | ≤5 s — **PASS** |

Native-aspect (180×320) numbers are near-identical (v3: median 2.00, mean 2.98,
max 10.70, <0.2 0.0%, <0.5 12.8%, first-5 s 1.27) — see "meter corrections" below.

The 6 sub-0.5 s in v3 (fixed meter): t4→5 (0.28), t5→6 (0.28), t7→8 (0.29) —
Beat 1's tail, the marker patrolling alone; t17→18 (0.31) — Beat 3, the clock hand
+ signal dot are the only motion; t43→44 (0.45), t44→45 (0.41) — Beat 7's tail,
the pin travelling alone. No second is <0.2.

## Meter corrections discovered while measuring v3

- **`fps=1` duplicates frames.** The old meter extracted with `-vf fps=1`, which
  rounds timestamps and can emit the SAME frame twice. v3 measured 0.01/0.02 for
  t4→t5 and t7→t8 that way; a direct `-ss` comparison of the same intervals is
  0.28/0.29 — the video is moving, the extraction was lying. The v3 meter now
  selects by FRAME NUMBER (`select='not(mod(n,25))'`, `-vsync 0`, assumes 25 fps).
  All three videos above were re-measured with it.
- **The vertical squash is disproven.** v3 at legacy 320×180 vs native 180×320:
  median 2.03 vs 2.00, near-frozen identical — the 10.7× squash does NOT hide
  motion. The v2 BUILD-NOTE's squash explanation for the unmet bar was wrong.
  The meter's real blind spot is **low-contrast fades**: a fade between two
  mostly-black frames scores ~0.1 even though the eye sees a clear transition
  (v3's 8→9 s B1→B2 morph). The skill + WORKFLOW.md meter notes are corrected.
- **Run-to-run jitter:** the same file measures median 1.65–2.03 across meter
  methods (and v2's note recorded 1.10–1.38 across export runs). Treat the median
  as ±0.2, not exact.

## Frame verification (final mp4, viewed)

t=0 — frame 1: payoff "11 km / day" mint + huge, chips +45 mint / −7 periwinkle,
"= 0 µs/day", marker at −7, caption "Subtract one from the other,". Clean.
t=1 — counter "5", marker travelling, caption in sync. Clean.
t=2 — counter "15", marker mid-travel, caption in sync. Clean.
t=5 — counter "38", marker at +45 (the designed overshoot before settling to +38).
Clean.
t=9 — B1→B2 morph mid-flight: old beat ghosting out, callout "5" counting, dot
gliding, connector lines drawing. Clean.
t=10 — callout "11", dot at the line start, trace beginning. Clean.
t=15 — trace done, dot at 1,000,000, callout "38", "×26,316 magnification". Clean.
t=24 — zoom mid-push-in: "11" huge and sharp, "km / day" fully opaque, pin +
mint trail, "2.7 km", vbar growing. Clean.
t=26 — zoom at full push-in: "km / day" fully visible, clear of the vbar (fixed,
see bugs). Clean.
t=27 — zoom easing out, vbar tall, "7.3 km", pin mid-travel. Clean.
t=30 — B4→B5 transition: outgoing "11" dissolving over incoming "11.0 km" (both
read "11" for ~0.45 s — a known wart, see limits), pin mid-glide to the drop
point. Acceptable, not clean.
t=38 — Beat 6: first wave of 10 month-dots, counter "157 km", "wrong city"
(not yet struck). Clean.
t=45 — giant mint "11 km / day" centre, pin travelling with full mint trail,
caption in sync. The money shot. Clean.
t=46.5 — loop-back: Beat-1 composition restored (chips, "= 38", scale + marker at
+38, payoff at the bottom), caption "unless Einstein saves it." Clean.

## Whisper spot check (faster-whisper base, final mp4)

- Hook 0–9 s: "Subtract one from the other and the satellite clock ends up
  gaining about 38 microseconds a day." — word-for-word. PASS.
- Middle 22.65–29.69 s: "and 38 microseconds becomes about 11 kilometers of air
  every day." — right sentence; "error" misheard as "air" (Whisper, same as v2 —
  the reused audio says "error"). PASS.
- End 40.54–47.6 s: "Your phone would light to you by 11 kilometers a day, unless
  Akinstein saves it." — right sentence; "lie"→"light", "Einstein"→"Akinstein"
  (Whisper mishearings of the reused audio, same as v2). PASS.
A/V sync correct at all three points.

## Bugs found and fixed during this build

1. **Paint order — the "38" was invisible in the callout.** The persistent
   `#stage` was painted BEFORE the beat groups, so Beat 2's callout circle
   (opaque #141414 fill) covered `num38`. Fixed by moving the whole `#stage`
   group AFTER the beat groups (stage elements now paint above beat-group fills).
2. **Fill attributes lose to `.math{fill:#fff}`.** "+45", "−7", and the payoff
   "11" were written with `fill="#6FCF97"` / `fill="#7E9BFF"` attributes and
   rendered WHITE. Fixed with the colour classes (`class="math green"` /
   `class="math blue"`, defined after `.math` in the stylesheet).
3. **Self-inflicted file corruption (fixed, verified).** The script that did fix
   (1) matched the literal string `<g id="stage">` inside a CSS comment in
   `<style>` and cut the file at the wrong place, landing the beat groups inside
   `<style>` as text. Reconstructed by reversing the rearrangement (all content
   was preserved, only order was wrong) and verified: structure assertions
   (svg < b1 < b7 < stage < /svg, 7 beats, one `</style>`), `node --check`,
   density PASS, full smoke test, full export.
4. **First caption missing from frame 1.** The caption is set on the first tick
   (~100 ms in), so the export's frame 0 had no caption. Fixed with
   `showCaption(0)` at load.
5. **Beat-4 zoom pushed the vbar into the "km / day" text.** At full 1.2×
   push-in the growing vbar (x 930–970) clipped the tail of "km / day"
   (x 640–~950 at font 80). Fixed by moving the text to x=610 and shrinking it
   to font 72 (ends ~897 viewBox; clear of the vbar zoomed and unzoomed).
   Caught at t=26, fixed, re-exported (3rd export), re-verified at t=26/27.
6. **`goTo`/`play` could leave two beats `.active`.** `showBeat` only removes
   the class from the previously-tracked beat; a seek invalidates the track.
   Fixed: `goTo` clears all beat classes first; `play()` restarts via `goTo(0)`.

## Honest rewatch verdict

Would I loop it voluntarily? **Beats 4–7, yes — Beats 1–2, mostly.** The morph
from 38 µs to 11 km, the trace with the counting callout, the day/month dots, the
pin leaving its mint trail, and the giant "11 km / day" restatement are the parts
I would rewatch — the picture now changes every second and the payoff lands
twice (frame 1 and Beat 7). The first 5 seconds earn the next 5, which the old
Short never did, and frame 1 now tells the whole story at a glance.

What still bores me: **Beat 1's tail (5–8 s)** is the weakest stretch — after the
counter lands at 3.8 s, the only motion is a small marker patrolling ±45 px on a
line (the meter's three slowest seconds are all here). On a rewatch I would skip
from 4 s to 9 s. **Beat 3 (17–18 s)** is the second-weakest second — a spinning
clock hand and a small dot down the phone's edge, everything else static.
**Beat 7's tail (43–45 s)** is a lone pin travelling. And the **burst bar is still
unmet (10.6 vs ≥25)**: our biggest single-second change is ~11 grey levels,
while winners change the picture by 28–83 in a second — we have no single moment
as big as Animated Math's scene transformations. The 0.45 s dissolve at t=30
("11" over "11.0 km") is the ugliest single frame; a real morph of the "11" into
the "11.0 km" readout would kill it.

Verdict: v3 passes the screening bar the skill sets (median ≥1.5, hook
near-frozen 0%, first-5 s ≥1.0, hook density 61) and is a real step past v2 on
every number — but it is not yet a Short I would loop end-to-end voluntarily.
The next fix, in order: (1) give Beat 1's tail a second moving element (the
payoff breathing, or the marker leaving a trail); (2) a bigger burst in the hook
(a full-scene morph in the first 5 s, not just the counter); (3) morph the "11"
into "11.0 km" instead of dissolving at 29.69 s.

## Known limits

- No `Write` primitive used (no formula ≥48 px here).
- Loop seam: the last frame shows "= 38", the first frame shows "= 0" (the
  counter restarts on loop). The composition matches; only the counter jumps.
- The B2 recount jumps 38→0 at 8.7 s, masked by the glide into the callout.
- `check_density.py` counts what the HTML declares; JS-built elements (the 30
  month dots) are invisible to it unless declared in `events[]` — v3 declares
  them, so its 61 is honest.
- Meter: the fps=1 duplicate-frame bug and the fade blind spot are documented
  above; the skill + WORKFLOW.md are corrected, and `measure_framediff.py`
  (this folder) selects by frame number.
