#!/usr/bin/env python3
"""Build the video 04 mix: voice lines at measured starts + SFX + pad,
then loudnorm two-pass toward -14 LUFS (TP <= -1 dBTP), per SKILL.md §2c.

Usage: python3 build_mix.py
Reads timing.json in the 04 audio dir, writes mix.json and
rag-video-04-full-audio.mp3, prints the measured loudness of the result.
"""
import json
import re
import subprocess
from pathlib import Path

AUDIO = Path("/home/hatch/workspace/goals/ai-engineer-pivot-combined-learning-roadmap/files/rag-video-04-audio")
SFX_DIR = Path("/home/hatch/workspace/goals/ai-engineer-pivot-combined-learning-roadmap/files/rag-video-01-audio")

# scene number -> sfx file (from the storyboard's per-scene sound triggers)
SFX = {
    1: "sfx-whoosh.wav", 2: "sfx-pop.wav", 3: "sfx-pop.wav",
    4: "sfx-thud.wav", 5: "sfx-pop.wav", 6: "sfx-tick.wav",
    7: "sfx-pop.wav", 8: "sfx-tick.wav", 9: "sfx-whoosh.wav",
    10: "sfx-tick.wav", 11: "sfx-pop.wav", 12: "sfx-tick.wav",
    13: "sfx-whoosh.wav", 14: "sfx-tick.wav", 15: "sfx-tick.wav",
    16: "sfx-whoosh.wav", 17: "sfx-thud.wav", 18: "sfx-chime.wav",
    19: "sfx-pop.wav", 20: "sfx-thud.wav", 21: "sfx-tick.wav",
    22: "sfx-tick.wav", 23: "sfx-tick.wav", 24: "sfx-pop.wav",
    25: "sfx-whoosh.wav", 26: "sfx-pop.wav", 27: "sfx-tick.wav",
    28: "sfx-pop.wav", 29: "sfx-whoosh.wav", 30: "sfx-pop.wav",
    31: "sfx-tick.wav", 32: "sfx-pop.wav", 33: "sfx-thud.wav",
    34: "sfx-pop.wav", 35: "sfx-chime.wav", 36: "sfx-whoosh.wav",
    37: "sfx-chime.wav", 38: "sfx-chime.wav",
}


def run(cmd):
    subprocess.run(cmd, check=True)


def main():
    timing = json.loads((AUDIO / "timing.json").read_text())
    starts, total = timing["starts"], timing["total"]
    assert len(starts) == 38
    sfx = []
    for i, start in enumerate(starts, 1):
        f = SFX[i]
        offset = 1.5 if f == "sfx-chime.wav" else 0.7
        sfx.append({"file": f, "at": round(start + offset, 3)})
    cfg = {"voice_starts": starts, "sfx": sfx, "total": total}
    (AUDIO / "mix.json").write_text(json.dumps(cfg, indent=2))
    print(f"mix.json written (total={total}s, {len(sfx)} sfx events)")

    inputs = [(AUDIO / f"vo-{i:02d}.mp3", int(round(s * 1000)))
              for i, s in enumerate(starts, 1)]
    inputs += [(SFX_DIR / ev["file"], int(round(ev["at"] * 1000))) for ev in sfx]

    cmd = ["ffmpeg", "-y", "-v", "error"]
    for path, _ in inputs:
        cmd += ["-i", str(path)]
    filt, labels = [], []
    for idx, (_, delay) in enumerate(inputs):
        filt.append(f"[{idx}:a]adelay={delay}|{delay}[a{idx}]")
        labels.append(f"[a{idx}]")
    n = len(inputs)
    filt.append(f"sine=frequency=110:duration={total},volume=0.06[p1]")
    filt.append(f"sine=frequency=165:duration={total},volume=0.06[p2]")
    filt.append("[p1][p2]amix=inputs=2:normalize=0[pad]")
    labels.append("[pad]")
    filt.append(f"{''.join(labels)}amix=inputs={n + 1}:normalize=0[out]")

    raw = AUDIO / "rag-video-04-full-audio.raw.wav"
    run(cmd + ["-filter_complex", ";".join(filt), "-map", "[out]",
               "-t", str(total), "-c:a", "pcm_s16le", str(raw)])
    print("raw mix built:", raw)

    # loudnorm pass 1: measure
    probe = subprocess.run(
        ["ffmpeg", "-i", str(raw), "-af",
         "loudnorm=I=-14:TP=-1.0:LRA=11:print_format=json",
         "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"\{[^}]*\}", probe.stderr)
    measured = json.loads(m.group(0))
    print("loudnorm measured:", {k: measured[k] for k in
          ("input_i", "input_tp", "input_lra", "input_thresh", "target_offset")})

    out_mp3 = AUDIO / "rag-video-04-full-audio.mp3"
    ln = ("loudnorm=I=-14:TP=-1.0:LRA=11"
          f":measured_I={measured['input_i']}"
          f":measured_TP={measured['input_tp']}"
          f":measured_LRA={measured['input_lra']}"
          f":measured_thresh={measured['input_thresh']}"
          f":offset={measured['target_offset']}:linear=true")
    run(["ffmpeg", "-y", "-v", "error", "-i", str(raw), "-af", ln,
         "-c:a", "libmp3lame", "-b:a", "160k", str(out_mp3)])
    raw.unlink()

    # verify the result
    probe2 = subprocess.run(
        ["ffmpeg", "-i", str(out_mp3), "-af",
         "loudnorm=I=-14:TP=-1.0:LRA=11:print_format=json",
         "-f", "null", "-"], capture_output=True, text=True)
    m2 = re.search(r"\{[^}]*\}", probe2.stderr)
    v = json.loads(m2.group(0))
    print("RESULT:", out_mp3, "integrated:", v["input_i"], "LUFS, TP:",
          v["input_tp"], "dBTP, LRA:", v["input_lra"])
    dur = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(out_mp3)],
        capture_output=True, text=True, check=True).stdout.strip())
    print("mix duration:", round(dur, 3), "s (target total:", total, ")")


if __name__ == "__main__":
    main()
