# YouTube publish pack — Video 03 "Why GPS Would Fail in 2 Minutes Without Einstein"

Updated 2026-11-26 ~15:25 local for the v2.0 final (8:13, 1.25x). Paste-ready for the YouTube upload. Do NOT post to the Bug 5h Chiều Facebook page — this is an English YouTube video.

Video file: `~/workspace/median-style-videos/videos/03-gps/video-1080p-fast.mp4` (1920x1080, 493.44s = 8:13, verified by ffprobe 2026-11-26; raw `video-1080p.mp4` is 616.72s = 10:17)
Thumbnail file: `~/workspace/median-style-videos/videos/03-gps/thumbnail.png` (1280x720, verified — black bg, giant "2 MINUTES", "WITHOUT EINSTEIN" in periwinkle, phone + ticking clock)
Voice: Muse TTS avocado_v2, English, speed 105 — Vietnamese accent, accepted by the user on 2026-11-26 for speed over a native accent.
Script: v2.0, 38 lines, 1,479 words, through-line "your phone would lie to you by 11 km a day — unless Einstein saves it".

Note: a v2.1 motion-smoothing re-export was requested by the user at 15:23 local 2026-11-26 and was being rendered in the side chat. It keeps the same script, voice and audio, so these chapters and this pack still apply to it — just use the newest `video-1080p-fast.mp4` when it lands. The old v1.0 pack (10:49, chapters 0:00/0:48/2:09/3:15/4:59/6:28/8:09/10:03) is superseded — do NOT use those timestamps.

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
0:34 GPS is a clock, not a map
1:35 One nanosecond = 30 centimetres
2:29 Speed slows time: −7 µs/day
3:34 Height speeds time up: +45 µs/day
4:55 The net drift: +38 µs/day, 11 km/day
6:06 The fix: build the clock wrong on purpose
7:33 Recap

The numbers: satellites orbit at ~20,200 km, ~3.9 km/s. Special relativity slows their clocks by ~7 µs/day; general relativity speeds them up by ~45 µs/day. Net: +38 µs/day. Engineers set the atomic clocks to 10.22999999543 MHz instead of 10.23 MHz before launch — off by less than 0.005 Hz, exactly the drift Einstein predicted. In 1977, the NTS-2 satellite flew with the correction switchable on/off, and the drift matched the prediction.

Chapter timestamps: computed from `mix.json` voice_starts (raw) divided by 1.25, floored to the second, and cross-checked against the fast file's real duration (493.44s). Chapter starts are lines 1, 4, 9, 13, 18, 23, 29, 36 of the v2.0 script in `kich-ban-storyboard.md`.

## Tags
GPS, relativity, Einstein, special relativity, general relativity, physics, science, atomic clock, satellite, time dilation, Median style, explainer

## Thumbnail
Already made: `thumbnail.png` in the same folder (1280x720, black bg, giant "2 MINUTES", "WITHOUT EINSTEIN" in periwinkle). Upload it as-is — no new thumbnail brief needed.

## Before upload — one decision left for the user
Listen to the voiceover once: if the Muse voice (Vietnamese-accented English) is acceptable, upload as-is with this pack. If not, the only fix is re-recording the 38 lines with another voice — the animation, mix and export would then need re-running.
