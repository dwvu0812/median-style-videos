#!/usr/bin/env python3
"""Hook-density pre-export check (research §5.7, 2026-11-28).

Parses an animation HTML (long-form player or vertical Short player) and
FAILS the build loudly unless the winners' hook-density bars are met:
  1. first-60 s visual events >= 6 (Animated Math / 3B1B-Transformers have
     7 visual discontinuities in the 25-35 s window alone; ours had ~1
     scene swap per 13-19 s and nothing new inside a scene after ~3.4 s).
  2. no scene >= 12 s has < 4 events (a new element every 2-4 s through
     the WHOLE scene — the build clock, not just the entrance).
  3. the payoff is SPOKEN by 5 s (--payoff regex, e.g. "thirty-eight|38";
     without it, the first number word/digit in the captions must land
     by 5 s — the weak form of the check).

An "event" = a scene/beat start + every entry in that scene's events[]
(build clock) + every data-count counter + every <animateMotion> +
every .write element inside the scene's group. Events[] is the
authoritative build clock: declare ALL timed build events there
(counter starts, morph triggers, dot arrivals, SFX), not only in CSS.

Usage:
  python3 check_density.py <animation.html> [--lines lines.txt]
                             [--payoff "thirty-eight|38"]
Exit code 0 = PASS, 1 = FAIL. Run before export, not after.
"""
import sys, re, argparse
from pathlib import Path

NUMBER_WORDS = (
    r"zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|"
    r"thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|"
    r"million|billion"
)
NUM_RE = re.compile(r"\d|\b(?:" + NUMBER_WORDS + r")\b", re.I)

def parse_scenes(html):
    """Return list of {id, t0, dur, events:[{t,...}]} from BEATS[] or scenes[]."""
    # Find the BEATS/scenes array literal (non-greedy to the closing "];").
    m = re.search(r"(?:const\s+)?(?:BEATS|scenes)\s*=\s*\[(.*?)\n\];", html, re.S)
    if not m:
        return []
    body = m.group(1)
    scenes = []
    # Scan top-level objects with balanced braces (objects contain nested
    # events:[{t:..}] arrays, so a flat \{[^{}]*\} regex would miss them).
    i = 0
    while i < len(body):
        if body[i] != "{":
            i += 1
            continue
        depth, j = 0, i
        in_str = None
        while j < len(body):
            c = body[j]
            if in_str:
                if c == in_str and body[j - 1] != "\\":
                    in_str = None
            elif c in "\"'":
                in_str = c
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        obj = body[i:j + 1]
        i = j + 1
        t0 = re.search(r"t0\s*:\s*([0-9.]+)", obj)
        dur = re.search(r"dur\s*:\s*([0-9.]+)", obj)
        if not t0 or not dur:
            continue
        # Count event entries: {t: ...} objects inside the events:[...] list.
        evm = re.search(r"events\s*:\s*\[(.*?)\]", obj, re.S)
        nev = len(re.findall(r"\{\s*t\s*:", evm.group(1))) if evm else 0
        sid = re.search(r"id\s*:\s*'([^']+)'", obj)
        capm = re.search(r'cap\s*:\s*"((?:[^"\\]|\\.)*)"', obj)
        cap = re.sub(r"<[^>]+>", "", capm.group(1)) if capm else ""
        scenes.append({
            "id": sid.group(1) if sid else f"s{len(scenes)+1}",
            "t0": float(t0.group(1)),
            "dur": float(dur.group(1)),
            "events": nev,
            "cap": cap,
        })
    return scenes

def parse_groups(html):
    """Split the SVG into scene/beat groups; count primitives per group id."""
    starts = [(m.start(), m.group(2)) for m in
              re.finditer(r'<g class="(?:beat|scene)" id="([bs])(\d+)"', html)]
    svg_end = html.find("</svg>")
    if svg_end < 0:
        svg_end = len(html)
    groups = {}
    for i, (pos, gid) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else svg_end
        chunk = html[pos:end]
        groups[gid] = {
            "animateMotion": chunk.count("<animateMotion"),
            "data-count": chunk.count("data-count="),
            "write": len(re.findall(r'class="[^"]*\bwrite\b', chunk)),
            "draw": len(re.findall(r'class="[^"]*\bdraw\w*\b', chunk)),
            "dotIn": chunk.count("dotIn"),
        }
    return groups

