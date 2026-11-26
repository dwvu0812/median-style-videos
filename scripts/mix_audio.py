#!/usr/bin/env python3
"""Mix per-line voice clips + SFX + ambient pad into one full audio mix.

Usage:
    python3 scripts/mix_audio.py videos/02-embedding/audio/ videos/02-embedding/mix.json assets/sfx/ videos/02-embedding/audio-full.mp3

mix.json shape:
    {"voice_starts": [0.8, 5.408, ...],            # seconds, one per vo-NN.mp3
     "sfx": [{"file": "sfx-whoosh.wav", "at": 1.5}, ...],
     "total": 68.72}

The mix places each voice clip with adelay at its start, SFX at their motion
points, and a very low ambient pad (sine 110Hz + 165Hz) underneath, then
normalises peak to -4.5 dB. Output is mp3 160k.
"""
import json
import subprocess
import sys
from pathlib import Path


def run(cmd):
    subprocess.run(cmd, check=True)


def main(audio_dir: str, mix_file: str, sfx_dir: str, out_mp3: str) -> None:
    cfg = json.loads(Path(mix_file).read_text(encoding="utf-8"))
    audio = Path(audio_dir)
    sfx = Path(sfx_dir)
    total = float(cfg["total"])

    inputs = []   # (path, delay_ms or None)
    for i, start in enumerate(cfg["voice_starts"], 1):
        inputs.append((audio / f"vo-{i:02d}.mp3", int(round(float(start) * 1000))))
    sfx_inputs = []
    for ev in cfg.get("sfx", []):
        sfx_inputs.append((sfx / ev["file"], int(round(float(ev["at"]) * 1000))))
    inputs += sfx_inputs

    cmd = ["ffmpeg", "-y", "-v", "error"]
    for path, _ in inputs:
        cmd += ["-i", str(path)]

    filt = []
    labels = []
    for idx, (_, delay) in enumerate(inputs):
        filt.append(f"[{idx}:a]adelay={delay}|{delay}[a{idx}]")
        labels.append(f"[a{idx}]")
    n = len(inputs)
    filt.append(f"sine=frequency=110:duration={total},volume=0.03[p1]")
    filt.append(f"sine=frequency=165:duration={total},volume=0.03[p2]")
    filt.append("[p1][p2]amix=inputs=2:normalize=0[pad]")
    labels.append("[pad]")
    filt.append(f"{''.join(labels)}amix=inputs={n + 1}:normalize=0[out]")

    raw = Path(out_mp3).with_suffix(".raw.wav")
    run(cmd + ["-filter_complex", ";".join(filt), "-map", "[out]",
               "-t", str(total), "-c:a", "pcm_s16le", str(raw)])

    probe = subprocess.run(
        ["ffmpeg", "-i", str(raw), "-af", "volumedetect", "-vn", "-sn", "-dn",
         "-f", "null", "/dev/null"],
        capture_output=True, text=True)
    maxv = None
    for line in probe.stderr.splitlines():
        if "max_volume" in line:
            maxv = float(line.split("max_volume:")[1].split("dB")[0].strip())
    gain = -4.5 - (maxv if maxv is not None else 0.0)
    run(["ffmpeg", "-y", "-v", "error", "-i", str(raw),
         "-af", f"volume={gain:.2f}dB",
         "-c:a", "libmp3lame", "-b:a", "160k", out_mp3])
    raw.unlink()
    print(f"mixed {out_mp3} ({total}s, peak normalised to -4.5 dB)")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
