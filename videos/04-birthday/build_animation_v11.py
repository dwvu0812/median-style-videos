#!/usr/bin/env python3
"""Build rag-video-04-animation-v1.1.html from the v1.0 animation.

v1.1 densifies the visuals only — no script, voice, timing or scene-order
changes. Audio/timing stay byte-identical to v1.0 (scenes[] JS untouched).

Changes:
- S19 (the sparse curve scene, t=285-299s): rebuilt as a two-column layout.
  Left: a TRUE probability curve (computed P(n), polyline every 2 people)
  with axes, 0/25/50/75/100% y-ticks, 0-70 x-ticks, a dashed 50% line, and
  8 plotted dots (10/15/20/23/30/40/50/70) with label chips on 10/23/50/70.
  Right: a people-vs-chance table (all 8 values), 23 row highlighted.
- S13: row of 23 grey dots + one crossed-out pair + "23 people, no match".
- S16: dimension rule + "23 factors" label above the fraction.
- S20: dashed 50% threshold line on top + "underdog"/"favourite" labels.
- S21: "22 people - 47.6%" -> "23 people - 50.7%" comparison chips on top.
- S24: same comparison chips (23 vs 70) on top + a row of 70 dots below.
- S25: y-axis with 0/50/100% ticks.
- S35: top row of 8 mini pair-dots + baseline with ticks under the icons.
- S36: "11 + 11 + 1 = 23" formula on top + "11" labels + "referee" label.
"""
import re
from pathlib import Path

BASE = Path("/home/hatch/workspace/goals/ai-engineer-pivot-combined-learning-roadmap/files")
SRC = BASE / "rag-video-04-animation.html"
DST = BASE / "rag-video-04-animation-v1.1.html"

# ---- probability curve geometry (plot x 60..440, y 80..330 = 100%..0%) ----
def prob(n):
    p = 1.0
    for k in range(n):
        p *= (365 - k) / 365
    return 1 - p

def X(n): return 60 + n * 380 / 70
def Y(pr): return 330 - pr * 250

curve_pts = [(X(n), Y(prob(n))) for n in range(0, 71, 2)]
curve_d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in curve_pts)

