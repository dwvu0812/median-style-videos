#!/usr/bin/env python3
"""Generate rag-video-03-animation.html from scene specs + measured timing.

Usage:
    python3 build_animation_03.py <timing.json> <out.html>

timing.json: {"starts": [...], "durations": [...], "total": ...}
Scenes are defined below (38 scenes, one per spoken line).
"""
import html
import json
import sys

MARK = '<text x="770" y="430" text-anchor="end" class="mark">gps — 03</text>'

# (eyebrow, svg body, caption html)
SCENES = [
("WHY GPS NEEDS EINSTEIN",
 """<text x="400" y="180" font-size="30" text-anchor="middle" class="math">your phone</text>
      <g class="f1"><rect x="350" y="210" width="100" height="160" rx="14" fill="none" stroke="#fff" stroke-width="2"/></g>
      <g class="f2"><circle cx="400" cy="120" r="26" fill="none" stroke="#fff" stroke-width="2"/><line x1="400" y1="120" x2="400" y2="100" class="thin"/><line x1="400" y1="120" x2="414" y2="126" class="thin"/></g>
      <g class="f3"><text x="400" y="405" font-size="18" text-anchor="middle" class="grey">a relativity experiment — every second</text></g>""",
 "<b>Your phone is running an experiment in relativity</b> — right now, in your pocket."),
("WHY GPS NEEDS EINSTEIN",
 """<g class="f1"><text x="400" y="230" font-size="96" text-anchor="middle" class="math blurIn">2 minutes</text></g>
      <g class="f2"><text x="400" y="290" font-size="20" text-anchor="middle" class="grey">not two days — two minutes</text></g>
      <g class="f3"><text x="400" y="330" font-size="18" text-anchor="middle" class="grey">then your maps stop working</text></g>""",
 "If Einstein had been wrong, <b>your maps would stop working in about two minutes.</b>"),
("WHY GPS NEEDS EINSTEIN",
 """<g class="f1"><circle cx="280" cy="220" r="46" fill="none" stroke="#9A9A9A" stroke-width="2"/><line x1="280" y1="220" x2="280" y2="188" stroke="#9A9A9A" stroke-width="2"/><line x1="280" y1="220" x2="300" y2="232" stroke="#9A9A9A" stroke-width="2"/><text x="280" y="310" font-size="17" text-anchor="middle" class="grey">ground</text></g>
      <g class="f2"><circle cx="520" cy="220" r="46" fill="none" stroke="#7E9BFF" stroke-width="2"/><line x1="520" y1="220" x2="520" y2="188" stroke="#7E9BFF" stroke-width="2"/><line x1="520" y1="220" x2="540" y2="232" stroke="#7E9BFF" stroke-width="2"/><text x="520" y="310" font-size="17" text-anchor="middle" class="blue">satellite</text></g>
      <g class="f3"><text x="400" y="370" font-size="18" text-anchor="middle" class="grey">one shape, two clocks</text></g>""",
 "Relativity sounds like black holes — not coffee shops. But you'll see why, <b>with one shape and two clocks.</b>"),
("PART 1 — A CLOCK, NOT A MAP",
 """<g class="f1"><text x="400" y="230" font-size="64" text-anchor="middle" class="math blurIn">GPS = a clock</text></g>
      <g class="f2"><text x="400" y="290" font-size="20" text-anchor="middle" class="grey">not a map</text></g>
      <g class="f3"><text x="400" y="330" font-size="18" text-anchor="middle" class="grey">a whole sky full of clocks</text></g>""",
 "Forget the map. <b>GPS is a clock</b> — a whole sky full of clocks."),
("PART 1 — A CLOCK, NOT A MAP",
 """<path d="M 80 400 A 420 420 0 0 1 720 400" class="thinG f1" fill="none"/>
      <g class="f2"><circle cx="400" cy="130" r="9" fill="#fff"/><circle cx="400" cy="130" r="20" fill="none" stroke="#fff" stroke-width="1" opacity=".4"/></g>
      <g class="f3"><text x="400" y="230" font-size="40" text-anchor="middle" class="math">20,200 km</text><text x="400" y="275" font-size="18" text-anchor="middle" class="grey">12,500 miles above you</text></g>""",
 "More than thirty satellites, <b>20,200 km</b> above you — each one broadcasting the time."),
("PART 1 — A CLOCK, NOT A MAP",
 """<g class="f1"><circle cx="200" cy="110" r="7" fill="#fff"/><circle cx="350" cy="80" r="7" fill="#fff"/><circle cx="480" cy="95" r="7" fill="#fff"/><circle cx="620" cy="115" r="7" fill="#fff"/></g>
      <g class="f2"><line x1="200" y1="117" x2="400" y2="300" stroke="#9A9A9A" stroke-width="1.5" stroke-dasharray="5 7"/><line x1="350" y1="87" x2="400" y2="300" stroke="#9A9A9A" stroke-width="1.5" stroke-dasharray="5 7"/><line x1="480" y1="102" x2="400" y2="300" stroke="#9A9A9A" stroke-width="1.5" stroke-dasharray="5 7"/><line x1="620" y1="122" x2="400" y2="300" stroke="#9A9A9A" stroke-width="1.5" stroke-dasharray="5 7"/></g>
      <g class="f3"><rect x="370" y="300" width="60" height="100" rx="10" fill="none" stroke="#fff" stroke-width="2"/><text x="400" y="415" font-size="18" text-anchor="middle" class="grey">4 signals</text></g>""",
 "Your phone listens to <b>four of them</b> and measures how long each signal took."),
("PART 1 — A CLOCK, NOT A MAP",
 """<g class="f1"><text x="250" y="240" font-size="72" text-anchor="middle" class="mathI">x</text><text x="350" y="240" font-size="72" text-anchor="middle" class="mathI">y</text><text x="450" y="240" font-size="72" text-anchor="middle" class="mathI">z</text></g>
      <g class="f2"><text x="560" y="240" font-size="72" text-anchor="middle" class="mathI blue">t</text></g>
      <g class="f3"><text x="400" y="320" font-size="18" text-anchor="middle" class="grey">four unknowns — three are position, one is time</text></g>""",
 "Four travel times solve <b>four unknowns</b>: x, y, z — and time itself."),
("PART 1 — A CLOCK, NOT A MAP",
 """<g class="f1"><circle cx="300" cy="220" r="9" fill="#9A9A9A"/><circle cx="400" cy="220" r="9" fill="#9A9A9A"/><circle cx="500" cy="220" r="9" fill="#9A9A9A"/></g>
      <g class="f2"><circle cx="400" cy="140" r="10" class="blue"/><text x="400" y="110" font-size="17" text-anchor="middle" class="blue">4th</text></g>
      <g class="f3"><text x="400" y="300" font-size="20" text-anchor="middle" class="math">the 4th satellite measures your clock error</text></g>""",
 "Why four, not three? The fourth exists to measure <b>your phone's own clock error.</b>"),
("PART 2 — LIGHT-SPEED TIMING",
 """<g class="f1"><line x1="80" y1="225" x2="720" y2="225" class="thin draw"/></g>
      <g class="f2"><text x="400" y="180" font-size="40" text-anchor="middle" class="math">c = 300,000 km/s</text></g>
      <g class="f3"><text x="400" y="300" font-size="18" text-anchor="middle" class="grey">no room for almost</text></g>""",
 "Signals travel at <b>the speed of light</b> — 300,000 km every second."),
("PART 2 — LIGHT-SPEED TIMING",
 """<g class="f1"><line x1="150" y1="220" x2="650" y2="220" class="thin"/><line x1="150" y1="205" x2="150" y2="235" class="thin"/><line x1="275" y1="210" x2="275" y2="230" class="thin"/><line x1="400" y1="210" x2="400" y2="230" class="thin"/><line x1="525" y1="210" x2="525" y2="230" class="thin"/><line x1="650" y1="205" x2="650" y2="235" class="thin"/></g>
      <g class="f2"><text x="400" y="160" font-size="48" text-anchor="middle" class="math">1 ns = 30 cm</text></g>
      <g class="f3"><text x="400" y="300" font-size="18" text-anchor="middle" class="grey">about a foot — a school ruler</text></g>""",
 "In one nanosecond, light travels <b>30 cm</b> — about a foot."),
("PART 2 — LIGHT-SPEED TIMING",
 """<g class="f1"><text x="400" y="180" font-size="36" text-anchor="middle" class="math">1 ns wrong → 30 cm off</text></g>
      <g class="f2"><text x="400" y="250" font-size="36" text-anchor="middle" class="math">10 ns wrong → 3 m off</text></g>
      <g class="f3"><text x="400" y="320" font-size="18" text-anchor="middle" class="grey">billionths decide everything</text></g>""",
 "1 ns wrong = 30 cm off. <b>10 ns wrong = 3 m off.</b>"),
("PART 2 — LIGHT-SPEED TIMING",
 """<g class="f1"><circle cx="400" cy="210" r="70" fill="none" stroke="#fff" stroke-width="1.5"/><circle cx="400" cy="210" r="40" fill="none" stroke="#fff" stroke-width="1.5"/><circle cx="400" cy="210" r="6" fill="#fff"/></g>
      <g class="f2"><text x="400" y="330" font-size="30" text-anchor="middle" class="math">5–10 m</text></g>
      <g class="f3"><text x="400" y="370" font-size="18" text-anchor="middle" class="grey">timed to a few billionths of a second</text></g>""",
 "GPS promises <b>5–10 m</b> accuracy — timed to a few billionths of a second."),
("PART 3 — SPEED SLOWS TIME",
 """<path d="M 120 380 A 380 380 0 0 1 680 380" class="thinG f1" fill="none"/>
      <g class="f2"><circle cx="400" cy="140" r="9" fill="#fff"/></g>
      <g class="f3"><text x="400" y="230" font-size="40" text-anchor="middle" class="math">3.9 km/s</text><text x="400" y="275" font-size="18" text-anchor="middle" class="grey">twice around the Earth, every day</text></g>""",
 "Each satellite races at <b>3.9 km/s</b> — around the Earth twice a day."),
("PART 3 — SPEED SLOWS TIME",
 """<g class="f1"><circle cx="280" cy="210" r="46" fill="none" stroke="#fff" stroke-width="2"/><line x1="280" y1="210" x2="280" y2="178" class="thin"/><line x1="280" y1="210" x2="302" y2="222" class="thin"/><text x="280" y="300" font-size="17" text-anchor="middle" class="grey">still — on Earth</text></g>
      <g class="f2"><circle cx="520" cy="210" r="46" fill="none" stroke="#7E9BFF" stroke-width="2"/><line x1="520" y1="210" x2="520" y2="182" stroke="#7E9BFF" stroke-width="2"/><line x1="520" y1="210" x2="536" y2="218" stroke="#7E9BFF" stroke-width="2"/><text x="520" y="300" font-size="17" text-anchor="middle" class="blue">moving — in orbit</text></g>
      <g class="f3"><text x="400" y="360" font-size="20" text-anchor="middle" class="math">moving clocks run slow</text></g>""",
 "Special relativity: <b>a moving clock ticks more slowly.</b>"),
("PART 3 — SPEED SLOWS TIME",
 """<g class="f1"><text x="400" y="230" font-size="80" text-anchor="middle" class="math blurIn">−7 µs / day</text></g>
      <g class="f2"><text x="400" y="290" font-size="20" text-anchor="middle" class="grey">the satellite clock loses time</text></g>
      <g class="f3"><text x="400" y="330" font-size="18" text-anchor="middle" class="grey">special relativity · 1905</text></g>""",
 "The satellite clock loses <span class='b'>7 microseconds</span> every day."),
("PART 3 — SPEED SLOWS TIME",
 """<g class="f1"><text x="400" y="180" font-size="40" text-anchor="middle" class="math">7 µs / day</text></g>
      <g class="f2"><text x="400" y="240" font-size="28" text-anchor="middle" class="grey">↓</text></g>
      <g class="f3"><text x="400" y="300" font-size="40" text-anchor="middle" class="math">≈ 2 km / day</text></g>""",
 "1 µs = 300 m of error. So 7 µs a day is <b>about 2 km of error a day.</b>"),
("PART 3 — SPEED SLOWS TIME",
 """<g class="f1"><text x="220" y="230" font-size="40" text-anchor="middle" class="math blue">−7</text><text x="220" y="270" font-size="17" text-anchor="middle" class="grey">speed</text></g>
      <g class="f2"><text x="580" y="230" font-size="40" text-anchor="middle" class="math dim">+45</text><text x="580" y="270" font-size="17" text-anchor="middle" class="grey">height</text></g>
      <g class="f3"><text x="400" y="340" font-size="18" text-anchor="middle" class="grey">only half the story…</text></g>""",
 "That alone would break your maps. But speed is <b>only half the story.</b>"),
("PART 4 — GRAVITY SPEEDS TIME",
 """<g class="f1"><line x1="80" y1="150" x2="720" y2="150" class="thinG"/><path d="M 80 225 Q 400 260 720 225" class="thinG" fill="none"/><path d="M 80 300 Q 400 360 720 300" class="thinG" fill="none"/></g>
      <g class="f2"><circle cx="400" cy="225" r="55" fill="#1A1A1A" stroke="#fff" stroke-width="2"/></g>
      <g class="f3"><text x="400" y="370" font-size="20" text-anchor="middle" class="math">gravity bends time</text></g>""",
 "General relativity: <b>gravity slows time down.</b>"),
("PART 4 — GRAVITY SPEEDS TIME",
 """<g class="f1"><circle cx="280" cy="210" r="46" fill="none" stroke="#9A9A9A" stroke-width="2"/><line x1="280" y1="210" x2="280" y2="180" stroke="#9A9A9A" stroke-width="2"/><text x="280" y="300" font-size="17" text-anchor="middle" class="grey">slow down here</text></g>
      <g class="f2"><circle cx="520" cy="210" r="46" fill="none" stroke="#6FCF97" stroke-width="2"/><line x1="520" y1="210" x2="520" y2="176" stroke="#6FCF97" stroke-width="2"/><text x="520" y="300" font-size="17" text-anchor="middle" class="green">fast up there</text></g>
      <g class="f3"><text x="400" y="360" font-size="18" text-anchor="middle" class="grey">gravity is weaker in orbit</text></g>""",
 "Down here gravity is strong — clocks run slow. Up in orbit, <b>clocks run fast.</b>"),
("PART 4 — GRAVITY SPEEDS TIME",
 """<g class="f1"><text x="400" y="230" font-size="80" text-anchor="middle" class="math green blurIn">+45 µs / day</text></g>
      <g class="f2"><text x="400" y="290" font-size="20" text-anchor="middle" class="grey">the satellite clock gains time</text></g>
      <g class="f3"><text x="400" y="330" font-size="18" text-anchor="middle" class="grey">general relativity · 1915</text></g>""",
 "20,200 km up, clocks gain <span class='g'>45 microseconds</span> every day."),
("PART 4 — GRAVITY SPEEDS TIME",
 """<g class="f1"><circle cx="280" cy="210" r="46" fill="none" stroke="#9A9A9A" stroke-width="2"/><line x1="280" y1="210" x2="280" y2="180" stroke="#9A9A9A" stroke-width="2"/><text x="280" y="300" font-size="17" text-anchor="middle" class="grey">ground · +0</text></g>
      <g class="f2"><circle cx="520" cy="210" r="46" fill="none" stroke="#6FCF97" stroke-width="2"/><line x1="520" y1="210" x2="520" y2="176" stroke="#6FCF97" stroke-width="2"/><text x="520" y="300" font-size="17" text-anchor="middle" class="green">sky · +45 µs</text></g>
      <g class="f3"><text x="400" y="360" font-size="18" text-anchor="middle" class="grey">nothing moving, nothing broken — just gravity</text></g>""",
 "Two identical clocks — the sky one pulls ahead by <b>45 µs a day.</b>"),
("PART 4 — GRAVITY SPEEDS TIME",
 """<g class="f1"><text x="220" y="230" font-size="40" text-anchor="middle" class="math blue">−7</text><text x="220" y="270" font-size="17" text-anchor="middle" class="grey">speed</text></g>
      <g class="f2"><text x="580" y="230" font-size="40" text-anchor="middle" class="math green">+45</text><text x="580" y="270" font-size="17" text-anchor="middle" class="grey">height</text></g>
      <g class="f3"><line x1="270" y1="230" x2="530" y2="230" class="thinG"/><text x="400" y="340" font-size="18" text-anchor="middle" class="grey">a tug of war — and height is winning</text></g>""",
 "A tug of war: speed pulls slow by 7, height pushes fast by <b>45.</b>"),
("PART 5 — THE NET DRIFT",
 """<g class="f1"><text x="400" y="230" font-size="72" text-anchor="middle" class="math blurIn">45 − 7 = 38</text></g>
      <g class="f2"><text x="400" y="290" font-size="24" text-anchor="middle" class="grey">µs / day</text></g>
      <g class="f3"><text x="400" y="340" font-size="18" text-anchor="middle" class="grey">the net drift</text></g>""",
 "<b>45 − 7 = 38.</b> The satellite clock gains 38 microseconds a day."),
("PART 5 — THE NET DRIFT",
 """<g class="f1"><text x="400" y="210" font-size="56" text-anchor="middle" class="math">38 µs = 11 km / day</text></g>
      <g class="f2"><text x="400" y="270" font-size="20" text-anchor="middle" class="grey">about 7 miles — every single day</text></g>
      <g class="f3"><text x="400" y="320" font-size="18" text-anchor="middle" class="grey">a week: the wrong city · a month: the wrong country</text></g>""",
 "38 µs = <b>11 km of error a day</b> — about 7 miles."),
("PART 5 — THE NET DRIFT",
 """<g class="f1"><line x1="150" y1="240" x2="650" y2="240" class="thin"/><line x1="200" y1="228" x2="200" y2="252" class="thin"/><line x1="400" y1="228" x2="400" y2="252" class="thin"/><line x1="600" y1="228" x2="600" y2="252" class="thin"/></g>
      <g class="f2"><text x="400" y="180" font-size="56" text-anchor="middle" class="math">8 m / minute</text></g>
      <g class="f3"><text x="400" y="320" font-size="18" text-anchor="middle" class="grey">ticking upward, minute after minute</text></g>""",
 "The error grows <b>8 metres every minute</b> — and never stops."),
("PART 5 — THE NET DRIFT",
 """<g class="f1"><path d="M 200 320 H 320 V 270 H 440 V 220 H 560" class="thin draw" fill="none"/></g>
      <g class="f2"><text x="320" y="300" font-size="16" text-anchor="middle" class="grey">11 km</text><text x="440" y="250" font-size="16" text-anchor="middle" class="grey">11 km</text><text x="540" y="200" font-size="16" text-anchor="middle" class="grey">11 km</text></g>
      <g class="f3"><text x="400" y="370" font-size="18" text-anchor="middle" class="grey">it never resets — the error accumulates</text></g>""",
 "It never resets. Every day adds another <b>11 km</b> on top of yesterday's."),
("PART 5 — THE NET DRIFT",
 """<g class="f1"><text x="400" y="190" font-size="56" text-anchor="middle" class="math">2 minutes → 16 m</text></g>
      <g class="f2"><text x="400" y="260" font-size="28" text-anchor="middle" class="math">16 m &gt; 5–10 m</text></g>
      <g class="f3"><text x="400" y="320" font-size="18" text-anchor="middle" class="grey">the promise is broken — not a blackout</text></g>""",
 "After one minute: 8 m. After two minutes: <b>16 m</b>. The promise is broken."),
("PART 5 — THE NET DRIFT",
 """<g class="f1"><line x1="100" y1="280" x2="700" y2="280" class="thinG"/><line x1="100" y1="330" x2="700" y2="330" class="thinG"/></g>
      <g class="f2"><circle cx="560" cy="255" r="10" class="blue"/></g>
      <g class="f3"><text x="400" y="380" font-size="18" text-anchor="middle" class="grey">the wrong street — and the phone believes its own clock</text></g>""",
 "The screen doesn't go black. The dot just drifts to <b>the wrong street.</b>"),
("PART 6 — THE FIX",
 """<g class="f1"><circle cx="400" cy="150" r="9" fill="#fff"/><circle cx="400" cy="150" r="22" fill="none" stroke="#fff" stroke-width="1" opacity=".4"/></g>
      <g class="f2"><text x="400" y="230" font-size="30" text-anchor="middle" class="math">fix it before launch</text></g>
      <g class="f3"><text x="400" y="290" font-size="18" text-anchor="middle" class="grey">the fix is baked into the clock itself</text></g>""",
 "How do engineers fix it? They cheat — <b>before the satellite leaves the ground.</b>"),
("PART 6 — THE FIX",
 """<g class="f1"><text x="400" y="190" font-size="56" text-anchor="middle" class="math">10.23 MHz</text></g>
      <g class="f2"><text x="400" y="250" font-size="28" text-anchor="middle" class="grey">↓ set slow, on purpose ↓</text></g>
      <g class="f3"><text x="400" y="320" font-size="30" text-anchor="middle" class="math blue">10.22999999543 MHz</text></g>""",
 "Atomic clocks tick at <b>10.23 MHz</b> — but are set to run slow before launch."),
("PART 6 — THE FIX",
 """<g class="f1"><text x="400" y="210" font-size="56" text-anchor="middle" class="math">−0.004567 Hz</text></g>
      <g class="f2"><text x="400" y="280" font-size="28" text-anchor="middle" class="math">= 38 µs / day</text></g>
      <g class="f3"><text x="400" y="340" font-size="18" text-anchor="middle" class="grey">exactly as Einstein predicted</text></g>""",
 "The offset is less than 0.005 Hz — <b>exactly the 38 µs a day Einstein predicted.</b>"),
("PART 6 — THE FIX",
 """<g class="f1"><text x="250" y="230" font-size="24" text-anchor="middle" class="math">wrong on Earth</text></g>
      <g class="f2"><line x1="330" y1="222" x2="470" y2="222" class="thin draw"/></g>
      <g class="f3"><text x="560" y="230" font-size="24" text-anchor="middle" class="math blue">right in space</text></g>""",
 "A clock <b>wrong on Earth, on purpose</b> — because it will be right in space."),
("PART 6 — THE FIX",
 """<g class="f1"><rect x="370" y="280" width="60" height="100" rx="10" fill="none" stroke="#fff" stroke-width="2"/><circle cx="200" cy="110" r="7" fill="#fff"/><circle cx="350" cy="80" r="7" fill="#fff"/><circle cx="480" cy="95" r="7" fill="#fff"/><circle cx="620" cy="115" r="7" fill="#fff"/></g>
      <g class="f2"><line x1="200" y1="117" x2="400" y2="280" stroke="#7E9BFF" stroke-width="1.5" stroke-dasharray="5 7"/><line x1="350" y1="87" x2="400" y2="280" stroke="#7E9BFF" stroke-width="1.5" stroke-dasharray="5 7"/><line x1="480" y1="102" x2="400" y2="280" stroke="#7E9BFF" stroke-width="1.5" stroke-dasharray="5 7"/><line x1="620" y1="122" x2="400" y2="280" stroke="#7E9BFF" stroke-width="1.5" stroke-dasharray="5 7"/></g>
      <g class="f3"><text x="400" y="415" font-size="18" text-anchor="middle" class="grey">4th unknown = your own clock error</text></g>""",
 "Your phone solves for its own clock error — <b>corrected by the sky.</b>"),
("PART 6 — THE FIX",
 """<g class="f1"><rect x="330" y="170" width="140" height="70" rx="8" fill="none" stroke="#fff" stroke-width="2"/><line x1="400" y1="170" x2="400" y2="240" class="thin"/></g>
      <g class="f2"><text x="365" y="215" font-size="22" text-anchor="middle" class="math">ON</text><text x="435" y="215" font-size="22" text-anchor="middle" class="math dim">OFF</text></g>
      <g class="f3"><text x="400" y="300" font-size="18" text-anchor="middle" class="grey">1977 · NTS-2 — the drift matched Einstein</text></g>""",
 "1977, NTS-2: correction on, correction off — <b>the drift matched Einstein.</b>"),
("PART 6 — THE FIX",
 """<g class="f1"><circle cx="200" cy="330" r="7" fill="#fff"/><circle cx="400" cy="120" r="7" fill="#fff"/><circle cx="600" cy="330" r="7" fill="#fff"/><line x1="200" y1="330" x2="400" y2="120" class="thinG"/><line x1="400" y1="120" x2="600" y2="330" class="thinG"/><line x1="200" y1="330" x2="600" y2="330" class="thinG"/></g>
      <g class="f2"><text x="200" y="370" font-size="16" text-anchor="middle" class="grey">ground station</text><text x="400" y="95" font-size="16" text-anchor="middle" class="grey">satellite</text><text x="600" y="370" font-size="16" text-anchor="middle" class="grey">your phone</text></g>
      <g class="f3"><text x="400" y="230" font-size="20" text-anchor="middle" class="math">fresh corrections, every day</text></g>""",
 "Nothing pretends relativity doesn't exist. <b>Fresh corrections, every day.</b>"),
("RECAP",
 """<g class="f1"><text x="400" y="230" font-size="64" text-anchor="middle" class="math blurIn">time → space</text></g>
      <g class="f2"><text x="400" y="290" font-size="20" text-anchor="middle" class="grey">your phone finds where you are by measuring time</text></g>
      <g class="f3"><text x="400" y="330" font-size="18" text-anchor="middle" class="grey">30 cm per nanosecond</text></g>""",
 "Your phone finds where you are <b>by measuring time.</b>"),
("RECAP",
 """<g class="f1"><text x="400" y="170" font-size="36" text-anchor="middle" class="math blue">speed: −7 µs / day</text></g>
      <g class="f2"><text x="400" y="240" font-size="36" text-anchor="middle" class="math green">height: +45 µs / day</text></g>
      <g class="f3"><text x="400" y="320" font-size="44" text-anchor="middle" class="math">net: +38 µs / day</text></g>""",
 "Speed: −7. Height: +45. Net: <b>+38 µs a day.</b>"),
("RECAP",
 """<g class="f1"><text x="400" y="210" font-size="40" text-anchor="middle" class="math blurIn">wrong on the ground,</text></g>
      <g class="f2"><text x="400" y="270" font-size="40" text-anchor="middle" class="math blue">right in the sky</text></g>
      <g class="f3"><text x="400" y="340" font-size="18" text-anchor="middle" class="grey">your phone tests Einstein — every second, in your pocket</text></g>""",
 "Build the clock wrong on the ground, so it is <b>right in the sky.</b>"),
]

