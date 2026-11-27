#!/usr/bin/env python3
"""Cut 3 vertical Shorts (1080x1920) from the Birthday Paradox video 04 master.
Layout: pure black canvas, 1920x1080 video scaled to 1080x607 centred
(black bars blend into the black background), hook title on top,
burned-in English captions in the black space below the video,
small channel tag at the bottom.
Captions: line text from lines.txt + timing.json, phrase-split with
time distributed proportionally by character count.
Same pipeline as videos/03-gps/shorts/build_shorts.py."""
import json
import os
import re
import subprocess

GOAL = os.path.expanduser("~/workspace/goals/ai-engineer-pivot-combined-learning-roadmap/files")
MASTER = f"{GOAL}/rag-video-04-1080p.mp4"
OUTDIR = f"{GOAL}/rag-video-04-shorts"
MIRROR = os.path.expanduser("~/workspace/median-style-videos/videos/04-birthday/shorts")
os.makedirs(OUTDIR, exist_ok=True)
os.makedirs(MIRROR, exist_ok=True)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

timing = json.load(open(f"{GOAL}/rag-video-04-audio/timing.json"))
starts, durations = timing["starts"], timing["durations"]
lines = open(f"{GOAL}/rag-video-04-audio/lines.txt").read().splitlines()
assert len(lines) == 38 == len(starts) == len(durations), (len(lines), len(starts))

SHORTS = [
    {
        "slug": "short-01-23-people-enough",
        "start": 0.0, "end": 48.56,
        "line_range": (1, 3),  # 1-indexed inclusive
        "title": "23 people is\nenough",
    },
    {
        "slug": "short-02-253-pairs",
        "start": 126.176, "end": 172.856,
        "line_range": (9, 11),
        "title": "253 pairs,\nnot 23 people",
    },
    {
        "slug": "short-03-366-certain",
        "start": 515.384, "end": 561.632,
        "line_range": (33, 34),
        "title": "366 people.\nA match, guaranteed",
    },
]


def split_phrases(text, max_chars=42):
    """Split a spoken line into caption chunks at punctuation."""
    parts = re.split(r"(?<=[,.;:?!—])\s+", text)
    chunks, cur = [], ""
    for p in parts:
        if not cur:
            cur = p
        elif len(cur) + 1 + len(p) <= max_chars:
            cur += " " + p
        else:
            chunks.append(cur)
            cur = p
    if cur:
        chunks.append(cur)
    # merge tiny trailing chunks
    out = []
    for c in chunks:
        if out and len(c) < 12:
            out[-1] += " " + c
        else:
            out.append(c)
    return out


def fmt_ass_time(t):
    t = max(0.0, t)
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def build_ass(short, path):
    lo, hi = short["line_range"]
    events = []
    for li in range(lo, hi + 1):
        text = lines[li - 1]
        ls, ld = starts[li - 1], durations[li - 1]
        chunks = split_phrases(text)
        total_chars = sum(len(c) for c in chunks)
        t = ls
        for c in chunks:
            d = ld * len(c) / total_chars
            events.append((t - short["start"], t + d - short["start"], c))
            t += d
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,DejaVu Sans,52,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,2,0,2,60,60,360,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with open(path, "w") as f:
        f.write(header)
        for s, e, c in events:
            f.write(f"Dialogue: 0,{fmt_ass_time(s)},{fmt_ass_time(e)},Default,,0,0,0,,{c}\n")
    return len(events)


def build_short(short):
    slug = short["slug"]
    dur = short["end"] - short["start"]
    ass_path = f"{OUTDIR}/{slug}.ass"
    title_path = f"{OUTDIR}/{slug}-title.txt"
    n_ev = build_ass(short, ass_path)
    with open(title_path, "w") as f:
        f.write(short["title"])
    out = f"{OUTDIR}/{slug}.mp4"
    vf = (
        "scale=1080:607,pad=1080:1920:0:656:black,"
        f"subtitles='{ass_path}',"
        f"drawtext=fontfile={BOLD}:textfile='{title_path}':fontsize=66:fontcolor=white:x=(w-text_w)/2:y=230,"
        f"drawtext=fontfile={REG}:text='The Maths Inside':fontsize=40:fontcolor=0x9A9A9A:x=(w-text_w)/2:y=1830"
    )
    cmd = [
        "ffmpeg", "-y", "-v", "error",
        "-ss", str(short["start"]), "-t", f"{dur:.3f}", "-i", MASTER,
        "-vf", vf,
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p", "-r", "25",
        "-c:a", "aac", "-b:a", "160k",
        "-movflags", "+faststart", out,
    ]
    subprocess.run(cmd, check=True)
    print(f"{slug}: {dur:.1f}s, {n_ev} caption events -> {out}")
    return out


for s in SHORTS:
    build_short(s)
print("done")