# ---- S19: rebuilt two-column curve scene ----
s19 = (
    '<g class="scene" id="s19">'
    '<text x="40" y="48" class="eyebrow">PART 4 \u2014 THE CURVE</text>'
    '<g class="f1">'
    '<line x1="60" y1="330" x2="440" y2="330" class="thinG"/>'
    '<line x1="60" y1="330" x2="60" y2="80" class="thinG"/>'
    '<line x1="54" y1="330" x2="60" y2="330" class="thinG"/><text x="48" y="334" font-size="12" text-anchor="end" class="grey">0%</text>'
    '<line x1="54" y1="268" x2="60" y2="268" class="thinG"/><text x="48" y="272" font-size="12" text-anchor="end" class="grey">25%</text>'
    '<line x1="54" y1="205" x2="60" y2="205" class="thinG"/><text x="48" y="209" font-size="12" text-anchor="end" class="grey">50%</text>'
    '<line x1="54" y1="143" x2="60" y2="143" class="thinG"/><text x="48" y="147" font-size="12" text-anchor="end" class="grey">75%</text>'
    '<line x1="54" y1="80" x2="60" y2="80" class="thinG"/><text x="48" y="84" font-size="12" text-anchor="end" class="grey">100%</text>'
    + "".join(
        f'<line x1="{x}" y1="330" x2="{x}" y2="336" class="thinG"/>'
        f'<text x="{x}" y="350" font-size="12" text-anchor="middle" class="grey">{n}</text>'
        for x, n in [(60, 0), (114, 10), (169, 20), (223, 30), (277, 40), (331, 50), (386, 60), (440, 70)]
    )
    + '<line x1="60" y1="205" x2="440" y2="205" stroke="#6FCF97" stroke-width="1.5" stroke-dasharray="6 6"/>'
    f'<path d="{curve_d}" class="thin draw" pathLength="100" fill="none"/>'
    "</g>"
    '<g class="f2">'
    '<circle cx="114.3" cy="300.8" r="5" fill="#fff"/>'
    '<circle cx="141.4" cy="266.8" r="5" fill="#7E9BFF"/>'
    '<circle cx="168.6" cy="227.1" r="5" fill="#fff"/>'
    '<circle cx="184.9" cy="203.2" r="7" fill="#6FCF97" class="pulse"/>'
    '<circle cx="222.9" cy="153.4" r="5" fill="#fff"/>'
    '<circle cx="277.1" cy="107.2" r="5" fill="#fff"/>'
    '<circle cx="331.4" cy="87.4" r="6" fill="#6FCF97"/>'
    '<circle cx="440" cy="80.2" r="6" fill="#6FCF97"/>'
    '<rect x="76" y="308" width="76" height="20" fill="#141414"/><text x="114" y="322" font-size="13" text-anchor="middle" class="grey">10 \u00b7 11.7%</text>'
    '<rect x="140" y="172" width="90" height="20" fill="#141414"/><text x="185" y="186" font-size="14" text-anchor="middle" class="green">23 \u00b7 50.7%</text>'
    '<rect x="286" y="58" width="90" height="20" fill="#141414"/><text x="331" y="72" font-size="13" text-anchor="middle" class="green">50 \u00b7 97.0%</text>'
    '<rect x="396" y="90" width="80" height="20" fill="#141414"/><text x="436" y="104" font-size="13" text-anchor="middle" class="green">70 \u00b7 99.9%</text>'
    "</g>"
    '<g class="f3">'
    '<text x="500" y="86" font-size="13" class="grey">people</text>'
    '<text x="730" y="86" font-size="13" text-anchor="end" class="grey">chance</text>'
    '<line x1="480" y1="96" x2="750" y2="96" stroke="#333" stroke-width="1"/>'
    '<rect x="480" y="182" width="270" height="28" fill="#212120"/>'
    + "".join(
        f'<text x="500" y="{y}" font-size="15" class="{"green" if n == 23 else "grey"}">{n} people</text>'
        f'<text x="730" y="{y}" font-size="15" text-anchor="end" class="{"green" if n == 23 else "math"}">{v}</text>'
        for y, (n, v) in zip(
            [112, 140, 168, 196, 224, 252, 280, 308],
            [(10, "11.7%"), (15, "25.3%"), (20, "41.1%"), (23, "50.7%"),
             (30, "70.6%"), (40, "89.1%"), (50, "97.0%"), (70, "99.9%")],
        )
    )
    + '<text x="615" y="340" font-size="13" text-anchor="middle" class="green">23 \u2014 the tipping point</text>'
    '<text x="400" y="390" font-size="18" text-anchor="middle" class="grey">the curve starts slow</text>'
    "</g>"
    '<text x="770" y="430" text-anchor="end" class="mark">birthday \u2014 04</text>'
    "</g>"
)

# ---- S13: 23 dots, one crossed-out pair, label ----
dots13 = "".join(
    f'<circle cx="{110 + 26 * i}" cy="120" r="5" fill="#464845"/>' for i in range(23)
)
s13 = (
    '<g class="scene" id="s13">'
    '<text x="40" y="48" class="eyebrow">PART 3 \u2014 THE MATHS</text>'
    f'<g class="f1"><text x="400" y="95" font-size="15" text-anchor="middle" class="grey">23 people, no match</text>'
    f"{dots13}"
    '<line x1="390" y1="112" x2="428" y2="128" stroke="#9A9A9A" stroke-width="2"/>'
    '<line x1="390" y1="128" x2="428" y2="112" stroke="#9A9A9A" stroke-width="2"/>'
    "</g>"
    '<g class="f2 arrive"><text x="400" y="250" font-size="130" text-anchor="middle" class="math">?</text></g>'
    '<g class="f2"><text x="400" y="310" font-size="26" text-anchor="middle" class="math">what if NOBODY shares?</text></g>'
    '<g class="f3"><text x="400" y="350" font-size="18" text-anchor="middle" class="grey">count the opposite \u2014 then flip it</text></g>'
    '<path d="M 300 380 H 500" stroke="#9A9A9A" stroke-width="1.5" stroke-dasharray="5 7" fill="none"/>'
    '<text x="770" y="430" text-anchor="end" class="mark">birthday \u2014 04</text>'
    "</g>"
)

