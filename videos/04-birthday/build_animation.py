#!/usr/bin/env python3
"""Build rag-video-04-animation.html from the video 03 v2.5 player template.

Reuses the v2.5 CSS + JS (wall clock, gap-hold, 0.45s blur-outgoing-only
dissolve, f1/f2/f3 stagger) verbatim; only the 38 scene groups, the scenes[]
array (from timing.json), TOTAL and the countUp target change.

Usage: python3 build_animation.py
"""
import itertools
import json
import math
from pathlib import Path

GOAL = Path("/home/hatch/workspace/goals/ai-engineer-pivot-combined-learning-roadmap/files")
V3 = GOAL / "rag-video-03-animation.html"
AUDIO = GOAL / "rag-video-04-audio"
OUT = GOAL / "rag-video-04-animation.html"

MARK = '<text x="770" y="430" text-anchor="end" class="mark">birthday — 04</text>'

EYEBROW = {
    1: "WHY 23 PEOPLE IS ENOUGH", 2: "WHY 23 PEOPLE IS ENOUGH",
    3: "WHY 23 PEOPLE IS ENOUGH",
    4: "PART 1 — THE WRONG QUESTION", 5: "PART 1 — THE WRONG QUESTION",
    6: "PART 1 — THE WRONG QUESTION", 7: "PART 1 — THE WRONG QUESTION",
    8: "PART 2 — COUNT THE PAIRS", 9: "PART 2 — COUNT THE PAIRS",
    10: "PART 2 — COUNT THE PAIRS", 11: "PART 2 — COUNT THE PAIRS",
    12: "PART 2 — COUNT THE PAIRS",
    13: "PART 3 — THE MATHS", 14: "PART 3 — THE MATHS",
    15: "PART 3 — THE MATHS", 16: "PART 3 — THE MATHS",
    17: "PART 3 — THE MATHS", 18: "PART 3 — THE MATHS",
    19: "PART 4 — THE CURVE", 20: "PART 4 — THE CURVE",
    21: "PART 4 — THE CURVE", 22: "PART 4 — THE CURVE",
    23: "PART 4 — THE CURVE", 24: "PART 4 — THE CURVE",
    25: "PART 4 — THE CURVE",
    26: "PART 5 — WHY YOUR BRAIN SAYS NO",
    27: "PART 5 — WHY YOUR BRAIN SAYS NO",
    28: "PART 5 — WHY YOUR BRAIN SAYS NO",
    29: "PART 5 — WHY YOUR BRAIN SAYS NO",
    30: "PART 5 — WHY YOUR BRAIN SAYS NO",
    31: "PART 6 — TRY IT YOURSELF", 32: "PART 6 — TRY IT YOURSELF",
    33: "PART 6 — TRY IT YOURSELF", 34: "PART 6 — TRY IT YOURSELF",
    35: "PART 6 — TRY IT YOURSELF",
    36: "RECAP", 37: "RECAP", 38: "RECAP",
}


def row(n, x0, y, dx=24, r=6, fill="#464845", hi=()):
    return "".join(
        f'<circle cx="{x0 + i * dx}" cy="{y}" r="{r}" '
        f'fill="{("#6FCF97" if i in hi else fill)}"/>'
        for i in range(n))


def grid(n, x0, y0, cols, dx, dy, r=6, fill="#464845", hi=()):
    out = []
    for i in range(n):
        cx = x0 + (i % cols) * dx
        cy = y0 + (i // cols) * dy
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" '
                   f'fill="{("#6FCF97" if i in hi else fill)}"/>')
    return "".join(out)


def circle_dots(cx, cy, rad, n, r=6, fill="#464845", hi=()):
    out = []
    for i in range(n):
        a = 2 * math.pi * i / n - math.pi / 2
        x = cx + rad * math.cos(a)
        y = cy + rad * math.sin(a)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" '
                   f'fill="{("#6FCF97" if i in hi else fill)}"/>')
    return "".join(out)


def circle_pts(cx, cy, rad, n):
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n - math.pi / 2
        pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    return pts


def chords(pts, pairs, stroke="#464845", w=1, op=".6"):
    return "".join(
        f'<line x1="{pts[a][0]:.1f}" y1="{pts[a][1]:.1f}" '
        f'x2="{pts[b][0]:.1f}" y2="{pts[b][1]:.1f}" stroke="{stroke}" '
        f'stroke-width="{w}" opacity="{op}"/>'
        for a, b in pairs)


# --- scene inner content (eyebrow + wordmark added at assembly) ---
S = {}

S[1] = (
    '<g class="f1 arrive"><text x="400" y="240" font-size="150" text-anchor="middle" class="math">23</text></g>'
    '<g class="f2"><text x="400" y="300" font-size="20" text-anchor="middle" class="grey">in a room of just twenty-three people</text></g>'
    '<g class="f3"><text x="400" y="338" font-size="18" text-anchor="middle" class="green">a shared birthday is more likely than not</text></g>'
    + row(23, 90, 392, dx=28, r=4, hi=(5, 6))
)

S[2] = (
    '<g class="f1"><text x="400" y="120" font-size="20" text-anchor="middle" class="grey">most people guess</text></g>'
    '<g class="f2"><text x="290" y="250" font-size="110" text-anchor="middle" class="math dim">180</text>'
    '<line x1="195" y1="212" x2="385" y2="212" stroke="#9A9A9A" stroke-width="3"/>'
    '<text x="290" y="300" font-size="15" text-anchor="middle" class="grey">the guess</text></g>'
    '<text x="440" y="250" font-size="40" text-anchor="middle" class="grey">→</text>'
    '<g class="f3 arrive"><text x="590" y="250" font-size="130" text-anchor="middle" class="math green">23</text>'
    '<text x="590" y="300" font-size="15" text-anchor="middle" class="green">the answer</text></g>'
)

