#!/usr/bin/env python3
"""Render all spoken lines with ElevenLabs Magnus (deep British narrator).

Usage:
    python3 render_voice_elevenlabs.py <lines.txt> <outdir> [--start N]

One creative_generate_speech call per line (generations_count=1), all on the
same flow so the takes stay together. Polls the flow run until completed,
downloads the mp3 to vo-NN.mp3, measures duration with ffprobe, and prints
a timing JSON (starts with 0.8s lead, 1.2s gaps) at the end.

Stops (no retry) on any failed generation — a retry would charge a second
generation. Inspect the flow with creative_get_flow before re-running.
Skips lines whose vo-NN.mp3 already exists.
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

FLOW_ID = "nL2BYqFG68Q6m9Rj7uvg"
VOICE_ID = "EhNmn5gmtSM4VHNQgBt4"
MODEL_ID = "eleven_v4"
CLI = "/opt/hatch/bin/elevenlabs-connector-cli"
LEAD = 0.8
GAP = 1.2


def cli_json(cmd, args, outfile):
    full = [CLI, cmd, "--arguments-json", json.dumps(args),
            "--json-output-file", str(outfile)]
    r = subprocess.run(full, capture_output=True, text=True, timeout=1500)
    if r.returncode != 0:
        raise RuntimeError(f"{cmd} failed rc={r.returncode}: {r.stdout[-500:]} {r.stderr[-500:]}")
    return json.loads(Path(outfile).read_text())


def generate_line(text: str, line_no: int, tmpdir: Path):
    args = {
        "context": f"Generate narration line {line_no} of 38 for a science explainer video about GPS and relativity.",
        "prompt": text,
        "voice_id": VOICE_ID,
        "model_id": MODEL_ID,
        "generations_count": 1,
        "flow_id": FLOW_ID,
    }
    out = tmpdir / f"gen_{line_no:02d}.json"
    res = cli_json("creative_generate_speech", args, out)
    sc = res["structuredContent"]
    session_ids = sc["session_ids"]
    # poll until completed
    for _ in range(30):
        time.sleep(5)
        st = cli_json("creative_get_flow_run_status",
                      {"context": f"Poll narration line {line_no}.",
                       "flow_id": FLOW_ID, "session_ids": session_ids},
                      tmpdir / f"status_{line_no:02d}.json")
        ssc = st["structuredContent"]
        if ssc.get("has_failures"):
            raise RuntimeError(f"line {line_no}: generation failed: {json.dumps(ssc)[:500]}")
        if ssc.get("all_completed"):
            gens = ssc["generations"]
            assert len(gens) == 1, gens
            return gens[0]["content_url"], gens[0].get("duration_secs")
    raise RuntimeError(f"line {line_no}: timed out waiting for completion")


def duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lines_file")
    ap.add_argument("outdir")
    ap.add_argument("--start", type=int, default=1)
    args = ap.parse_args()

    lines = [ln.strip() for ln in Path(args.lines_file).read_text(encoding="utf-8")
             .splitlines() if ln.strip()]
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)
    tmpdir = out / ".el_tmp"
    tmpdir.mkdir(exist_ok=True)

    durations = {}
    for i in range(args.start, len(lines) + 1):
        target = out / f"vo-{i:02d}.mp3"
        if target.exists():
            print(f"line {i}: exists, skipping", flush=True)
            durations[i] = round(duration(target), 3)
            continue
        print(f"line {i}/{len(lines)} ({len(lines[i-1].split())} words)...", flush=True)
        url, dur_api = generate_line(lines[i - 1], i, tmpdir)
        urllib.request.urlretrieve(url, str(target))
        durations[i] = round(duration(target), 3)
        print(f"  -> {durations[i]}s (api said {dur_api}s)", flush=True)
        time.sleep(3)

    starts, t = [], LEAD
    ds = []
    for i in range(1, len(lines) + 1):
        starts.append(round(t, 3))
        ds.append(durations[i])
        t += durations[i] + GAP
    total = round(starts[-1] + durations[len(lines)], 3)
    print(json.dumps({"durations": ds, "starts": starts,
                      "total": total}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
