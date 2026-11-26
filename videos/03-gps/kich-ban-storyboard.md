# Video 03 — "Why GPS Would Fail in 2 Minutes Without Einstein"

**Series:** Median-style animated explainers, English, for an international YouTube audience.
**Core idea (one sentence):** Your phone finds where you are by measuring time to billionths of a second — and Einstein's relativity makes satellite clocks drift by 38 microseconds a day, which is 11 km of error a day, 8 metres a minute, so after 2 minutes GPS accuracy is already broken unless engineers pre-correct the clocks.
**Through-line (carried through the whole video):** "Your phone would lie to you by 11 km a day — unless Einstein saves it."
**Format:** long-form, 38 spoken lines, 38 scenes, 8 chapters. **v2.0: 1,479 words, raw 616.7s (10:16), sped up 1.25x → ~493s (~8:13) fast final.**
**Voice:** Muse built-in TTS **avocado_v2:vd2_smoky_teacup** ("voice A"), English, speed 105. Vietnamese accent — accepted by the user (speed over native accent, 2026-11-26). NOT Gemini Charon, NOT ElevenLabs (both dropped 2026-11-26: Gemini hit its free-tier quota wall, ElevenLabs approvals were denied by the user).
**Wordmark (bottom-right, small, low contrast):** `gps — 03`

## v2.0 changes (2026-11-26 — user watched v1.0: "video bị chậm, thiếu animation")
1. **Story pass:** rewritten for clarity and engagement. One question carried through ("your phone would lie by 11 km a day — unless Einstein saves it", lines 24 + 38). Stakes anchored in everyday life: maps, food delivery finding your door, morning run measured right, delivery driver at the wrong door. Short plain sentences; jargon cut ("gravitational field" → plain words; "measured to exquisite precision" cut; the 10.22999999543 MHz number is shown on screen, spoken short as "less than five thousandths of a hertz"). All 38 lines re-recorded with voice A speed 105 (one consistent take), mix rebuilt, timing re-measured.
2. **More animation in every scene:** no more fade-in-then-hold. Continuous meaningful motion everywhere — satellites actually orbit/travel their arcs, clock hands tick (ground slow, satellite fast), light pulses race down signal lines, the error bar grows, the dot drifts off the road, the "38" counts up live. Entrances are fast and decisive (slam/draw-fast), then settle into slow holds.
3. **Eye-catching direction:** hook frame hits in the first 3s (phone + ticking clock + mint pulse ring); "2 minutes" is 120px and slams in; one big high-contrast moment per chapter (giant −7 blue, giant +45 mint, live count-up to 38, the long MHz number in blue). Accents used boldly at key moments.
4. **Faster pace:** finished video sped up 1.25x (ffmpeg setpts=0.8 + atempo=1.25) → `rag-video-03-1080p-fast.mp4` is the new final (~8:13). v1.0 mp4 kept as `rag-video-03-1080p-v1.mp4`.
5. **Thumbnail:** `rag-video-03-thumbnail.png` (1280x720) — black bg, giant "2 MINUTES", "WITHOUT EINSTEIN" in periwinkle, phone + ticking clock, mint satellite dot, bending grid.
6. **Flaw fixed:** in the "3.9 km/s" scene (13) the subtitle was moved above the orbit arc — the arc no longer passes behind the text.