CSS = """  *{box-sizing:border-box}
  body{margin:0;background:#000;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#fff}
  .wrap{max-width:820px;margin:0 auto;padding:16px}
  h1{font-size:16px;margin:4px 0 2px;font-weight:600;color:#fff}
  h1 span{color:#9A9A9A}
  .sub{color:#9A9A9A;font-size:12px;margin:0 0 12px;line-height:1.5}
  .stage{position:relative;width:100%;aspect-ratio:16/9;background:#000;overflow:hidden}
  svg{width:100%;height:100%;display:block}
  /* SMOOTH TRANSITIONS: scenes stack, crossfade 0.5s, never display:none */
  .scene{display:block;opacity:0;transition:opacity .5s ease;pointer-events:none}
  .scene.active{opacity:1;pointer-events:auto}
  .eyebrow{font-size:12px;letter-spacing:.28em;fill:#9A9A9A;font-weight:600}
  .head{font-size:26px;font-weight:700;fill:#fff}
  .math{font-family:"Times New Roman",Georgia,serif;fill:#fff}
  .mathI{font-family:"Times New Roman",Georgia,serif;font-style:italic;fill:#fff}
  .grey{fill:#9A9A9A}
  .dim{opacity:.28}
  .blue{fill:#7E9BFF}.green{fill:#6FCF97}
  .blueS{stroke:#7E9BFF}.greenS{stroke:#6FCF97}
  .thin{stroke:#fff;stroke-width:1.5;fill:none}
  .thinG{stroke:#9A9A9A;stroke-width:1.5;fill:none}
  .fillChar{fill:#1A1A1A}
  .fillSlate{fill:#3A4A5A}
  .fillBlue{fill:#5F7FA8}
  .mark{font-size:12px;fill:#9A9A9A}
  /* Median motion: no camera moves. Slow fade, line draws, shape grows. One element at a time. ease-in-out. */
  .active .f1{animation:fade 1.4s ease-in-out both}
  .active .f2{animation:fade 1.4s 1.2s ease-in-out both}
  .active .f3{animation:fade 1.4s 2.4s ease-in-out both}
  @keyframes fade{from{opacity:0}to{opacity:1}}
  .active .draw{stroke-dasharray:600;stroke-dashoffset:600;animation:draw 1.6s .3s ease-in-out forwards}
  @keyframes draw{to{stroke-dashoffset:0}}
  .active .grow{animation:grow 1.6s .6s ease-in-out both;transform-origin:center;transform-box:fill-box}
  @keyframes grow{from{transform:scaleX(0);opacity:0}to{transform:scaleX(1);opacity:1}}
  .active .blurIn{animation:blurIn 1.6s ease-in-out both}
  @keyframes blurIn{from{opacity:0;filter:blur(8px)}to{opacity:1;filter:blur(0)}}
  .caption{min-height:54px;padding:12px 2px 0;font-size:16px;line-height:1.55;color:#fff;transition:opacity .18s ease}
  .caption b{color:#fff}
  .caption .b{color:#7E9BFF}.caption .g{color:#6FCF97}
  .controls{display:flex;gap:12px;align-items:center;margin-top:10px}
  button{background:none;border:1px solid #555;color:#fff;border-radius:999px;padding:8px 16px;cursor:pointer;font-size:14px}
  button:hover{border-color:#fff}
  .progress{flex:1;height:2px;background:#222;cursor:pointer}
  .progress i{display:block;height:100%;background:#fff;width:0%}
  .time{font-size:12px;color:#9A9A9A;min-width:80px;text-align:right}
  .note{font-size:12px;color:#9A9A9A;margin-top:14px;line-height:1.6}
  .note b{color:#fff}
"""