S[3] = (
    '<g class="f1"><text x="40" y="136" font-size="16" class="grey">classroom</text>'
    + row(30, 200, 132, dx=16, r=5)
    + '<text x="700" y="136" font-size="16" class="grey">30</text></g>'
    '<g class="f2"><text x="40" y="226" font-size="16" class="grey">party</text>'
    + row(23, 200, 222, dx=16, r=5)
    + '<text x="700" y="226" font-size="16" class="grey">23</text></g>'
    '<g class="f3"><text x="40" y="316" font-size="16" class="grey">football team</text>'
    + row(23, 200, 312, dx=16, r=5)
    + '<text x="700" y="316" font-size="16" class="grey">23</text></g>'
    '<text x="400" y="380" font-size="18" text-anchor="middle" class="grey">twenty-three people is enough — anywhere</text>'
)

S[4] = (
    '<g class="f1">' + circle_dots(400, 210, 95, 12, r=7) +
    '<circle cx="400" cy="210" r="13" fill="#7E9BFF" class="pulse"/>'
    '<text x="400" y="215" font-size="11" text-anchor="middle" class="ink">you</text></g>'
    '<g class="f2"><text x="400" y="350" font-size="26" text-anchor="middle" class="math">will someone share MY birthday?</text></g>'
    '<g class="f3"><text x="400" y="390" font-size="18" text-anchor="middle" class="grey">that is the wrong question</text></g>'
)

S[5] = (
    '<rect x="140" y="150" width="520" height="140" fill="url(#dotgrid)"/>'
    '<g class="f1"><circle cx="400" cy="220" r="13" fill="#7E9BFF" class="pulse"/>'
    '<text x="400" y="215" font-size="11" text-anchor="middle" class="ink">you</text></g>'
    '<g class="f2"><text x="400" y="340" font-size="30" text-anchor="middle" class="math">253 other people</text></g>'
    '<g class="f3"><text x="400" y="380" font-size="18" text-anchor="middle" class="grey">more than ten times as many — all hoping to match one day</text></g>'
)

S[6] = (
    '<g class="f1 arrive"><text x="400" y="180" font-size="72" text-anchor="middle" class="math">1 / 365</text></g>'
    '<g class="f2"><rect x="120" y="220" width="560" height="48" fill="url(#calgrid)"/>'
    '<rect x="120" y="220" width="12" height="12" fill="#6FCF97"/>'
    '<text x="400" y="310" font-size="18" text-anchor="middle" class="grey">one chance — one day out of three hundred and sixty-five</text></g>'
    '<g class="f3"><text x="400" y="360" font-size="18" text-anchor="middle" class="grey">it adds up slowly</text></g>'
)

S[7] = (
    '<rect x="90" y="150" width="280" height="170" rx="10" fill="#212120"/>'
    '<rect x="430" y="150" width="280" height="170" rx="10" fill="#212120"/>'
    '<g class="f1"><circle cx="190" cy="225" r="14" fill="#6FCF97"/><circle cx="270" cy="225" r="14" fill="#6FCF97"/>'
    '<line x1="204" y1="225" x2="256" y2="225" stroke="#6FCF97" stroke-width="2"/>'
    '<text x="230" y="290" font-size="17" text-anchor="middle" class="green">ANY two people</text></g>'
    '<g class="f2"><circle cx="530" cy="225" r="14" fill="#7E9BFF"/><circle cx="610" cy="225" r="14" fill="#464845"/>'
    '<line x1="544" y1="225" x2="596" y2="225" stroke="#9A9A9A" stroke-width="2"/>'
    '<text x="570" y="290" font-size="17" text-anchor="middle" class="blue">YOU + someone</text></g>'
    '<g class="f3"><text x="400" y="370" font-size="18" text-anchor="middle" class="grey">the real question is different</text></g>'
)

S[8] = (
    '<g class="f1 arrive"><text x="400" y="220" font-size="44" text-anchor="middle" class="math">23 + 22 + 21 + … + 1</text></g>'
    '<g class="f2"><text x="400" y="290" font-size="18" text-anchor="middle" class="grey">every pair counted once — nobody counted twice</text></g>'
    '<g class="f3"><text x="400" y="340" font-size="18" text-anchor="middle" class="grey">person 1 has 22 partners · person 2 has 21 new ones · and so on</text></g>'
    '<line x1="200" y1="370" x2="600" y2="370" stroke="#9A9A9A" stroke-width="1.5"/>'
    '<text x="200" y="392" font-size="13" text-anchor="middle" class="grey">22</text>'
    '<text x="400" y="392" font-size="13" text-anchor="middle" class="grey">21</text>'
    '<text x="600" y="392" font-size="13" text-anchor="middle" class="grey">1</text>'
)