## v2.1 changes (2026-11-26 — user: "khá oke rồi, nhưng cần chỉnh code phần animation cho mượt hơn, giống kênh median hơn")
Motion-language polish only — **script, voice, mix and timing untouched** (same 38 lines, same 616.688s mix, same scene t0/dur). v2.0 final kept as `rag-video-03-1080p-fast-v2.0.mp4`; new final keeps the name `rag-video-03-1080p-fast.mp4`.
1. **Entrances:** every `slam` (0.5s, scale 1.14 snap) replaced by `arrive` — slow ease-out scale 1.06→1 + blur(6px)→0 + fade over 1.8s, cubic-bezier(0.22,1,0.36,1). f1/f2/f3 stagger kept (0s / 1.4s / 2.8s), now with blur-fade (blur(8px)→0, 1.8s, same ease-out) instead of plain fade.
2. **Line drawing:** `drawfast` (0.8s) replaced by `draw` — 2.5s ease-in-out, with `pathLength="100"` on the drawn line/path so dasharray 100 always means the full length (the old dasharray 600 also left the last 40px of the 640px ray in scene 9 undrawn).
3. **Loops slowed, amplitude shrunk:** pulse 2.4s→5s (opacity .45–1), breathe 7s→6s (scale 1.03, opacity .92), bob −10px→−6px / 6s, drift 18px→10px / 6s, grow-loop 4.5s→6s, sway ±2°→±1.5°. SMIL travelling pulses: 2.2s→4.5s (stagger 0/1.1/2.2/3.3s), 2s→4s, 2.5s→5s, 3s→5s, 6s→8s. Orbits (26s/12s) and clock hands (24s/12s/6s) stay linear — constant speed is physically correct.
4. **At most 2 things moving at once per scene:** removed the bobbing satellite dots in scenes 6/33/35 (the travelling pulses are the motion there), the breathing phone rect in scene 33, and the breathing grid in scene 18 (Earth breathe + orbiting mint dot remain).
5. **Transitions:** scene crossfade 0.5s→0.9s, plus a blur dissolve — outgoing scene blurs to 6px as it fades out, incoming blurs in from 6px.
6. **Big moments arrive smoothly:** giant "2 minutes", −7, +45, "38 µs = 11 km/day", "10.22999999543 MHz" etc. now scale in with `arrive` instead of slamming. Count-up 0→38 (scene 23) now 3s with ease-out instead of 2.4s linear.
7. **Timing fix (corrected after the first v2.1 export failed end-sync):** first attempt drove the scene clock from the `<audio>` element's `currentTime` — WRONG under recording load: headless Chromium's audio clock runs ~2% slow (measured 2026-11-26: audio advanced only ~58.7s per 60s of wall time), so the picture lagged the voice by ~13s at the end and the final scene ("right in the sky") never appeared in the export. Fixed by driving the clock from `performance.now()` wall time instead: `elapsed = (performance.now() - startPerf) / 1000`, recomputed every tick so late `setInterval` firings never accumulate (`startPerf` reset in `play()`/`goTo()`). The audio element is only for the preview; the recorded video is muxed with the mix afterwards, so scenes must follow wall time.
8. Per-scene "Motion" tables below still say v2.0 — read them with this mapping: slam→arrive (1.8s ease-out), drawfast→draw (2.5s), pulse/breathe/bob/drift/grow-loop at the v2.1 periods above, travelling pulses at the v2.1 durations above.

## Verified numbers (checked 2026-11-26 — Perimeter Institute, Ohio State, GPS World, Neil Ashby)

| Fact | Value |
|---|---|
| GPS altitude | ~20,200 km (12,500 miles) |
| Orbital speed | ~3,874 m/s (~3.9 km/s, ~2.5 miles/s), orbit ~12 h |
| Light in 1 ns | ~30 cm (~1 foot) |
| 1 µs of clock error | ~300 m of position error |
| Special relativity (speed) | satellite clock **slow** by ~7 µs/day (−7.2) |
| General relativity (height) | satellite clock **fast** by ~45 µs/day (+45.7) |
| Net drift | **+38 µs/day** (~38.6) |
| Error if uncorrected | ~11 km/day (~7 miles), ~8 m per minute, ~16 m in 2 min |
| GPS accuracy promise | ~5–10 m |
| Factory offset | clocks set to **10.22999999543 MHz** instead of 10.23 MHz (offset −0.004567 Hz) |
| NTS-2 test (1977) | satellite flew with a switch: relativity correction on/off; drift matched Einstein's prediction |

**Careful phrasing:** "fails in 2 minutes" means the *accuracy promise* breaks (error ~16 m > 5–10 m), NOT a blackout — the map still draws, the dot just drifts to the wrong street.

## Title / hook (per research §6)
- Title: **"Why GPS Would Fail in 2 Minutes Without Einstein"** — question + specific number + familiar object.
- Hook structure (0–30s): 0–3s show the surprising visual (phone + ticking clock + mint pulse ring); 3–10s ask the question (the 2-minute claim, 120px slam); 10–30s promise the mechanism ("one shape, two clocks"). Mechanism starts closing before minute 3 (Part 3: 1 ns = 30 cm).

## Script (38 lines, 1,479 words, v2.0)
Spoken lines live in `rag-video-03-audio/lines.txt` (one per line). On-screen text keeps digits; spoken text spells numbers out ("thirty-eight microseconds", "ten point two three megahertz").