# ---- S16: dimension rule + "23 factors" label above the fraction ----
s16_old = '<g class="f1"><text x="400" y="190" font-size="44" text-anchor="middle" class="math">365 \u00d7 364 \u00d7 \u2026 \u00d7 343</text></g>'
s16_new = (
    '<g class="f1">'
    '<line x1="200" y1="145" x2="600" y2="145" stroke="#9A9A9A" stroke-width="1.5"/>'
    '<line x1="200" y1="141" x2="200" y2="149" stroke="#9A9A9A" stroke-width="1.5"/>'
    '<line x1="600" y1="141" x2="600" y2="149" stroke="#9A9A9A" stroke-width="1.5"/>'
    '<text x="610" y="149" font-size="13" class="grey">23 factors</text>'
    '<text x="400" y="190" font-size="44" text-anchor="middle" class="math">365 \u00d7 364 \u00d7 \u2026 \u00d7 343</text>'
    "</g>"
)

# ---- S20: 50% threshold line on top + underdog/favourite labels ----
s20_old_f1 = '<g class="f1"><rect x="270" y="224" width="260" height="12" rx="6" fill="#464845" class="sway"/><polygon points="400,236 388,262 412,262" fill="#212120"/></g>'
s20_new_f1 = (
    '<g class="f1">'
    '<line x1="120" y1="110" x2="680" y2="110" stroke="#6FCF97" stroke-width="1.5" stroke-dasharray="6 6"/>'
    '<text x="680" y="100" font-size="15" text-anchor="end" class="green">50% \u2014 the line</text>'
    '<rect x="270" y="224" width="260" height="12" rx="6" fill="#464845" class="sway"/>'
    '<polygon points="400,236 388,262 412,262" fill="#212120"/>'
    "</g>"
)
s20_old_f3 = '<g class="f3"><text x="400" y="320" font-size="18" text-anchor="middle" class="grey">then it tips \u2014 almost there</text></g>'
s20_new_f3 = (
    '<g class="f3">'
    '<text x="315" y="300" font-size="15" text-anchor="middle" class="grey">underdog</text>'
    '<text x="485" y="300" font-size="15" text-anchor="middle" class="green">favourite</text>'
    '<text x="400" y="320" font-size="18" text-anchor="middle" class="grey">then it tips \u2014 almost there</text></g>'
)

# ---- S21: 22 vs 23 comparison chips on top (into f2) ----
s21_old_f2 = '<g class="f2"><line x1="120" y1="300" x2="680" y2="300" stroke="#6FCF97" stroke-width="2" stroke-dasharray="6 6"/><text x="680" y="290" font-size="15" text-anchor="end" class="green">50% \u2014 the line</text></g>'
s21_new_f2 = (
    '<g class="f2">'
    '<text x="290" y="98" font-size="16" text-anchor="middle" class="grey">22 people \u2014 47.6%</text>'
    '<text x="400" y="98" font-size="16" text-anchor="middle" class="grey">\u2192</text>'
    '<text x="510" y="98" font-size="16" text-anchor="middle" class="green">23 people \u2014 50.7%</text>'
    '<line x1="120" y1="300" x2="680" y2="300" stroke="#6FCF97" stroke-width="2" stroke-dasharray="6 6"/>'
    '<text x="680" y="290" font-size="15" text-anchor="end" class="green">50% \u2014 the line</text>'
    "</g>"
)

# ---- S24: 23 vs 70 chips on top (into f2) + 70-dot row (into f3) ----
dots70 = "".join(
    f'<circle cx="{80 + 9.5 * i:.1f}" cy="385" r="3.5" fill="{"#6FCF97" if i in (33, 34) else "#464845"}"/>'
    for i in range(70)
)
s24_old_f2 = '<g class="f2"><text x="400" y="290" font-size="20" text-anchor="middle" class="grey">at seventy people</text></g>'
s24_new_f2 = (
    '<g class="f2">'
    '<text x="290" y="98" font-size="16" text-anchor="middle" class="grey">23 people \u2014 50.7%</text>'
    '<text x="400" y="98" font-size="16" text-anchor="middle" class="grey">\u2192</text>'
    '<text x="510" y="98" font-size="16" text-anchor="middle" class="green">70 people \u2014 99.9%</text>'
    '<text x="400" y="290" font-size="20" text-anchor="middle" class="grey">at seventy people</text>'
    "</g>"
)
s24_old_f3 = '<g class="f3"><text x="400" y="330" font-size="18" text-anchor="middle" class="grey">as certain as anything gets</text></g>'
s24_new_f3 = (
    f'<g class="f3">{dots70}'
    '<text x="400" y="330" font-size="18" text-anchor="middle" class="grey">as certain as anything gets</text></g>'
)