S[9] = (
    '<rect x="110" y="150" width="580" height="120" rx="10" fill="#141414"/>'
    '<g class="f1 arrive"><text x="400" y="235" font-size="72" text-anchor="middle" class="math">23 × 22 ÷ 2 = <tspan id="count253" fill="#6FCF97">253</tspan></text></g>'
    '<g class="f2"><rect x="176" y="252" width="448" height="4" fill="#6FCF97" class="growloop"/></g>'
    '<g class="f3"><text x="400" y="310" font-size="20" text-anchor="middle" class="grey">two hundred and fifty-three pairs — two hundred and fifty-three chances</text></g>'
    '<text x="400" y="350" font-size="18" text-anchor="middle" class="grey">pairs</text>'
)

S[10] = (
    '<rect x="140" y="150" width="520" height="130" fill="url(#dotgrid)"/>'
    '<g class="f1"><circle cx="360" cy="215" r="9" fill="#6FCF97"/><circle cx="440" cy="215" r="9" fill="#6FCF97"/>'
    '<line x1="369" y1="215" x2="431" y2="215" stroke="#6FCF97" stroke-width="2"/></g>'
    '<g class="f2"><text x="400" y="330" font-size="30" text-anchor="middle" class="math">each pair: 1 in 365</text></g>'
    '<g class="f3"><text x="400" y="370" font-size="18" text-anchor="middle" class="grey">small on its own — but there are two hundred and fifty-three of them</text></g>'
)

S[11] = (
    '<rect x="80" y="160" width="300" height="160" rx="10" fill="#212120"/>'
    '<rect x="420" y="160" width="300" height="160" rx="10" fill="#212120"/>'
    '<g class="f1"><text x="230" y="240" font-size="64" text-anchor="middle" class="math green">253</text>'
    '<text x="230" y="280" font-size="17" text-anchor="middle" class="grey">pairs</text></g>'
    '<g class="f2"><text x="570" y="240" font-size="64" text-anchor="middle" class="math blue">253</text>'
    '<text x="570" y="280" font-size="17" text-anchor="middle" class="grey">other people</text></g>'
    '<g class="f3"><text x="400" y="370" font-size="18" text-anchor="middle" class="grey">same number, two different questions</text></g>'
)

S[12] = (
    '<rect x="90" y="140" width="280" height="180" rx="10" fill="#141414"/>'
    '<rect x="430" y="140" width="280" height="180" rx="10" fill="#141414"/>'
    '<g class="f1"><text x="230" y="180" font-size="20" text-anchor="middle" class="math">23 vs 1</text>'
    + grid(23, 140, 205, cols=6, dx=26, dy=26, r=6)
    + '<text x="230" y="355" font-size="15" text-anchor="middle" class="grey">you against the room</text></g>'
    '<g class="f2"><text x="570" y="180" font-size="20" text-anchor="middle" class="math">253 vs 253</text>'
    '<rect x="470" y="210" width="200" height="18" fill="#6FCF97"/>'
    '<rect x="470" y="245" width="200" height="18" fill="#7E9BFF"/>'
    '<text x="570" y="300" font-size="15" text-anchor="middle" class="grey">any pair against any pair</text></g>'
    '<g class="f3"><text x="400" y="395" font-size="18" text-anchor="middle" class="grey">two kinds of comparison — only one of them is the paradox</text></g>'
)

S[13] = (
    '<g class="f1 arrive"><text x="400" y="250" font-size="130" text-anchor="middle" class="math">?</text></g>'
    '<g class="f2"><text x="400" y="310" font-size="26" text-anchor="middle" class="math">what if NOBODY shares?</text></g>'
    '<g class="f3"><text x="400" y="350" font-size="18" text-anchor="middle" class="grey">count the opposite — then flip it</text></g>'
    '<path d="M 300 380 H 500" stroke="#9A9A9A" stroke-width="1.5" stroke-dasharray="5 7" fill="none"/>'
)

S[14] = (
    '<g class="f1 arrive"><text x="400" y="220" font-size="88" text-anchor="middle" class="math">365 / 365</text></g>'
    '<g class="f2"><text x="400" y="280" font-size="20" text-anchor="middle" class="grey">person one — any day is free</text></g>'
    '<g class="f3"><rect x="180" y="310" width="440" height="36" fill="url(#calgrid)"/>'
    '<text x="400" y="380" font-size="15" text-anchor="middle" class="grey">all three hundred and sixty-five days open</text></g>'
)

S[15] = (
    '<g class="f1 arrive"><text x="400" y="220" font-size="88" text-anchor="middle" class="math">364 / 365</text></g>'
    '<g class="f2"><text x="400" y="280" font-size="20" text-anchor="middle" class="grey">person two — any day except the first person’s</text></g>'
    '<g class="f3"><rect x="180" y="310" width="440" height="36" fill="url(#calgrid)"/>'
    '<rect x="180" y="310" width="12" height="12" fill="#212120" stroke="#fff" stroke-width="1.5"/>'
    '<line x1="180" y1="310" x2="192" y2="322" stroke="#fff" stroke-width="1.5"/>'
    '<line x1="192" y1="310" x2="180" y2="322" stroke="#fff" stroke-width="1.5"/>'
    '<text x="400" y="380" font-size="15" text-anchor="middle" class="grey">one day taken</text></g>'
)

S[16] = (
    '<g class="f1"><text x="400" y="190" font-size="44" text-anchor="middle" class="math">365 × 364 × … × 343</text></g>'
    '<g class="f2"><line x1="150" y1="215" x2="650" y2="215" class="thin"/>'
    '<text x="400" y="280" font-size="44" text-anchor="middle" class="math">365<tspan baseline-shift="super" font-size="28">23</tspan></text></g>'
    '<g class="f3"><text x="400" y="340" font-size="18" text-anchor="middle" class="grey">twenty-three factors on top — the 23rd person avoids twenty-two days</text></g>'
)

