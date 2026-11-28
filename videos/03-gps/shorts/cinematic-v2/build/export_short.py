#!/usr/bin/env python3
"""Export the cinematic-v2 vertical Short via Playwright (video only), then
trim the measured click offset and mux with the reused audio.
Adapted from ~/workspace/median-style-videos/scripts/export_video.py.
Usage: python3 export_short.py [html_path] [audio_path] [out_path]
Defaults: build/short-01-cinematic-v2.html, ../audio.m4a, ../short-01-11km-a-day-cinematic-v2.mp4
"""
import sys, os, time, subprocess, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
HTML = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "short-01-cinematic-v2.html"
AUDIO = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE.parent / "audio.m4a"
OUT = Path(sys.argv[3]) if len(sys.argv) > 3 else HERE.parent / "short-01-11km-a-day-cinematic-v2.mp4"
TOTAL = 47.568  # seconds (line 23 + line 24 + the 1.2s gap inside beat 3)

from playwright.sync_api import sync_playwright

raw_path = HERE / "raw_video.mp4"
with sync_playwright() as p:
    browser = p.chromium.launch(args=["--mute-audio", "--autoplay-policy=no-user-gesture-required"])
    ctx = browser.new_context(viewport={"width": 1080, "height": 1920},
                              record_video_dir=str(HERE), record_video_size={"width": 1080, "height": 1920})
    page = ctx.new_page()
    t0 = time.time()
    page.goto("file://" + str(HTML) + "#export")
    # 2.0s: let Beat 1's entrance settle BEFORE the click, so frame 1 of
    # the export is the full composition (chips in, "= 0 µs/day", scale).
    # The click offset is measured and trimmed, so this wait costs no
    # video time — it only guarantees the first frame is not black.
    page.wait_for_timeout(2000)
    page.evaluate("document.querySelector('#playBtn').click()")
    click_offset = time.time() - t0
    print(f"click offset measured: {click_offset:.3f}s", flush=True)
    page.wait_for_timeout((TOTAL + 2.0) * 1000)
    video_path = page.video.path()
    ctx.close()
    browser.close()

print(f"raw video: {video_path}", flush=True)
os.rename(video_path, raw_path)

# Trim the measured click offset (-ss BEFORE the video's -i) and mux audio.
cmd = [
    "ffmpeg", "-y",
    "-ss", f"{click_offset:.3f}", "-i", str(raw_path),
    "-i", str(AUDIO),
    "-t", str(TOTAL),
    "-map", "0:v", "-map", "1:a",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20",
    "-c:a", "aac", "-b:a", "160k",
    "-movflags", "+faststart",
    str(OUT),
]
print(" ".join(cmd), flush=True)
subprocess.run(cmd, check=True)
raw_path.unlink()
print(f"done: {OUT}", flush=True)
print(json.dumps({"click_offset": round(click_offset, 3), "total": TOTAL, "out": str(OUT)}))
