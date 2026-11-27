#!/usr/bin/env python3
"""Record animation.html to a 1080p mp4 with Playwright, muxed with the voice mix.

Usage:
    python3 scripts/export_video.py videos/02-embedding/animation.html 68.72 videos/02-embedding/audio-full.mp3 videos/02-embedding/video-1080p.mp4

Steps: build a full-bleed export copy of the HTML (title/caption/controls hidden,
stage stretched to 100vw x 100vh), record it in Chromium at 1920x1080 while the
player runs, trim the pre-click lead-in, mux with the audio mix.

The trim is NOT a fixed 1.5s: the click happens (page-load time + 1.5s) after the
recording starts, and page load varies (the 12MB audio preload alone costs
~0.6s). Trimming a fixed 1.5s left the picture lagging the voice by ~0.6s in
video 03 v2.2's first export. So the record script measures the real click
offset and the mux trims exactly that (input seeking on the video before its
`-i`; the audio is not trimmed. NOTE: `-ss` must sit BEFORE the video's `-i` —
between the two `-i`s it would trim the AUDIO instead and leave the video
untrimmed, which is what the first attempt at this fix did in video 03 v2.2).

Requires: playwright + a Chromium build (`python3 -m playwright install chromium`).
The system Hatch Chrome refuses to launch, so use the Playwright Chromium.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def main(html_path: str, total: float, audio_mp3: str, out_mp4: str) -> None:
    html = Path(html_path).read_text(encoding="utf-8")
    export = html.replace(
        "</style>",
        ".wrap{max-width:none;padding:0} h1,.sub,.caption,.controls,.note"
        "{display:none!important} .stage{width:100vw;height:100vh} "
        "body{overflow:hidden} </style>")
    tmpdir = Path(tempfile.mkdtemp(prefix="median-export-"))
    export_html = tmpdir / "export.html"
    export_html.write_text(export, encoding="utf-8")

    rec_script = tmpdir / "record.py"
    rec_script.write_text(f"""
import glob, time
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(args=["--mute-audio", "--no-sandbox"])
    ctx = browser.new_context(viewport={{"width": 1920, "height": 1080}},
                              record_video_dir="{tmpdir}",
                              record_video_size={{"width": 1920, "height": 1080}})
    page = ctx.new_page()
    t0 = time.time()
    page.goto("{export_html.as_uri()}")
    page.wait_for_timeout(1500)
    page.evaluate("document.getElementById('playBtn').click()")
    open("{tmpdir}/click_offset.txt", "w").write(str(time.time() - t0))
    page.wait_for_timeout(int(({total} + 2) * 1000))
    ctx.close()
    browser.close()
print(glob.glob("{tmpdir}/*.webm"))
""", encoding="utf-8")
    subprocess.run([sys.executable, str(rec_script)], check=True)
    webm = next(tmpdir.glob("*.webm"))
    click_offset = float((tmpdir / "click_offset.txt").read_text().strip())
    print(f"click offset measured: {click_offset:.3f}s (trimming exactly this)")
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", "-ss", str(click_offset), "-i", str(webm),
        "-i", audio_mp3, "-t", str(total),
        "-map", "0:v", "-map", "1:a",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20",
        "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out_mp4,
    ], check=True)
    print(f"exported {out_mp4} (1920x1080, {total}s)")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1], float(sys.argv[2]), sys.argv[3], sys.argv[4])