JS_TEMPLATE = """const scenes=[
__SCENES__
];
const TOTAL=__TOTAL__;
let elapsed=0, playing=false, timer=null, currentIdx=-1;
const capEl=document.getElementById('caption'), bar=document.getElementById('bar'), timeEl=document.getElementById('time'), playBtn=document.getElementById('playBtn');
function fmt(s){return Math.floor(s/60)+':'+String(Math.floor(s%60)).padStart(2,'0')}
function showScene(i){
  if(i===currentIdx) return;
  currentIdx=i;
  scenes.forEach((s,j)=>{
    document.getElementById('s'+(j+1)).classList.toggle('active', j===i);
  });
  capEl.style.opacity=0;
  setTimeout(()=>{ capEl.innerHTML=scenes[i].cap; capEl.style.opacity=1; },180);
}
function tick(){
  elapsed+=0.1;
  if(elapsed>=TOTAL){ pause(); elapsed=TOTAL; }
  const idx=scenes.findIndex((s,i)=> elapsed>=s.t0 && elapsed < s.t0+s.dur);
  if(idx>=0) showScene(idx); // gap between lines: KEEP the current scene, never jump to another
  bar.style.width=(elapsed/TOTAL*100)+'%';
  timeEl.textContent=fmt(elapsed)+' / '+fmt(TOTAL);
}
function play(){ if(elapsed>=TOTAL){ elapsed=0; currentIdx=-1; } playing=true; playBtn.textContent='Pause'; timer=setInterval(tick,100); const a=document.getElementById('vo'); if(a){ a.currentTime=elapsed; a.play().catch(()=>{}); } }
function pause(){ playing=false; playBtn.textContent='Play'; clearInterval(timer); const a=document.getElementById('vo'); if(a) a.pause(); }
function goTo(t){ elapsed=t; const a=document.getElementById('vo'); if(a){ a.currentTime=t; if(playing) a.play().catch(()=>{}); } const i=scenes.findIndex((s)=> t>=s.t0 && t < s.t0+s.dur); currentIdx=-1; showScene(i<0?0:i); bar.style.width=(elapsed/TOTAL*100)+'%'; timeEl.textContent=fmt(elapsed)+' / '+fmt(TOTAL); }
playBtn.onclick=()=> playing?pause():play();
document.getElementById('restartBtn').onclick=()=>{ goTo(0); play(); };
document.getElementById('progress').onclick=function(e){ const r=this.getBoundingClientRect(); goTo((e.clientX-r.left)/r.width*TOTAL); };
showScene(0);
"""