S[17] = (
    '<g class="f1 arrive"><text x="400" y="200" font-size="88" text-anchor="middle" class="math grey">49.3%</text></g>'
    '<g class="f2"><rect x="120" y="250" width="560" height="24" fill="#212120"/>'
    '<rect x="120" y="250" width="276" height="24" fill="#464845"/>'
    '<line x1="400" y1="240" x2="400" y2="284" stroke="#6FCF97" stroke-width="2" stroke-dasharray="5 5"/>'
    '<text x="400" y="310" font-size="15" text-anchor="middle" class="green">50% — the line</text></g>'
    '<g class="f3"><text x="400" y="360" font-size="18" text-anchor="middle" class="grey">the chance nobody shares — less than half</text></g>'
)

S[18] = (
    '<rect x="110" y="150" width="580" height="120" rx="10" fill="#141414"/>'
    '<g class="f1 arrive"><text x="400" y="235" font-size="72" text-anchor="middle" class="math">100 − 49.3 = <tspan fill="#6FCF97">50.7%</tspan></text></g>'
    '<g class="f2"><rect x="176" y="252" width="448" height="4" fill="#6FCF97" class="growloop"/></g>'
    '<g class="f3"><text x="400" y="310" font-size="20" text-anchor="middle" class="grey">flip it — more likely than not</text></g>'
)

S[19] = (
    '<g class="f1"><line x1="120" y1="340" x2="680" y2="340" class="thinG"/>'
    '<line x1="120" y1="340" x2="120" y2="120" class="thinG"/>'
    '<path d="M 120 340 L 250 305 L 550 225" class="thin draw" pathLength="100" fill="none"/></g>'
    '<g class="f2"><circle cx="250" cy="305" r="8" fill="#fff"/><circle cx="550" cy="225" r="8" fill="#7E9BFF" class="pulse"/>'
    '<text x="250" y="335" font-size="15" text-anchor="middle" class="grey">10 · 11.7%</text>'
    '<text x="550" y="200" font-size="15" text-anchor="middle" class="blue">15 · 25.3%</text></g>'
    '<g class="f3"><text x="400" y="390" font-size="18" text-anchor="middle" class="grey">the curve starts slow</text></g>'
)
S[20] = (
    '<g class="f1"><rect x="270" y="224" width="260" height="12" rx="6" fill="#464845" class="sway"/>'
    '<polygon points="400,236 388,262 412,262" fill="#212120"/></g>'
    '<g class="f2"><rect x="270" y="196" width="90" height="28" rx="6" fill="#212120"/>'
    '<rect x="440" y="196" width="90" height="28" rx="6" fill="#212120"/>'
    '<text x="315" y="176" font-size="16" text-anchor="middle" class="grey">20 · 41.1%</text>'
    '<text x="485" y="176" font-size="16" text-anchor="middle" class="blue">22 · 47.6%</text></g>'
    '<g class="f3"><text x="400" y="320" font-size="18" text-anchor="middle" class="grey">then it tips — almost there</text></g>'
    '<line x1="320" y1="268" x2="480" y2="268" stroke="#9A9A9A" stroke-width="1.5"/>'
)

S[21] = (
    '<rect x="110" y="130" width="580" height="120" rx="10" fill="#141414"/>'
    '<g class="f1 arrive"><text x="400" y="225" font-size="120" text-anchor="middle" class="math green">50.7%</text></g>'
    '<g class="f2"><line x1="120" y1="300" x2="680" y2="300" stroke="#6FCF97" stroke-width="2" stroke-dasharray="6 6"/>'
    '<text x="680" y="290" font-size="15" text-anchor="end" class="green">50% — the line</text></g>'
    '<g class="f3"><text x="400" y="350" font-size="20" text-anchor="middle" class="grey">crossed at twenty-three people</text></g>'
)

S[22] = (
    '<g class="f1">'
    '<rect x="150" y="333" width="80" height="47" fill="#464845"/>'
    '<rect x="260" y="279" width="80" height="101" fill="#464845"/>'
    '<rect x="370" y="216" width="80" height="164" fill="#464845"/>'
    '<rect x="480" y="190" width="80" height="190" fill="#464845"/>'
    '<rect x="590" y="177" width="80" height="203" fill="#6FCF97"/></g>'
    '<g class="f2">'
    '<text x="190" y="320" font-size="14" text-anchor="middle" class="grey">11.7%</text>'
    '<text x="300" y="266" font-size="14" text-anchor="middle" class="grey">25.3%</text>'
    '<text x="410" y="203" font-size="14" text-anchor="middle" class="grey">41.1%</text>'
    '<text x="520" y="177" font-size="14" text-anchor="middle" class="grey">47.6%</text>'
    '<text x="630" y="164" font-size="14" text-anchor="middle" class="green">50.7%</text></g>'
    '<g class="f3"><text x="400" y="425" font-size="18" text-anchor="middle" class="grey">every new person adds more pairs than the last</text></g>'
    '<text x="190" y="400" font-size="13" text-anchor="middle" class="grey">10</text>'
    '<text x="300" y="400" font-size="13" text-anchor="middle" class="grey">15</text>'
    '<text x="410" y="400" font-size="13" text-anchor="middle" class="grey">20</text>'
    '<text x="520" y="400" font-size="13" text-anchor="middle" class="grey">22</text>'
    '<text x="630" y="400" font-size="13" text-anchor="middle" class="grey">23</text>'
)

