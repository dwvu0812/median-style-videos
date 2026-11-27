# YouTube publish pack — Video 03 "Why GPS Would Fail in 2 Minutes Without Einstein"

Updated 2026-11-26 for the v2.4 final (12:45, NO speedup — see note below). **v2.5 update, same day: the video file below is now the v2.5 render — same audio, same timing, same duration 765.28s and same chapters, but the visuals were rebuilt with measured Median fills + face shading + density (see storyboard §v2.5). The filename `video-1080p-fast.mp4` is a misnomer: there is NO speedup in v2.5 (or v2.4).** Paste-ready for the YouTube upload. Do NOT post to the Bug 5h Chiều Facebook page — this is an English YouTube video.

Video file: `~/workspace/median-style-videos/videos/03-gps/video-1080p-fast.mp4` (1920x1080, 765.28s = 12:45, verified by ffprobe 2026-11-26 — this file IS the raw 1.0x render; v2.4 removed the 1.25x speedup entirely, so the audio sounds exactly as in the voice samples)
Thumbnail file: `~/workspace/median-style-videos/videos/03-gps/thumbnail.png` (1280x720, verified — black bg, giant "2 MINUTES", "WITHOUT EINSTEIN" in periwinkle, phone + ticking clock; v2.2 rebuild fills the bottom half with phone + clock + orbit ring + "your maps would lie by 11 km a day")
Voice: Muse TTS avocado_v2 **vd2_quivering_oak** ("voice B", very deep British), English, **speed 80** — chosen by the user 2026-11-26 from 4 samples; measures **116.9 wpm, no speedup** — exactly the pace heard in the samples (v2.3's 1.25x speedup had pushed it to 146 wpm effective and added atempo distortion, which is why the user said the audio sounded rushed and warped unlike the samples).
Script: v2.3, 38 lines, through-line "your phone would lie to you by 11 km a day — unless Einstein saves it". Same script as v2.2 (4 lines re-recorded then for "parts in a million"; line 34 ends with the NTS-2 switch test). Mix normalized toward −14 LUFS (integrated **−15.70 LUFS**, true peak −1.22 dBTP). Animation denser than v2.2: 14 scenes enriched with illustration tied to the narration (scale bars 30 cm vs 3 m and 5–10 m vs 16 m, day-after-day dots, error-over-time timeline, altitude arrow, ON/OFF mini clocks, drifting blue dot in the hook).

Note: the v2.3 pack (10:12, chapters 0:00/0:42/1:57/3:05/4:25/5:45/7:31/9:19) is superseded — v2.4 removed the 1.25x speedup, so use the chapters below, recomputed from the v2.3 `mix.json` raw times (v2.3 fast chapters × 1.25).

## Title (recommended — same as the script title)
Why GPS Would Fail in 2 Minutes Without Einstein

Alternatives if the user wants to test another hook:
- Your Phone Is a Relativity Experiment (And It Runs Every Second)
- GPS Is a Clock, Not a Map — And Einstein Keeps It Honest

## Description (paste as-is)
Your phone finds where you are by measuring time — to billionths of a second. And Einstein's relativity makes satellite clocks drift by 38 microseconds a day. That's 11 km of error a day, 8 metres a minute. So after just 2 minutes, GPS accuracy is already broken — unless engineers pre-correct the clocks before launch.

"Fails in 2 minutes" means the accuracy promise breaks (error ~16 m vs the 5–10 m GPS promises), not a blackout: the map still draws, the dot just drifts to the wrong street.

Chapters:
0:00 Your phone is running a relativity experiment
0:52 GPS is a clock, not a map
2:26 One nanosecond = 30 centimetres
3:51 Speed slows time: −7 µs/day
5:31 Height speeds time up: +45 µs/day
7:11 The net drift: +38 µs/day, 11 km/day
9:23 The fix: build the clock wrong on purpose
11:38 Recap

The numbers: satellites orbit at ~20,200 km, ~3.9 km/s. Special relativity slows their clocks by ~7 µs/day; general relativity speeds them up by ~45 µs/day. Net: +38 µs/day. Engineers set the atomic clocks to 10.22999999543 MHz instead of 10.23 MHz before launch — off by less than 0.005 Hz, exactly the drift Einstein predicted. In 1977, the NTS-2 satellite flew with the correction switchable on/off, and the drift matched the prediction.

Chapter timestamps: the v2.3 fast chapters × 1.25 (= the raw `mix.json` voice_starts), floored to the second, cross-checked against the final duration (765.28s). Chapter starts are lines 1, 4, 9, 13, 18, 23, 29, 36 of the v2.3 script in `kich-ban-storyboard.md`.

## Tags
GPS, relativity, Einstein, special relativity, general relativity, physics, science, atomic clock, satellite, time dilation, Median style, explainer

## Thumbnail
Already made: `thumbnail.png` in the same folder (1280x720, black bg, giant "2 MINUTES", "WITHOUT EINSTEIN" in periwinkle). Upload it as-is — no new thumbnail brief needed.

## Before upload — one decision left for the user
Listen to the voiceover once: the voice is now Quivering Oak (deep British, 116.9 wpm, no speedup) — it sounds exactly like the samples the user picked from. If it sounds right, upload as-is with this pack.