### PART 1 — HOOK (lines 1–3)
| # | Spoken line (short) | Frame | Motion (v2.0) | On-screen text | Sound |
|---|---|---|---|---|---|
| 1 | Your phone is running a relativity experiment, right now, in your pocket. | Phone outline centre, small clock above it ticking | Phone slams in; clock hand ticks (12s loop); mint ring pulses | `your phone` + ticking clock | whoosh |
| 2 | If Einstein had been wrong, your maps would stop working in about two minutes. | Huge serif "2 minutes" centre | 120px, slams in; mint bar grows + loops under it | **2 minutes** | thud |
| 3 | Relativity sounds like black holes, not coffee shops — but you'll see why, with one shape and two clocks. | Two clocks side by side (ground dim, satellite blue) | Ground hand slow (24s), satellite hand fast (6s) — time visibly runs differently | `one shape, two clocks` | pop |

### PART 2 — GPS IS A CLOCK, NOT A MAP (lines 4–8)
| # | Spoken line (short) | Frame | Motion (v2.0) | On-screen text | Sound |
|---|---|---|---|---|---|
| 4 | Forget the map. GPS is a clock — a whole sky full of clocks. | Big serif "GPS = a clock" | Ring of 4 dots orbits the text (26s); text slams in | **GPS = a clock** | whoosh |
| 5 | 30+ satellites, 20,200 km up, each broadcasting where it is and the exact time. | Earth arc at bottom, satellite dot on orbit line | Satellite dot travels the arc, ping-pong (16s) | `20,200 km · 12,500 miles` | pop |
| 6 | Your phone listens to 4 of them and measures how long each signal took. | Phone at bottom, 4 satellite dots, dashed lines down | Light pulses race down the 4 lines (2.2s, staggered); satellites bob | `4 signals` | tick |
| 7 | Four travel times solve four unknowns: x, y, z — and time itself. | Four serif variables x, y, z, t in a row | Blue t pulses; mint ring breathes around it | *x y z t* | pop |
| 8 | Why four, not three? The fourth exists to measure your phone's own clock error. | Three dots + one highlighted blue dot | 4th blue dot pulses; ring breathes | `4th = your clock error` | tick |

### PART 3 — LIGHT-SPEED TIMING (lines 9–12)
| # | Spoken line (short) | Frame | Motion (v2.0) | On-screen text | Sound |
|---|---|---|---|---|---|
| 9 | Signals travel at light speed — 300,000 km/s. No room for almost. | Light ray line drawing across the frame | Ray draws fast; white pulse races along it (1.8s loop) | *c* = 300,000 km/s | whoosh |
| 10 | In 1 nanosecond, light travels 30 cm — a school ruler. | Ruler line with ticks | Light pulse races across the ruler (2s); mint segment pulses; "1 ns = 30 cm" 56px slams in | **1 ns = 30 cm** | tick |
| 11 | 1 ns wrong = 30 cm off. 10 ns wrong = 3 m off. Billionths decide everything. | Two conversion rows | "3 m" breathes | `1 ns → 30 cm` / `10 ns → 3 m` | tick |
| 12 | GPS promises 5–10 m accuracy — enough for your delivery to find your door. | Crosshair/target with "5–10 m" | Target rings breathe; centre dot pulses | **5–10 m** | thud |

### PART 4 — SPECIAL RELATIVITY: SPEED SLOWS TIME (lines 13–17)
| # | Spoken line (short) | Frame | Motion (v2.0) | On-screen text | Sound |
|---|---|---|---|---|---|
| 13 | Satellites race at 3.9 km/s — circling Earth twice a day. | Satellite dot moving along orbit arc | Dot travels the arc, ping-pong (14s); "3.9 km/s" slams in; subtitle moved above the arc | `3.9 km/s` | whoosh |
| 14 | Special relativity (1905): a moving clock ticks more slowly. Not the machinery — time itself. | Two clocks: ground clock normal, moving clock with slower hand | Ground hand slow (24s), satellite hand fast (6s) | `moving clocks run slow` | pop |
| 15 | From Earth, the satellite clock looks slow: it loses ~7 µs every day. | Big serif "−7 µs / day" | 110px blue, slams in; blue underline grows in a loop | **−7 µs / day** | tick |
| 16 | 1 µs = 300 m of error. So 7 µs/day ≈ 2 km of error a day, from speed alone. | Conversion: "7 µs → 2.1 km / day" | Blue dot falls down the arrow, looping (2s) | `7 µs/day → ≈ 2 km/day` | tick |
| 17 | That alone would break maps in a day or two. But speed is only half the story. | Tug arrows: "−7" left vs "+45" right (right dim for now) | Beam sways; dim +45 pulses, waiting its turn | `−7` ↔ `+45` | pop |