S[23] = (
    '<g class="f1">'
    '<rect x="180" y="168" width="100" height="212" fill="#464845"/>'
    '<rect x="360" y="113" width="100" height="267" fill="#464845"/>'
    '<rect x="540" y="89" width="100" height="291" fill="#6FCF97"/></g>'
    '<g class="f2">'
    '<text x="230" y="155" font-size="16" text-anchor="middle" class="grey">70.6%</text>'
    '<text x="410" y="100" font-size="16" text-anchor="middle" class="grey">89.1%</text>'
    '<text x="590" y="76" font-size="16" text-anchor="middle" class="green">97.0%</text></g>'
    '<g class="f3"><text x="400" y="425" font-size="18" text-anchor="middle" class="grey">almost certain by fifty</text></g>'
    '<text x="230" y="400" font-size="13" text-anchor="middle" class="grey">30 people</text>'
    '<text x="410" y="400" font-size="13" text-anchor="middle" class="grey">40 people</text>'
    '<text x="590" y="400" font-size="13" text-anchor="middle" class="grey">50 people</text>'
)

S[24] = (
    '<rect x="110" y="130" width="580" height="130" rx="10" fill="#141414"/>'
    '<g class="f1 arrive"><text x="400" y="230" font-size="120" text-anchor="middle" class="math green">99.9%</text></g>'
    '<g class="f2"><text x="400" y="290" font-size="20" text-anchor="middle" class="grey">at seventy people</text></g>'
    '<g class="f3"><text x="400" y="330" font-size="18" text-anchor="middle" class="grey">as certain as anything gets</text></g>'
)

S[25] = (
    '<g class="f1"><line x1="120" y1="380" x2="680" y2="380" class="thinG"/>'
    '<path d="M 120 375 C 250 375, 300 300, 400 220 S 550 95, 680 90" class="thin draw" pathLength="100" fill="none"/></g>'
    '<g class="f2"><circle cx="200" cy="372" r="7" fill="#fff"/><circle cx="400" cy="220" r="7" fill="#7E9BFF" class="pulse"/><circle cx="600" cy="108" r="7" fill="#6FCF97"/>'
    '<text x="200" y="400" font-size="13" text-anchor="middle" class="grey">10</text>'
    '<text x="400" y="200" font-size="13" text-anchor="middle" class="blue">23</text>'
    '<text x="600" y="88" font-size="13" text-anchor="middle" class="green">70</text></g>'
    '<g class="f3"><text x="400" y="415" font-size="18" text-anchor="middle" class="grey">flat, then steep, then flat again at the top</text></g>'
)

S[26] = (
    '<g class="f1"><text x="400" y="130" font-size="18" text-anchor="middle" class="grey">365 days</text>'
    '<rect x="60" y="150" width="680" height="72" fill="url(#calgrid)"/></g>'
    '<g class="f2">' + row(23, 110, 300, dx=26, r=7) +
    '<text x="400" y="340" font-size="18" text-anchor="middle" class="grey">23 people</text></g>'
    '<g class="f3"><text x="400" y="390" font-size="18" text-anchor="middle" class="grey">most days stay empty — the pairs do the work</text></g>'
)

S[27] = (
    '<g class="f1">'
    '<rect x="180" y="260" width="110" height="120" fill="#464845"/>'
    '<rect x="360" y="210" width="110" height="170" fill="#464845"/>'
    '<rect x="540" y="120" width="110" height="260" fill="#6FCF97"/></g>'
    '<g class="f2">'
    '<text x="235" y="247" font-size="16" text-anchor="middle" class="grey">253</text>'
    '<text x="415" y="197" font-size="16" text-anchor="middle" class="grey">435</text>'
    '<text x="595" y="107" font-size="16" text-anchor="middle" class="green">2,415</text></g>'
    '<g class="f3"><text x="400" y="425" font-size="18" text-anchor="middle" class="grey">pairs grow faster than people</text></g>'
    '<text x="235" y="400" font-size="13" text-anchor="middle" class="grey">23 people</text>'
    '<text x="415" y="400" font-size="13" text-anchor="middle" class="grey">30 people</text>'
    '<text x="595" y="400" font-size="13" text-anchor="middle" class="grey">70 people</text>'
)

_pts28 = circle_pts(600, 220, 70, 8)
S[28] = (
    '<g class="f1">' + grid(23, 130, 140, cols=5, dx=34, dy=34, r=7) +
    '<text x="215" y="320" font-size="16" text-anchor="middle" class="grey">23 people</text></g>'
    '<g class="f2">'
    + chords(_pts28, list(itertools.combinations(range(8), 2)))
    + chords(_pts28, [(0, 1)], stroke="#6FCF97", w=2, op="1")
    + "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{("#6FCF97" if i in (0, 1) else "#fff")}"/>'
              for i, (x, y) in enumerate(_pts28))
    + '<text x="600" y="330" font-size="16" text-anchor="middle" class="green">253 handshakes</text></g>'
    '<g class="f3"><text x="400" y="390" font-size="18" text-anchor="middle" class="grey">every handshake is a comparison</text></g>'
)

