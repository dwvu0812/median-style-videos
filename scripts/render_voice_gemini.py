#!/usr/bin/env python3
"""Render spoken lines to mp3 with Gemini TTS (Charon) and print measured timing.

Usage:
    python3 render_voice_gemini.py <lines.txt> <outdir> [--only N] [--start N]

Reads one spoken line per line. Writes vo-NN.mp3 into the output dir, then
prints durations and the suggested scene starts (first line at 0.8s, 1.2s
pause after each line) as JSON — copy those numbers into the animation.html
scenes[] array and into mix.json.

Voice: Charon (calm, low, measured male — the Median narration register),
model gemini-2.5-flash-preview-tts via the custom.gemini credential. The API
returns base64 PCM 16-bit 24000Hz mono; ffmpeg converts it to mp3.

On a 429, waits ~65s and retries that line only (up to 3 tries).
"""
import argparse
import base64
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

BASE = "https://generativelanguage.googleapis.com/v1beta"
MODEL = "gemini-2.5-flash-preview-tts"
VOICE = "Charon"
ALLOWED = ["generativelanguage.googleapis.com"]
LEAD = 0.8
GAP = 1.2


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        raise RuntimeError("redirect refused, verify the endpoint")


def tts_pcm(text: str) -> bytes:
    body = {
        "contents": [{"parts": [{"text": text}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {
                "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": VOICE}}
            },
        },
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE}/models/{MODEL}:generateContent", data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    add_surrogate_to_request(req, "custom.gemini", allowed_hosts=ALLOWED)
    with urllib.request.build_opener(NoRedirect()).open(req, timeout=120) as resp:
        result = read_json_response(resp)
    parts = result["candidates"][0]["content"]["parts"]
    for p in parts:
        if "inlineData" in p:
            return base64.b64decode(p["inlineData"]["data"])
    raise RuntimeError(f"no audio in response: {json.dumps(result)[:400]}")


def render_line(text: str, target: Path) -> None:
    last_exc = None
    for attempt in range(1, 7):
        try:
            pcm = tts_pcm(text)
            break
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")[:300]
            print(f"  HTTP {e.code} (attempt {attempt}): {body}", file=sys.stderr)
            last_exc = e
            if e.code == 429 and attempt < 6:
                print("  429 — waiting 180s before retry", file=sys.stderr)
                time.sleep(180)
                continue
            raise
        except Exception as e:
            last_exc = e
            if attempt < 3:
                print(f"  error (attempt {attempt}): {e} — retrying in 10s",
                      file=sys.stderr)
                time.sleep(10)
                continue
            raise
    else:
        raise last_exc
    raw = target.with_suffix(".pcm")
    raw.write_bytes(pcm)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-f", "s16le", "-ar", "24000",
         "-ac", "1", "-i", str(raw), "-c:a", "libmp3lame", "-b:a", "160k",
         str(target)], check=True)
    raw.unlink()


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
    ap.add_argument("--only", type=int, default=None, help="render only line N")
    ap.add_argument("--start", type=int, default=1, help="start at line N")
    args = ap.parse_args()

    lines = [ln.strip() for ln in Path(args.lines_file).read_text(encoding="utf-8")
             .splitlines() if ln.strip()]
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    if args.only is not None:
        idxs = [args.only]
    else:
        idxs = list(range(args.start, len(lines) + 1))

    durations = {}
    for i in idxs:
        target = out / f"vo-{i:02d}.mp3"
        if target.exists() and args.only is None:
            print(f"line {i}: exists, skipping")
            durations[i] = round(duration(target), 3)
            continue
        print(f"line {i}/{len(lines)} ({len(lines[i-1].split())} words)...",
              flush=True)
        render_line(lines[i - 1], target)
        durations[i] = round(duration(target), 3)
        print(f"  -> {durations[i]}s")
        time.sleep(60)  # free-tier TTS is RPM-limited; shorter spacing caused repeated 429s

    if args.only is None:
        # measure any pre-existing files not rendered this run
        for i in range(1, len(lines) + 1):
            if i not in durations:
                p = out / f"vo-{i:02d}.mp3"
                if p.exists():
                    durations[i] = round(duration(p), 3)
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
