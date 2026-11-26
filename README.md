# Median-Style Videos — Workflow làm video giải thích hoạt hình phong cách Median

Workflow hoàn chỉnh để làm video giải thích ngắn (khoảng 1 phút) theo phong cách kênh YouTube **Median** (@median-lab): nền đen, một vật thể ở giữa, chuyển động chậm gắn với lời thoại, giọng đọc Bắc trầm, đăng lên Facebook Reels.

> English: a complete, reusable workflow for making short Median-style animated explainer videos in Vietnamese — script, SVG animation player, voiceover, 1080p export, Facebook Reels. Two finished videos are included as examples.

## Video đã làm bằng workflow này

| # | Chủ đề | Thời lượng (sau tăng tốc) | Reel |
|---|--------|---------------------------|------|
| 01 | RAG hoạt động như thế nào? | 48 giây | [facebook.com/reel/1797776648004105](https://facebook.com/reel/1797776648004105/) (bản 60s) · [bản nhanh 48s](https://facebook.com/reel/2332818500907222/) |
| 02 | Embedding là gì? | 55 giây | [facebook.com/reel/1142893768252712](https://facebook.com/reel/1142893768252712/) |

## Quickstart — làm video mới trong 7 bước

```bash
# 0. Chuẩn bị: ffmpeg, python3, playwright + chromium, tts CLI
python3 -m playwright install chromium

# 1. Viết kịch bản + storyboard (xem WORKFLOW.md bước 1)
#    -> videos/03-ten-chu-de/kich-ban-storyboard.md, lines.txt (1 câu thoại / dòng)

# 2. Dựng animation từ template (xem WORKFLOW.md bước 2)
cp template/player.html videos/03-ten-chu-de/animation.html
#    ... vẽ 9 cảnh SVG, điền scenes[] với nhịp đo được ở bước 3 ...

# 3. Lồng tiếng giọng A, đo nhịp từng câu
python3 scripts/render_voice.py videos/03-ten-chu-de/lines.txt videos/03-ten-chu-de/audio/
#    -> vo-01.mp3 ... + JSON nhịp (starts, durations, total)

# 4. Trộn giọng + SFX + nhạc nền
python3 scripts/mix_audio.py videos/03-ten-chu-de/audio/ videos/03-ten-chu-de/mix.json assets/sfx/ videos/03-ten-chu-de/audio-full.mp3

# 5. Xuất video 1080p (ghi màn hình trình duyệt + mux tiếng)
python3 scripts/export_video.py videos/03-ten-chu-de/animation.html <TOTAL> videos/03-ten-chu-de/audio-full.mp3 videos/03-ten-chu-de/video-1080p.mp4

# 6. Tăng tốc 1.25x (60s -> ~48s, hình + tiếng vẫn khớp)
bash scripts/speedup.sh videos/03-ten-chu-de/video-1080p.mp4 videos/03-ten-chu-de/video-1080p-fast.mp4

# 7. Đăng Reel lên page Bug 5h Chiều (xem WORKFLOW.md bước 7)
```

**Chi tiết từng bước, bảng phong cách Median, và các lỗi đã gặp: xem [WORKFLOW.md](WORKFLOW.md).**

## Cấu trúc repo

```
├── README.md                 <- bạn đang đọc
├── WORKFLOW.md               <- workflow hoàn chỉnh, 1 tài liệu duy nhất
├── template/
│   └── player.html           <- khung animation (SVG + JS), chuyển cảnh crossfade mượt
├── scripts/
│   ├── render_voice.py       <- lồng tiếng từng câu + đo nhịp
│   ├── mix_audio.py          <- trộn giọng + SFX + nhạc nền
│   ├── export_video.py       <- ghi màn hình -> mp4 1080p
│   └── speedup.sh            <- tăng tốc 1.25x
├── assets/sfx/               <- whoosh, pop, tick, thud, chime (wav)
└── videos/
    ├── 01-rag/               <- kịch bản, animation, audio mix, mp4
    └── 02-embedding/
```

Mỗi video gồm: `kich-ban-storyboard.md`, `lines.txt` (lời thoại), `animation.html`,
`mix.json` (nhịp giọng + SFX), `audio-full.mp3`, `video-1080p.mp4`, `video-1080p-fast.mp4`
(bản đăng).

## Phong cách Median — tóm tắt 5 dòng

Nền đen #000, không gradient, không 3D. Một vật thể ở giữa, khoảng trống lớn.
Chữ toán serif trắng cỡ lớn + tiêu đề sans đậm. Chỉ 2 màu nhấn có ý nghĩa:
xanh periwinkle #7E9BFF (điểm được chọn), xanh mint #6FCF97 (câu hỏi).
Chuyển động: fade, vẽ đường, hình mọc ra — 1 yếu tố mỗi lần, nhịp 5–10 giây / 1 hình.
Chuyển cảnh crossfade 0.5s, ease-in-out, không cắt cứng.

## License

MIT — dùng tự do, ghi nguồn là được.