def main():
    timing = json.loads(open(sys.argv[1]).read())
    out_path = sys.argv[2]
    starts = timing["starts"]
    durations = timing["durations"]
    total = timing["total"]
    assert len(starts) == len(SCENES) == len(durations), (
        f"scene count mismatch: starts={len(starts)} scenes={len(SCENES)}")

    groups = []
    for i, (eb, body, cap) in enumerate(SCENES, 1):
        groups.append(
            f'    <!-- {i} -->\n'
            f'    <g class="scene" id="s{i}">\n'
            f'      <text x="40" y="48" class="eyebrow">{html.escape(eb)}</text>\n'
            f'      {body}\n'
            f'      {MARK}\n'
            f'    </g>')

    scene_rows = []
    for t0, d, (_, _, cap) in zip(starts, durations, SCENES):
        scene_rows.append(
            f' {{t0:{t0},  dur:{d}, cap:"{cap}"}},')
    js = JS_TEMPLATE.replace("__SCENES__", "\n".join(scene_rows)).replace("__TOTAL__", str(total))

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Why GPS Would Fail in 2 Minutes Without Einstein — Median style, v1.0 + voiceover</title>
<style>
{CSS}</style>
</head>
<body>
<div class="wrap">
  <h1>Why GPS Would Fail in 2 Minutes Without Einstein <span>— Median style, v1.0</span></h1>
  <p class="sub">Video 03 in the series. Black background #000, one object in the centre, serif maths + sans headings, only 2 meaningful accents. Crossfade 0.5s, ease-in-out. Voice: Muse TTS avocado_v2:vd2_smoky_teacup, English, speed 105.</p>

  <div class="stage">
  <svg viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg">
{chr(10).join(groups)}
  </svg>
  </div>

  <audio id="vo" src="rag-video-03-audio/rag-video-03-full-audio.mp3" preload="auto"></audio>
  <div class="caption" id="caption"></div>
  <div class="controls">
    <button id="playBtn">Play</button>
    <button id="restartBtn">Replay</button>
    <div class="progress" id="progress"><i id="bar"></i></div>
    <div class="time" id="time">0:00 / {int(total // 60)}:{int(total % 60):02d}</div>
  </div>
  <p class="note"><b>Video 03 — Why GPS Would Fail in 2 Minutes Without Einstein.</b> Long-form Median style: black background #000, one centred object, large white serif maths + bold sans headings, only 2 meaningful accents — periwinkle <b style="color:#7E9BFF">#7E9BFF</b> for the satellite / special relativity, mint <b style="color:#6FCF97">#6FCF97</b> for height / general relativity. Numbers verified: SR −7 µs/day, GR +45 µs/day, net +38 µs/day ≈ 11 km/day ≈ 8 m/min; factory offset 10.22999999543 MHz.</p>
</div>
<script>
{js}</script>
</body>
</html>
"""
    open(out_path, "w", encoding="utf-8").write(page)
    print(f"wrote {out_path} ({len(SCENES)} scenes, TOTAL={total}s)")


if __name__ == "__main__":
    main()
