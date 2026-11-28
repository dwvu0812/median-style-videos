#!/usr/bin/env python3
"""Frame-diff meter v3 — the audit's method PLUS the corrected separators
from the famous-channels research (report §0):
- legacy scale 320x180 (comparable with the audit / v2 numbers)
- native-aspect scale (180x320 for 9:16 vertical, 320x180 for 16:9) —
  no axis squash. The legacy 320x180 downscale squashes the vertical
  axis 10.7x on a 1080x1920 frame, so thin horizontal motion can read
  as frozen even when the eye follows it.
- median / mean / max (BURST SIZE — winners 28-83, ours was 6-16)
- near-frozen seconds at BOTH thresholds: <0.2 (research definition)
  and <0.5 (v2 definition)
- first-5 s median (Shorts hook window) and first-60 s near-frozen %
Usage: python3 measure_framediff.py <video.mp4> [duration_seconds]
"""
import sys, subprocess, statistics
from pathlib import Path
import numpy as np
from PIL import Image

VIDEO = Path(sys.argv[1])
TOTAL = float(sys.argv[2]) if len(sys.argv) > 2 else None
TMP = Path("/tmp") / ("framediff3_" + VIDEO.stem)

def ffprobe_dur(path):
    r = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(path)], capture_output=True, text=True, check=True)
    return float(r.stdout.strip())

def probe_wh(path):
    r = subprocess.run(["ffprobe", "-v", "quiet", "-select_streams", "v:0",
                        "-show_entries", "stream=width,height", "-of", "csv=p=0",
                        str(path)], capture_output=True, text=True, check=True)
    w, h = r.stdout.strip().split(",")
    return int(w), int(h)

if TOTAL is None:
    TOTAL = ffprobe_dur(VIDEO)
W, H = probe_wh(VIDEO)
vertical = H > W
# Native aspect at ~same pixel count as the legacy 320x180 (57,600 px):
# vertical 1080x1920 -> 180x320; horizontal -> 320x180.
native = "180:320" if vertical else "320:180"

def deltas_for(scale):
    d = TMP / scale.replace(":", "x")
    d.mkdir(parents=True, exist_ok=True)
    # Select by FRAME NUMBER (every 25th frame), not by timestamp: the
    # fps=1 filter rounds timestamps and can emit the SAME frame twice
    # (v3 measured 0.01/0.02 for t4->t5 and t7->t8 that way, while a direct
    # -ss comparison of the same intervals is 0.28) — a duplicate reads as
    # a frozen second that does not exist in the video. -vsync 0 keeps the
    # selected frames 1:1. Assumes 25 fps input (our exports are 25 fps).
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(VIDEO),
                    "-vf", f"select='not(mod(n,25))',scale={scale}",
                    "-vsync", "0", str(d / "f%04d.png")], check=True)
    frames = sorted(d.glob("f*.png"))
    prev, deltas = None, []
    for f in frames:
        g = np.asarray(Image.open(f).convert("L"), dtype=np.float32)
        if prev is not None:
            deltas.append(float(np.mean(np.abs(g - prev))))
        prev = g
    for f in frames:
        f.unlink()
    d.rmdir()
    return deltas

def report(label, deltas):
    n = len(deltas)
    med = statistics.median(deltas)
    mean = statistics.mean(deltas)
    mx = max(deltas)
    f02 = sum(1 for v in deltas if v < 0.2)
    f05 = sum(1 for v in deltas if v < 0.5)
    first5 = statistics.median(deltas[:5]) if n >= 5 else med
    first60 = deltas[:60]
    f60 = sum(1 for v in first60 if v < 0.2) / max(1, len(first60)) * 100
    print(f"[{label}] median {med:.2f}  mean {mean:.2f}  max (burst) {mx:.2f}")
    print(f"[{label}] near-frozen <0.2: {f02}/{n} = {100*f02/n:.1f}%  |  <0.5: {f05}/{n} = {100*f05/n:.1f}%")
    print(f"[{label}] first-5 s median {first5:.2f}  |  first-60 s near-frozen (<0.2) {f60:.1f}%")
    return {"median": med, "mean": mean, "max": mx,
            "frozen02": 100*f02/n, "frozen05": 100*f05/n,
            "first5": first5, "first60_frozen02": f60}

TMP.mkdir(parents=True, exist_ok=True)
print(f"video: {VIDEO}  {W}x{H}  duration: {TOTAL:.2f}s")
legacy = report("legacy 320x180", deltas_for("320:180"))
nat = report(f"native {native}", deltas_for(native))
TMP.rmdir()
print("bars (research §0, corrected): hook-window near-frozen (<0.2) <= 10%; "
      "burst size (max) >= 25; hook density >= 6 events/60s (check_density.py); "
      "median frame-diff is SCREENING only (>= 1.5 passes the screen).")
