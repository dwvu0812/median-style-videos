#!/usr/bin/env python3
"""Render spoken lines to mp3 with Muse TTS (voice A) and print measured timing.

Usage:
    python3 scripts/render_voice.py videos/02-embedding/lines.txt videos/02-embedding/audio/

Reads one spoken line per line (already spelled out for speech: "năm trăm ký tự",
"quý ba", "ba mảnh" — never digits or symbols like f(x)). Writes vo-01.mp3 ...
into the output dir, then prints durations and the suggested scene starts
(first line at 0.8s, 1.2s pause after each line) as JSON — copy those numbers
into the animation.html scenes[] array and into mix.json.

Voice: avocado_v2:vd2_smoky_teacup (Vietnamese male, mid-range, clear/crisp),
speed 90. Requires the `tts` CLI on PATH.
"""
import json
import subprocess
import sys
from pathlib import Path

VOICE = "avocado_v2:vd2_smoky_teacup"
SPEED = 90
LEAD = 0.8
GAP = 1.2


def duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def main(lines_file: str, outdir: str) -> None:
    lines = [ln.strip() for ln in Path(lines_file).read_text(encoding="utf-8")
             .splitlines() if ln.strip()]
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)

    durations = []
    for i, line in enumerate(lines, 1):
        target = out / f"vo-{i:02d}.mp3"
        subprocess.run(
            ["tts", "--text", line, "--voice", VOICE,
             "--speed", str(SPEED), "--output", str(target)],
            check=True)
        durations.append(round(duration(target), 3))

    starts, t = [], LEAD
    for d in durations:
        starts.append(round(t, 3))
        t += d + GAP
    total = round(starts[-1] + durations[-1], 3)
    print(json.dumps({"durations": durations, "starts": starts,
                      "total": total}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
