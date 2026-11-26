#!/bin/bash
# Speed the finished video up 1.25x (picture + voice stay in sync).
# 60s raw -> ~48s final. The user found the 60s pace too slow (2026-11-25).
# Usage: bash scripts/speedup.sh videos/02-embedding/video-1080p.mp4 videos/02-embedding/video-1080p-fast.mp4
set -e
ffmpeg -y -v error -i "$1" \
  -filter_complex "[0:v]setpts=0.8*PTS[v];[0:a]atempo=1.25[a]" \
  -map "[v]" -map "[a]" \
  -c:v libx264 -pix_fmt yuv420p -crf 20 -c:a aac -b:a 160k -movflags +faststart "$2"
echo "sped up: $2"
