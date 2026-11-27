#!/usr/bin/env python3
"""Build mix.json for video 03 from the voice timing JSON.

Usage:
    python3 build_mix_03.py <timing.json> <out mix.json>

SFX map comes from the storyboard's per-scene sound triggers.
SFX are placed at scene start + 0.7s (motion onset); chimes at +1.5s
(they land on the number/equation reveal).
"""
import json
import sys

# scene number -> sfx file (from rag-video-03-kich-ban-storyboard.md)
SFX = {
    1: "sfx-whoosh.wav", 2: "sfx-thud.wav", 3: "sfx-pop.wav",
    4: "sfx-whoosh.wav", 5: "sfx-pop.wav", 6: "sfx-tick.wav",
    7: "sfx-pop.wav", 8: "sfx-tick.wav", 9: "sfx-whoosh.wav",
    10: "sfx-tick.wav", 11: "sfx-tick.wav", 12: "sfx-thud.wav",
    13: "sfx-whoosh.wav", 14: "sfx-pop.wav", 15: "sfx-tick.wav",
    16: "sfx-tick.wav", 17: "sfx-pop.wav", 18: "sfx-whoosh.wav",
    19: "sfx-pop.wav", 20: "sfx-tick.wav", 21: "sfx-tick.wav",
    22: "sfx-thud.wav", 23: "sfx-chime.wav", 24: "sfx-tick.wav",
    25: "sfx-tick.wav", 26: "sfx-tick.wav", 27: "sfx-thud.wav",
    28: "sfx-pop.wav", 29: "sfx-whoosh.wav", 30: "sfx-tick.wav",
    31: "sfx-chime.wav", 32: "sfx-pop.wav", 33: "sfx-pop.wav",
    34: "sfx-tick.wav", 35: "sfx-chime.wav", 36: "sfx-whoosh.wav",
    37: "sfx-chime.wav", 38: "sfx-chime.wav",
}


def main():
    timing = json.loads(open(sys.argv[1]).read())
    starts = timing["starts"]
    assert len(starts) == 38
    sfx = []
    for i, start in enumerate(starts, 1):
        f = SFX[i]
        offset = 1.5 if f == "sfx-chime.wav" else 0.7
        sfx.append({"file": f, "at": round(start + offset, 3)})
    cfg = {"voice_starts": starts, "sfx": sfx, "total": timing["total"]}
    open(sys.argv[2], "w").write(json.dumps(cfg, indent=2))
    print(f"wrote {sys.argv[2]} (total={timing['total']}s, {len(sfx)} sfx events)")


if __name__ == "__main__":
    main()