# ---- S25: y-axis with 0/50/100% ticks (into f1) ----
s25_old_f1 = '<g class="f1"><line x1="120" y1="380" x2="680" y2="380" class="thinG"/><path d="M 120 375 C 250 375, 300 300, 400 220 S 550 95, 680 90" class="thin draw" pathLength="100" fill="none"/></g>'
s25_new_f1 = (
    '<g class="f1">'
    '<line x1="120" y1="380" x2="680" y2="380" class="thinG"/>'
    '<line x1="120" y1="380" x2="120" y2="90" class="thinG"/>'
    '<line x1="114" y1="330" x2="120" y2="330" class="thinG"/><text x="108" y="334" font-size="12" text-anchor="end" class="grey">0%</text>'
    '<line x1="114" y1="205" x2="120" y2="205" class="thinG"/><text x="108" y="209" font-size="12" text-anchor="end" class="grey">50%</text>'
    '<line x1="114" y1="80" x2="120" y2="80" class="thinG"/><text x="108" y="84" font-size="12" text-anchor="end" class="grey">100%</text>'
    '<path d="M 120 375 C 250 375, 300 300, 400 220 S 550 95, 680 90" class="thin draw" pathLength="100" fill="none"/>'
    "</g>"
)

# ---- S35: top row of 8 mini pair-dots (into f1) + baseline with ticks (into f3) ----
pairs35 = "".join(
    f'<line x1="{c - 7}" y1="110" x2="{c + 7}" y2="110" stroke="#464845" stroke-width="1.5"/>'
    f'<circle cx="{c - 7}" cy="110" r="4" fill="#464845"/><circle cx="{c + 7}" cy="110" r="4" fill="#464845"/>'
    for c in [130, 200, 270, 340, 410, 480, 550, 620]
)
s35_old_f1 = '<g class="f1"><rect x="170" y="220" width="70" height="60" rx="8" fill="#212120" stroke="#fff" stroke-width="2"/><path d="M 185 220 V 200 A 20 20 0 0 1 225 220" fill="none" stroke="#fff" stroke-width="2"/><text x="205" y="320" font-size="16" text-anchor="middle" class="grey">security</text></g>'
s35_new_f1 = f'<g class="f1">{pairs35}<rect x="170" y="220" width="70" height="60" rx="8" fill="#212120" stroke="#fff" stroke-width="2"/><path d="M 185 220 V 200 A 20 20 0 0 1 225 220" fill="none" stroke="#fff" stroke-width="2"/><text x="205" y="320" font-size="16" text-anchor="middle" class="grey">security</text></g>'
s35_old_f3 = '<text x="400" y="370" font-size="18" text-anchor="middle" class="grey">the same maths, everywhere</text>'
s35_new_f3 = (
    '<line x1="180" y1="348" x2="620" y2="348" stroke="#464845" stroke-width="1.5"/>'
    '<line x1="205" y1="344" x2="205" y2="352" stroke="#464845" stroke-width="1.5"/>'
    '<line x1="400" y1="344" x2="400" y2="352" stroke="#464845" stroke-width="1.5"/>'
    '<line x1="575" y1="344" x2="575" y2="352" stroke="#464845" stroke-width="1.5"/>'
    '<text x="400" y="370" font-size="18" text-anchor="middle" class="grey">the same maths, everywhere</text>'
)