S[29] = (
    '<g class="f1"><path d="M 120 380 H 240 V 330 H 360 V 280 H 480 V 230 H 600 V 180 H 680" class="thin draw" pathLength="100" fill="none"/></g>'
    '<circle r="7" fill="#7E9BFF"><animateMotion dur="8s" repeatCount="indefinite" path="M 120 380 H 240 V 330 H 360 V 280 H 480 V 230 H 600 V 180 H 680"/></circle>'
    '<g class="f2">'
    '<text x="180" y="365" font-size="14" text-anchor="middle" class="grey">10</text>'
    '<text x="300" y="315" font-size="14" text-anchor="middle" class="grey">15</text>'
    '<text x="420" y="265" font-size="14" text-anchor="middle" class="grey">20</text>'
    '<text x="540" y="215" font-size="14" text-anchor="middle" class="grey">22</text>'
    '<text x="640" y="165" font-size="14" text-anchor="middle" class="green">23</text></g>'
    '<g class="f3"><text x="400" y="415" font-size="18" text-anchor="middle" class="grey">each step is bigger than the last</text></g>'
)

S[30] = (
    '<g class="f1">'
    + "".join(
        f'<rect x="{90 + i * 58}" y="{340 - h}" width="40" height="{h}" '
        f'fill="{("#6FCF97" if i == 8 else "#464845")}"/>'
        for i, h in enumerate([168, 144, 180, 174, 186, 180, 192, 198, 228, 186, 174, 180]))
    + '</g>'
    '<g class="f2"><text x="400" y="100" font-size="18" text-anchor="middle" class="green">September — the busiest month</text></g>'
    '<g class="f3"><text x="400" y="410" font-size="18" text-anchor="middle" class="grey">real birthdays bunch up — but twenty-three stays twenty-three</text></g>'
    '<text x="110" y="360" font-size="12" text-anchor="middle" class="grey">J</text>'
    '<text x="168" y="360" font-size="12" text-anchor="middle" class="grey">F</text>'
    '<text x="226" y="360" font-size="12" text-anchor="middle" class="grey">M</text>'
    '<text x="284" y="360" font-size="12" text-anchor="middle" class="grey">A</text>'
    '<text x="342" y="360" font-size="12" text-anchor="middle" class="grey">M</text>'
    '<text x="400" y="360" font-size="12" text-anchor="middle" class="grey">J</text>'
    '<text x="458" y="360" font-size="12" text-anchor="middle" class="grey">J</text>'
    '<text x="516" y="360" font-size="12" text-anchor="middle" class="grey">A</text>'
    '<text x="574" y="360" font-size="12" text-anchor="middle" class="green">S</text>'
    '<text x="632" y="360" font-size="12" text-anchor="middle" class="grey">O</text>'
    '<text x="690" y="360" font-size="12" text-anchor="middle" class="grey">N</text>'
    '<text x="748" y="360" font-size="12" text-anchor="middle" class="grey">D</text>'
)

S[31] = (
    '<g class="f1">' + grid(30, 280, 120, cols=6, dx=34, dy=34, r=7, hi=(7, 8)) + '</g>'
    '<g class="f2"><text x="400" y="330" font-size="26" text-anchor="middle" class="math">a class of 30 — <tspan fill="#6FCF97">70.6%</tspan></text></g>'
    '<g class="f3"><text x="400" y="370" font-size="18" text-anchor="middle" class="grey">try it on your own class — count the pairs</text></g>'
)

S[32] = (
    '<g class="f1">' + grid(23, 90, 150, cols=5, dx=22, dy=22, r=5, hi=(6, 7)) +
    grid(23, 310, 150, cols=5, dx=22, dy=22, r=5, hi=(11, 12)) +
    grid(23, 530, 150, cols=5, dx=22, dy=22, r=5, hi=(3, 4)) + '</g>'
    '<g class="f2">'
    '<text x="155" y="300" font-size="15" text-anchor="middle" class="grey">group A</text>'
    '<text x="375" y="300" font-size="15" text-anchor="middle" class="grey">group B</text>'
    '<text x="595" y="300" font-size="15" text-anchor="middle" class="grey">group C</text></g>'
    '<g class="f3"><text x="400" y="350" font-size="20" text-anchor="middle" class="math">three groups of 23 — one of them almost certainly has a match</text></g>'
)

S[33] = (
    '<g class="f1"><text x="400" y="120" font-size="18" text-anchor="middle" class="grey">365 days — 365 slots</text>'
    '<rect x="80" y="140" width="640" height="60" fill="url(#calgrid)"/></g>'
    '<g class="f2"><circle cx="400" cy="260" r="11" fill="#6FCF97" class="bob"/>'
    '<line x1="400" y1="275" x2="400" y2="300" stroke="#6FCF97" stroke-width="2"/>'
    '<polygon points="400,312 392,300 408,300" fill="#6FCF97"/>'
    '<text x="400" y="350" font-size="20" text-anchor="middle" class="grey">person 366 — no day left</text></g>'
    '<g class="f3 arrive"><text x="400" y="405" font-size="36" text-anchor="middle" class="math green">guaranteed — 100%</text></g>'
)

S[34] = (
    '<g class="f1">'
    + row(8, 120, 150, dx=80, r=8)
    + row(8, 160, 210, dx=60, r=6)
    + row(8, 200, 270, dx=45, r=4.5)
    + row(8, 230, 320, dx=34, r=3.5)
    + '</g>'
    '<g class="f2"><text x="400" y="380" font-size="30" text-anchor="middle" class="math">count pairs, not people</text></g>'
    '<g class="f3"><text x="400" y="415" font-size="18" text-anchor="middle" class="grey">the crowd looks big — the pairs are bigger</text></g>'
)