### PART 5 — GENERAL RELATIVITY: HEIGHT SPEEDS TIME (lines 18–22)
| # | Spoken line (short) | Frame | Motion (v2.0) | On-screen text | Sound |
|---|---|---|---|---|---|
| 18 | General relativity (1915): gravity slows time down. Stronger gravity, slower clock. | Spacetime grid bending near Earth circle | Grid breathes (bends); Earth circle breathes; mint dot orbits Earth (12s) | `gravity bends time` | whoosh |
| 19 | Down here gravity is strong, clocks run slow. Up in orbit, gravity is weaker — clocks run fast. | Earth circle + two clocks: ground dim slow, satellite bright fast | Ground hand slow (24s), satellite hand fast (6s, mint) | `slow down here · fast up there` | pop |
| 20 | 20,200 km up, clocks gain ~45 µs/day, just from being high up. | Big serif "+45 µs / day" | 110px mint, slams in; mint underline grows in a loop | **+45 µs / day** | tick |
| 21 | Two identical clocks, one on the ground, one in the sky — the sky one pulls ahead by 45 µs a day. | Two clocks side by side, satellite one visibly ahead | Ground hand slow, sky hand fast; "sky · +45 µs" pulses | `+45 µs` | tick |
| 22 | Tug of war: speed pulls slow by 7, height pushes fast by 45. | Tug of war: "−7" left, "+45" right, balance tilting right | Beam sways; +45 mint pulses | `−7` ↔ `+45` | thud |

### PART 6 — THE NET DRIFT: +38 µs/day AND THE 2-MINUTE FAILURE (lines 23–28)
| # | Spoken line (short) | Frame | Motion (v2.0) | On-screen text | Sound |
|---|---|---|---|---|---|
| 23 | 45 − 7 = 38. The satellite clock gains ~38 µs a day. | Equation big serif "45 − 7 = 38" | "38" counts up live 0→38 (JS); equation slams in; mint underline grows | **45 − 7 = 38** | chime |
| 24 | 38 µs = ~11 km of error a day (~7 miles). A week: wrong city. A month: wrong country. | Big "38 µs = 11 km / day" | White bar grows under the number, looping | **38 µs = 11 km / day** | tick |
| 25 | Per minute: the error grows ~8 m every minute, without stopping. | Growing error bar | Blue bar grows across the whole frame, looping; "8 m / minute" slams in | `8 m / minute` | tick |
| 26 | It never resets. Every day adds another 11 km on top of yesterday's. | Accumulating staircase: 11 km + 11 km + 11 km… | Blue dot climbs the staircase (6s loop) | `11 km + 11 km + 11 km…` | tick |
| 27 | Promise: 5–10 m. After 1 min: 8 m. After 2 min: 16 m. Promise broken. | "2 min → 16 m" vs "5–10 m" comparison | "2 minutes → 16 m" slams in; "16 m" pulses blue | **2 min → 16 m** | thud |
| 28 | The screen doesn't go black. The dot just quietly drifts to the wrong street. | Blue dot on a road line drifting off the road | Blue dot drifts off the road, ping-pong (6s) | `wrong street` | pop |