# ---- S36: "11 + 11 + 1 = 23" on top + "11" labels + "referee" label ----
s36_old_f1 = '<g class="f1"><circle cx="150" cy="180" r="8" fill="#fff"/>'
s36_new_f1 = (
    '<g class="f1"><text x="400" y="115" font-size="32" text-anchor="middle" class="math">11 + 11 + 1 = 23</text>'
    '<text x="110" y="185" font-size="14" text-anchor="middle" class="grey">11</text>'
    '<circle cx="150" cy="180" r="8" fill="#fff"/>'
)
s36_old_f2 = '<g class="f2"><circle cx="150" cy="280" r="8" fill="#464845"/>'
s36_new_f2 = (
    '<g class="f2"><text x="110" y="285" font-size="14" text-anchor="middle" class="grey">11</text>'
    '<circle cx="150" cy="280" r="8" fill="#464845"/>'
)
s36_old_f3 = '<g class="f3"><circle cx="400" cy="340" r="8" fill="#6FCF97"/><text x="400" y="380" font-size="18" text-anchor="middle" class="grey">eleven against eleven \u2014 plus the referee: twenty-three people, 253 pairs</text></g>'
s36_new_f3 = (
    '<g class="f3"><circle cx="400" cy="340" r="8" fill="#6FCF97"/>'
    '<text x="425" y="345" font-size="14" class="green">referee</text>'
    '<text x="400" y="380" font-size="18" text-anchor="middle" class="grey">eleven against eleven \u2014 plus the referee: twenty-three people, 253 pairs</text></g>'
)


def replace_scene(lines, scene_id, new_block):
    # v1.0 scenes can span MULTIPLE lines (opening <g> on its own line,
    # children on following lines, closing '    </g>' on its own line).
    # Replacing only the opening line leaves orphan fragments that break
    # the SVG (v1.1 first attempt did exactly this). Replace the whole span.
    start = next(i for i, ln in enumerate(lines) if f'id="{scene_id}"' in ln)
    close = next(i for i in range(start, len(lines)) if lines[i].strip() == "</g>")
    lines[start:close + 1] = [new_block]
    return True


def main():
    html = SRC.read_text(encoding="utf-8")
    lines = html.split("\n")
    replace_scene(lines, "s19", s19)
    replace_scene(lines, "s13", s13)

    def sub(old, new):
        nonlocal html
        assert old in html, f"pattern not found: {old[:80]}"
        html = html.replace(old, new, 1)

    html = "\n".join(lines)
    sub(s16_old, s16_new)
    sub(s20_old_f1, s20_new_f1)
    sub(s20_old_f3, s20_new_f3)
    sub(s21_old_f2, s21_new_f2)
    sub(s24_old_f2, s24_new_f2)
    sub(s24_old_f3, s24_new_f3)
    sub(s25_old_f1, s25_new_f1)
    sub(s35_old_f1, s35_new_f1)
    sub(s35_old_f3, s35_new_f3)
    sub(s36_old_f1, s36_new_f1)
    sub(s36_old_f2, s36_new_f2)
    sub(s36_old_f3, s36_new_f3)

    html = html.replace(
        "<title>Why 23 People Is Enough \u2014 The Birthday Paradox \u2014 Median style, v1.0 + voiceover</title>",
        "<title>Why 23 People Is Enough \u2014 The Birthday Paradox \u2014 Median style, v1.1 + voiceover</title>",
    )
    html = html.replace(
        "<h1>Why 23 People Is Enough \u2014 The Birthday Paradox <span>\u2014 Median style, v1.0</span></h1>",
        "<h1>Why 23 People Is Enough \u2014 The Birthday Paradox <span>\u2014 Median style, v1.1</span></h1>",
    )
    html = html.replace(
        "Voice: Muse TTS avocado_v2:vd2_quivering_oak, English, speed 80 (voice B).</p>",
        "Voice: Muse TTS avocado_v2:vd2_quivering_oak, English, speed 80 (voice B). "
        "v1.1: denser visuals only (curve scene rebuilt as a true chart + table, 8 more "
        "scenes enriched); script, voice, timing and scene order identical to v1.0.</p>",
    )
    html = html.replace(
        "Video 04 \u2014 Why 23 People Is Enough \u2014 The Birthday Paradox.</b> v1.0:",
        "Video 04 \u2014 Why 23 People Is Enough \u2014 The Birthday Paradox.</b> v1.1 (visuals only):",
    )
    # scenes[] JS must be untouched: verify the count is still 38
    assert html.count("{t0:") == 38, "scenes[] changed!"
    assert "const TOTAL=627.608" in html
    DST.write_text(html, encoding="utf-8")
    print(f"wrote {DST} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