S[35] = (
    '<g class="f1"><rect x="170" y="220" width="70" height="60" rx="8" fill="#212120" stroke="#fff" stroke-width="2"/>'
    '<path d="M 185 220 V 200 A 20 20 0 0 1 225 220" fill="none" stroke="#fff" stroke-width="2"/>'
    '<text x="205" y="320" font-size="16" text-anchor="middle" class="grey">security</text></g>'
    '<g class="f2"><rect x="365" y="220" width="70" height="60" rx="8" fill="#212120" stroke="#fff" stroke-width="2"/>'
    '<circle cx="365" cy="250" r="6" fill="#000"/><circle cx="435" cy="250" r="6" fill="#000"/>'
    '<text x="400" y="320" font-size="16" text-anchor="middle" class="grey">lotteries</text></g>'
    '<g class="f3"><path d="M 540 200 C 570 220, 570 240, 540 260 M 610 200 C 580 220, 580 240, 610 260" fill="none" stroke="#fff" stroke-width="2"/>'
    '<line x1="552" y1="215" x2="598" y2="215" stroke="#9A9A9A" stroke-width="1.5"/>'
    '<line x1="548" y1="230" x2="602" y2="230" stroke="#9A9A9A" stroke-width="1.5"/>'
    '<line x1="552" y1="245" x2="598" y2="245" stroke="#9A9A9A" stroke-width="1.5"/>'
    '<text x="575" y="320" font-size="16" text-anchor="middle" class="grey">DNA tests</text></g>'
    '<text x="400" y="370" font-size="18" text-anchor="middle" class="grey">the same maths, everywhere</text>'
)

S[36] = (
    '<g class="f1">' + row(11, 150, 180, dx=50, r=8, fill="#fff") + '</g>'
    '<g class="f2">' + row(11, 150, 280, dx=50, r=8, fill="#464845") + '</g>'
    '<g class="f3"><circle cx="400" cy="340" r="8" fill="#6FCF97"/>'
    '<text x="400" y="380" font-size="18" text-anchor="middle" class="grey">eleven against eleven — plus the referee: twenty-three people, 253 pairs</text></g>'
)

S[37] = (
    '<rect x="180" y="130" width="440" height="55" rx="8" fill="#212120"/>'
    '<rect x="180" y="200" width="440" height="55" rx="8" fill="#212120"/>'
    '<rect x="180" y="278" width="440" height="60" rx="8" fill="#6FCF97"/>'
    '<g class="f1"><text x="400" y="170" font-size="32" text-anchor="middle" class="math">23 people → <tspan fill="#6FCF97">50.7%</tspan></text></g>'
    '<g class="f2"><text x="400" y="240" font-size="32" text-anchor="middle" class="math">70 people → <tspan fill="#6FCF97">99.9%</tspan></text></g>'
    '<g class="f3"><text x="400" y="320" font-size="36" text-anchor="middle" class="math ink pulse">366 people → 100%</text></g>'
)

S[38] = (
    '<g class="f1"><text x="400" y="200" font-size="56" text-anchor="middle" class="math">twenty-three people.</text></g>'
    '<g class="f2 arrive"><text x="400" y="270" font-size="56" text-anchor="middle" class="math"><tspan fill="#6FCF97">253</tspan> chances.</text></g>'
    '<g class="f3"><text x="400" y="330" font-size="22" text-anchor="middle" class="grey">one shared birthday</text></g>'
    + row(23, 90, 392, dx=28, r=4, hi=(5, 6))
)

# --- captions (trimmed line text; key phrase bold) ---
CAPS = [
    "<b>Twenty-three people.</b> In any room, the odds are better than even that two share a birthday.",
    "Most people guess <b>around 180.</b> The real answer is 23.",
    "A classroom, a party, a football team — <b>twenty-three people is enough.</b>",
    "Your brain asks the <b>wrong question:</b> will someone share MY birthday?",
    "To match YOUR birthday you would need <b>253 other people</b> in the room.",
    "There is only one of you. Every new person gets <b>one chance in 365.</b>",
    "The real question is different: does <b>ANY two</b> people share a birthday?",
    "Every pair is a chance. With 23 people, how many pairs is that? <b>23 + 22 + … + 1.</b>",
    "23 × 22 ÷ 2 = <b>253 pairs.</b> Two hundred and fifty-three chances.",
    "Each pair is small — <b>1 in 365.</b> But there are 253 of them.",
    "253 is also how many OTHER people you would need <b>to match your birthday.</b> Same number, two questions.",
    "Two kinds of comparison: <b>23 against one</b>, or 253 against 253.",
    "The trick: count the opposite. What is the chance <b>nobody</b> shares?",
    "Person one: any day is free. <b>365 out of 365.</b>",
    "Person two: <b>364 out of 365</b> — any day except the first person's.",
    "Multiply them all: <b>365 × 364 × … × 343</b>, over 365 to the power 23.",
    "The chance nobody shares: <b>49.3%</b> — less than half.",
    "So flip it. 100 minus 49.3 is <b>50.7%</b>. More likely than not.",
    "The curve starts slow: 10 people, <b>11.7%</b>. 15 people, 25.3%.",
    "Then it tips: 20 people, <b>41.1%</b> — 22 people, 47.6%.",
    "At 23, it crosses the line: <b>50.7%.</b>",
    "Every new person adds <b>more pairs than the last.</b> The growth accelerates.",
    "At 30, it is <b>70.6%</b>. At 40, 89.1%. At 50, 97%.",
    "At 70 people, <b>99.9%</b> — as certain as anything gets.",
    "The curve is an S: flat, then steep, then <b>flat again at the top.</b>",
    "365 days, only 23 people — <b>most days stay empty.</b> The pairs do the work.",
    "Why 23 and not 50? Because 23 people make <b>253 pairs</b> — and 30 make 435.",
    "Every handshake is a comparison. <b>253 handshakes</b> in a room of 23.",
    "The odds rise like a wave, not a staircase. <b>Each step is bigger.</b>",
    "Birthdays are not spread evenly — but <b>it barely matters.</b>",
    "Try it: in a class of 30, the chance is <b>70.6%</b>.",
    "Three groups of 23 — <b>one of them almost certainly</b> has a match.",
    "With 366 people, a match is <b>guaranteed</b> — there are only 365 days.",
    "Your intuition counts people. <b>The maths counts pairs.</b>",
    "The same maths runs <b>security, lotteries and DNA tests.</b>",
    "A football team is enough. <b>Pairs grow faster than people.</b>",
    "23 people, <b>50.7%</b>. 70 people, 99.9%. 366 people, 100%.",
    "Twenty-three people. <b>Two hundred and fifty-three chances.</b> One shared birthday.",
]


