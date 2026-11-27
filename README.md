# Median-Style Videos — Workflow làm video giải thích hoạt hình phong cách Median

Workflow hoàn chỉnh để làm video giải thích theo phong cách kênh YouTube **Median** (@median-lab): nền đen, một vật thể ở giữa, chuyển động chậm gắn với lời thoại. Hai dạng đã làm xong: video ngắn ~1 phút tiếng Việt đăng Facebook Reels, và video dài 10–12 phút tiếng Anh cho kênh YouTube quốc tế.

> English: a complete, reusable workflow for making Median-style animated explainer videos — short Vietnamese videos (~1 min) for Facebook Reels, and long-form English videos (10–20 min) for international YouTube. Four finished videos are included as examples.

## Video đã làm bằng workflow này

| # | Chủ đề | Thời lượng (sau tăng tốc) | Reel |
|---|--------|---------------------------|------|
| 01 | RAG hoạt động như thế nào? | 48 giây | [facebook.com/reel/1797776648004105](https://facebook.com/reel/1797776648004105/) (bản 60s) · [bản nhanh 48s](https://facebook.com/reel/2332818500907222/) |
| 02 | Embedding là gì? | 55 giây | [facebook.com/reel/1142893768252712](https://facebook.com/reel/1142893768252712/) |
| 03 | Why GPS Would Fail in 2 Minutes Without Einstein (tiếng Anh) | 12:45 (bản cuối v2.5, 1.0x) | [YouTube](https://youtu.be/bqZfkYy7t8M) — xem [videos/03-gps/](videos/03-gps/) (kèm thumbnail + publish pack) |
| 04 | Why 23 People Is Enough — The Birthday Paradox (tiếng Anh) | 10:28 (bản cuối v1.1, 1.0x) | [YouTube](https://youtu.be/nV5hiMjqB9M) — xem [videos/04-birthday/](videos/04-birthday/) (kèm thumbnail + publish pack + 3 Shorts) |

## Quickstart — làm video mới trong 7 bước

```bash
# 0. Chuẩn bị: ffmpeg, python3, playwright + chromium, tts CLI
python3 -m playwright install chromium

# 1. Viết kịch bản + storyboard (xem WORKFLOW.md bước 1)
#    -> videos/03-ten-chu-de/kich-ban-storyboard.md, lines.txt (1 câu thoại / dòng)

# 2. Dựng animation từ template (xem WORKFLOW.md bước 2)
cp template/player.html videos/03-ten-chu-de/animation.html
#    ... vẽ 9 cảnh SVG, điền scenes[] với nhịp đo được ở bước 3 ...

# 3. Lồng tiếng, đo nhịp từng câu (video ngắn tiếng Việt: giọng A speed 90; video dài tiếng Anh: giọng B Quivering Oak speed 80, xem WORKFLOW.md §4)
python3 scripts/render_voice.py videos/03-ten-chu-de/lines.txt videos/03-ten-chu-de/audio/
#    -> vo-01.mp3 ... + JSON nhịp (starts, durations, total)

# 4. Trộn giọng + SFX + nhạc nền
python3 scripts/mix_audio.py videos/03-ten-chu-de/audio/ videos/03-ten-chu-de/mix.json assets/sfx/ videos/03-ten-chu-de/audio-full.mp3

# 5. Xuất video 1080p (ghi màn hình trình duyệt + mux tiếng)
python3 scripts/export_video.py videos/03-ten-chu-de/animation.html <TOTAL> videos/03-ten-chu-de/audio-full.mp3 videos/03-ten-chu-de/video-1080p.mp4

# 6. Tăng tốc 1.25x — CHỈ cho video ngắn tiếng Việt (60s -> ~48s, hình + tiếng vẫn khớp). Video dài tiếng Anh KHÔNG tăng tốc (1.0x, xem WORKFLOW.md §7)
bash scripts/speedup.sh videos/03-ten-chu-de/video-1080p.mp4 videos/03-ten-chu-de/video-1080p-fast.mp4

# 7. Đăng Reel lên page Bug 5h Chiều (xem WORKFLOW.md bước 7)
```

> Video dài tiếng Anh (video 03, 04) làm cùng 7 bước nhưng khác ở: kịch bản ~1.200–1.500 từ / 38 câu / 8 chương (WORKFLOW.md §2b), giọng B Quivering Oak speed 80 ở 1.0x, xuất hình theo thời gian thực 10–20 phút, và **không đăng Facebook** — deliverable là MP4 + thumbnail + publish pack cho YouTube (+ 2–3 Shorts cắt từ video dài, xem WORKFLOW.md §8).

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
    ├── 02-embedding/
    ├── 03-gps/               <- video dài tiếng Anh: + thumbnail.png, youtube-publish-pack.md, shorts/, channel-branding/
    └── 04-birthday/          <- video dài tiếng Anh thứ 2: + thumbnail.png, youtube-publish-pack.md, shorts/
```

Mỗi video gồm: `kich-ban-storyboard.md`, `lines.txt` (lời thoại), `animation.html`,
`mix.json` (nhịp giọng + SFX), `audio-full.mp3`, `video-1080p.mp4`, `video-1080p-fast.mp4`
(bản đăng). Video dài thêm `thumbnail.png` (1280x720) và `youtube-publish-pack.md`.

## Phong cách Median — tóm tắt 5 dòng

Nền đen #000, không gradient, không 3D. Một vật thể ở giữa, khoảng trống lớn.
Chữ toán serif trắng cỡ lớn + tiêu đề sans đậm. Chỉ 2 màu nhấn có ý nghĩa:
xanh periwinkle #7E9BFF (điểm được chọn), xanh mint #6FCF97 (câu hỏi).
Chuyển động: blur-in chậm 1.8s, vẽ đường 2.5s, hình mọc ra — 1 yếu tố mỗi lần, tối đa
2 thứ chuyển động cùng lúc, nhịp 5–10 giây / 1 hình. Chuyển cảnh dissolve 0.45s, blur chỉ ở cảnh đi, không cắt cứng. Đồng hồ cảnh chạy bằng `performance.now()` (xem WORKFLOW.md §3).

## License

MIT — dùng tự do, ghi nguồn là được.