def parse_captions(html, lines_path, scenes=None):
    """Return [(t0, text)] of spoken lines: CAPTIONS[] in the HTML, else the
    scenes[] cap fields (long-form: caps keep digits, so the payoff regex
    should use the caption form, e.g. 'two minutes|2 minutes')."""
    cues = []
    m = re.search(r"(?:const\s+)?CAPTIONS\s*=\s*\[(.*?)\n\];", html, re.S)
    if m:
        for cm in re.finditer(r"\{\s*t0\s*:\s*([0-9.]+)[^}]*?lines\s*:\s*\[(.*?)\]", m.group(1), re.S):
            text = " ".join(re.findall(r'"([^"]*)"', cm.group(2)))
            cues.append((float(cm.group(1)), text))
        if cues:
            return cues
    if scenes:
        return [(s["t0"], s.get("cap", "")) for s in scenes if s.get("cap")]
    if lines_path and Path(lines_path).exists():
        # lines.txt: one spoken line per paragraph; no timings — use the
        # timing.json sibling if present, else assume 0.8s start + ~1.2s gaps
        # is NOT reliable, so refuse to guess: report unknown.
        return []
    return cues

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--lines", default=None)
    ap.add_argument("--payoff", default=None,
                    help="regex for the payoff number/word, e.g. 'thirty-eight|38'")
    args = ap.parse_args()
    html = Path(args.html).read_text()
    scenes = parse_scenes(html)
    groups = parse_groups(html)
    if not scenes:
        print("HOOK-DENSITY CHECK: FAIL — no BEATS[]/scenes[] array found")
        return 1

    # Per-scene event totals: 1 (scene/beat start) + events[] + group
    # primitives (a drawing line, a dot arriving, a counting number and a
    # Write are each a visual event, not decoration).
    rows = []
    for i, s in enumerate(scenes):
        gid = re.sub(r"\D", "", s["id"]) or str(i + 1)
        g = groups.get(gid, {})
        total = (1 + s["events"] + g.get("animateMotion", 0)
                 + g.get("data-count", 0) + g.get("write", 0)
                 + g.get("draw", 0) + g.get("dotIn", 0))
        rows.append((s, total, g))

    first60 = sum(t for (s, t, g) in rows if s["t0"] < 60)
    failures = []
    print(f"hook-density check: {args.html}")
    print(f"{'scene':>6} {'t0':>6} {'dur':>5} {'evts':>5}  (1 start + events[] + motion + count + write + draw + dots)")
    for (s, t, g) in rows:
        print(f"{s['id']:>6} {s['t0']:6.2f} {s['dur']:5.2f} {t:5d}  "
              f"(events[]={s['events']} motion={g.get('animateMotion',0)} "
              f"count={g.get('data-count',0)} write={g.get('write',0)} "
              f"draw={g.get('draw',0)} dots={g.get('dotIn',0)})")
    print(f"first-60 s events: {first60} (bar: >= 6)")
    if first60 < 6:
        failures.append(f"first-60 s events = {first60} (< 6)")

    for (s, t, g) in rows:
        if s["dur"] >= 12 and t < 4:
            failures.append(f"scene {s['id']} is {s['dur']:.1f}s with only {t} events (< 4)")

    # Payoff spoken by 5 s.
    cues = parse_captions(html, args.lines, scenes)
    if cues:
        pat = re.compile(args.payoff, re.I) if args.payoff else NUM_RE
        hit = next(((t, txt) for (t, txt) in cues if pat.search(txt)), None)
        if hit is None:
            failures.append("payoff never spoken (no caption matches --payoff)")
            print("payoff: NEVER SPOKEN in captions")
        else:
            print(f"payoff first spoken at {hit[0]:.2f}s: \"{hit[1][:60]}\" (bar: <= 5 s)")
            if hit[0] > 5:
                failures.append(f"payoff first spoken at {hit[0]:.2f}s (> 5 s)")
    else:
        print("payoff: no CAPTIONS[] and no scenes[] caps to check against — "
              "check skipped, not passed")
        failures.append("payoff check could not run (no CAPTIONS[] / caps in HTML)")

    # Global primitive inventory (for the build note). Count on the HTML
    # with comments stripped: prose in comments (e.g. "<animateMotion>" in
    # a design note) is not a primitive in use. The write count looks for
    # the class in a class attribute, not the word in prose.
    code = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    code = re.sub(r"//[^\n]*", "", code)
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.S)
    print(f"global: animateMotion={code.count('<animateMotion')} "
          f"data-count={code.count('data-count=')} "
          f"write={len(re.findall(r'class=\"[^\"]*\\bwrite\\b', code))} "
          f"morph-calls={len(re.findall(r'(?:flipMorph|pathMorph|morphTo)\(', code))}")
    if failures:
        print("HOOK-DENSITY CHECK: FAIL")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("HOOK-DENSITY CHECK: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