def main():
    v3 = V3.read_text(encoding="utf-8")
    css = v3.split("<style>", 1)[1].split("</style>", 1)[0]
    js_funcs = v3.split("let elapsed=0", 1)[1].split("</script>", 1)[0]
    # adapt the v2.5 JS: countUp now counts to 253, triggered at scene 9 (index 8)
    js_funcs = (js_funcs
                .replace("count38", "count253")
                .replace("Math.round(38*e)", "Math.round(253*e)")
                .replace("if(i===22) countUp();", "if(i===8) countUp();"))

    timing = json.loads((AUDIO / "timing.json").read_text())
    starts, durations, total = timing["starts"], timing["durations"], timing["total"]
    assert len(starts) == 38 == len(CAPS) == len(S)
    scenes_js = ",\n".join(
        ' {t0:%s,  dur:%s, cap:%s}' % (starts[i], durations[i], json.dumps(CAPS[i]))
        for i in range(38))

    scenes_svg = []
    for i in range(1, 39):
        scenes_svg.append(
            f'    <!-- {i} -->\n'
            f'    <g class="scene" id="s{i}">\n'
            f'      <text x="40" y="48" class="eyebrow">{EYEBROW[i]}</text>\n'
            f'      {S[i]}\n      {MARK}\n    </g>')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Why 23 People Is Enough — The Birthday Paradox — Median style, v1.0 + voiceover</title>
<style>{css}</style>
</head>
<body>
<div class="wrap">
  <h1>Why 23 People Is Enough — The Birthday Paradox <span>— Median style, v1.0</span></h1>
  <p class="sub">Video 04 in the series. Black background #000, one object in the centre, serif maths + sans headings, only 2 meaningful accents. Crossfade 0.45s, blur on the outgoing scene only (≤3px), incoming sharp. Median motion language — slow blur-in entrances, lines drawing on over 2.5s, gentle 5–6s breathing loops, at most 2 things moving at once, scene clock from performance.now() wall time. Captions stagger 0 / 0.8 / 1.6s. Voice: Muse TTS avocado_v2:vd2_quivering_oak, English, speed 80 (voice B).</p>

  <div class="stage">
  <svg viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <pattern id="dotgrid" width="14" height="14" patternUnits="userSpaceOnUse">
        <circle cx="7" cy="7" r="3" fill="#464845"/>
      </pattern>
      <pattern id="calgrid" width="12" height="12" patternUnits="userSpaceOnUse">
        <rect x="1.5" y="1.5" width="9" height="9" fill="#212120" stroke="#464845" stroke-width="1"/>
      </pattern>
    </defs>
{chr(10).join(scenes_svg)}
  </svg>
  </div>

  <audio id="vo" src="rag-video-04-audio/rag-video-04-full-audio.mp3" preload="auto"></audio>
  <div class="caption" id="caption"></div>
  <div class="controls">
    <button id="playBtn">Play</button>
    <button id="restartBtn">Replay</button>
    <div class="progress" id="progress"><i id="bar"></i></div>
    <div class="time" id="time">0:00 / 10:28</div>
  </div>
  <p class="note"><b>Video 04 — Why 23 People Is Enough — The Birthday Paradox.</b> v1.0: one idea — your brain counts people, the maths counts pairs. 23 people make 253 pairs, so a shared birthday is more likely than not (50.7%). Voice: Muse TTS avocado_v2:vd2_quivering_oak, English, speed 80 (voice B), 1.0x — no speedup. Numbers verified by direct computation and cross-checked against Wikipedia's "Birthday problem": P(23) = 50.7%, P(30) = 70.6%, P(50) = 97.0%, P(70) = 99.9%, 366 people = 100% by the pigeonhole principle; matching YOUR birthday needs 253 other people. Sources in the publish pack.</p>
</div>
<script>
const scenes=[
{scenes_js},
];
const TOTAL={total};
let elapsed=0{js_funcs}</script>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({len(html)} bytes, TOTAL={total}s)")


if __name__ == "__main__":
    main()