### PART 7 — THE FIX (lines 29–35)
| # | Spoken line (short) | Frame | Motion (v2.0) | On-screen text | Sound |
|---|---|---|---|---|---|
| 29 | How do engineers fix it? They cheat — before the satellite leaves the ground. | Satellite with a clock, launch pad line below | Satellite bobs; ring pulses | `fix it before launch` | whoosh |
| 30 | Atomic clocks tick at 10.23 MHz — but are set to run slow before launch. | "10.23 MHz" big serif, arrow down to "10.22999999543 MHz" | Long number slams in blue; blue dot falls down the arrow (2s loop) | **10.23 MHz** → 10.22999999543 MHz | tick |
| 31 | The change is tiny — less than five thousandths of a hertz. Exactly the 38 µs/day Einstein predicted. | "−0.004567 Hz" highlighted | Number slams in; "= 38 µs/day" pulses mint | `−0.004567 Hz = 38 µs/day` | chime |
| 32 | They build a clock wrong on Earth, on purpose — because it will be right in space. | Clock labelled "wrong on Earth" → arrow → "right in space" | Blue dot rides the arrow (3s); "right in space" breathes | `wrong on Earth → right in space` | pop |
| 33 | Your phone solves for its own clock error as a fourth unknown — corrected by the sky. | Phone with 4 signals, "4th unknown" highlighted | White pulses race down the 4 blue lines (2.2s, staggered); phone breathes | `4th unknown = your clock` | pop |
| 34 | 1977, NTS-2: engineers flew a switch — correction on, correction off — and the drift matched Einstein. | Switch with two positions: ON / OFF, two clocks | Green knob slides ON/OFF on its own (6s drift) | `correction ON / OFF` | tick |
| 35 | Nothing ignores relativity. Clocks pre-corrected, receivers self-correcting, ground stations uploading daily. | Triangle: ground station – satellite – phone | Mint pulses travel the triangle ground → satellite → phone (3s) | `fresh corrections daily` | chime |

### PART 8 — RECAP (lines 36–38)
| # | Spoken line (short) | Frame | Motion (v2.0) | On-screen text | Sound |
|---|---|---|---|---|---|
| 36 | Your phone finds where you are by measuring time. 30 cm per nanosecond. | Big serif "time → space" | Text slams in; white pulse rides under it (2.5s) | **time → space** | whoosh |
| 37 | Speed: −7. Height: +45. Net: +38 µs/day = 11 km/day, 8 m/min — if nobody corrected it. | Three stacked numbers "−7 / +45 / = +38" | Net row pulses; mint underline grows | `−7 · +45 · = +38 µs/day` | chime |
| 38 | Build the clock wrong on the ground, so it is right in the sky. Your phone would lie by 11 km a day — unless Einstein saves it. | Final: "wrong on the ground, right in the sky" + small clock | Small clock ticks above; "right in the sky" slams in blue and breathes | `wrong on the ground, right in the sky` | chime |

## Style (true Median, verified from real videos)
Pure black #000, flat 2D line art, white #FFF main, grey #9A9A9A secondary, accents only periwinkle #7E9BFF (selected/correction) and mint #6FCF97 (question) used sparingly — v2.0 uses them boldly at chapter peaks (giant numbers, underlines, pulses). Serif maths (Times/Georgia), bold sans headings, small tracked-caps grey eyebrow ("PART 1", "PART 2", … "RECAP" — English, not "PHẦN"). One centred object, huge negative space, slow fades, no camera moves, no 3D/glow/emoji. Scenes crossfade 0.9s with a blur dissolve (never display:none); gap bug fix: during pauses between lines keep the current scene. Motion (v2.1): slow blur-in entrances 1.8s ease-out cubic-bezier(0.22,1,0.36,1), line draws 2.5s ease-in-out, gentle 5–6s breathing loops, at most 2 things moving at once, one element at a time staggered 1.4s; orbits and clock hands stay linear (constant speed); scene clock from audio currentTime. CSS keyframes (spin/drift/bob/breathe/pulse/grow-loop/sway/arrive) scoped under `.active`, plus SMIL animateMotion for travelling dots/pulses; one JS count-up (scene 23, "38" counts 0→38, 3s ease-out).

## Files
- `rag-video-03-kich-ban-storyboard.md` (this file)
- `rag-video-03-animation.html` + `rag-video-03-export.html`
- `rag-video-03-audio/` — `lines.txt`, `vo-01..38.mp3`, `rag-video-03-full-audio.mp3`, `mix.json`, `timing.json`
- `rag-video-03-1080p.mp4` (v2.1 raw, 616.7s) + `rag-video-03-1080p-fast.mp4` (**final, 1.25x, ~493s**) + `rag-video-03-1080p-fast-v2.0.mp4` (v2.0 final backup) + `rag-video-03-1080p-v1.mp4` (v1.0 backup, 649.4s)
- `rag-video-03-thumbnail.png` (1280x720)
- Mirror: `~/workspace/median-style-videos/videos/03-gps/`
- Do NOT post to the Bug 5h Chiều Facebook page (English YouTube video, not a Vietnamese Reel).
