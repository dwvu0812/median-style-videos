# WORKFLOW — Làm video giải thích phong cách Median, từ ý tưởng tới Reel

Một tài liệu duy nhất, đủ để làm lại video từ đầu. Đã kiểm chứng bằng 2 video thật
(01 RAG, 02 Embedding) — cả hai đều đã đăng lên page Facebook Bug 5h Chiều.

---

## 0. Yêu cầu

- `ffmpeg`, `python3`, `node` (chỉ để kiểm tra cú pháp JS)
- Playwright + Chromium: `pip install playwright && python3 -m playwright install chromium`
  (Chrome hệ thống không chạy được trong môi trường này — dùng Chromium của Playwright.)
- TTS CLI `tts` trên PATH (giọng Muse, xem bước 3)
- `facebook-cli` đã kết nối (xem bước 7)

## 1. Chọn chủ đề — 1 ý duy nhất

Mỗi video chỉ nói **1 ý**, gói trong 1 câu. Ví dụ:

- RAG: "AI trả lời sai không phải vì nó dốt, mà vì nó đi thi mà không được mang tài liệu."
- Embedding: "Máy không hiểu chữ, máy chỉ hiểu số. Embedding là biến chữ thành số, để cái gì giống nhau thì đứng gần nhau."

Không lan man sang training, fine-tuning hay so sánh model. Mọi cảnh chỉ phục vụ 1 ý đó.

## 2. Kịch bản + storyboard

- ~150 từ, **9 câu thoại, 9 cảnh**. Mục tiêu đọc ở tốc độ giọng A (speed 90) khoảng 60 giây.
- Viết file `videos/NN-ten/kich-ban-storyboard.md`: bảng lời thoại + từng cảnh ghi rõ
  khung hình, chuyển động, chữ trên màn hình, âm thanh gắn theo chuyển động.
- Viết file `videos/NN-ten/lines.txt`: 1 câu thoại / 1 dòng, **đánh vần số ra chữ**
  ("năm trăm ký tự", "quý ba", "ba mảnh") vì TTS đọc số/chữ cái rất dở.
- Các con số kỹ thuật phải đúng project thật (ví dụ RAG: chunk 500 ký tự overlap 50,
  embedding Gemini `gemini-embedding-001`, lưu Chroma, retrieve top-3, trả lời kèm
  trích dẫn thật, không có tài liệu thì nói không biết). Không nêu số mình không chắc
  (ví dụ: không ghi số chiều vector vì chưa rõ project dùng 3072 hay 768).

## 3. Dựng animation từ template

```bash
cp template/player.html videos/NN-ten/animation.html
```

Player là 1 file HTML tự chứa: SVG 800x450 với 9 nhóm `<g class="scene">`, caption
dưới sân khấu, nút Phát / Xem lại + thanh tiến trình, thẻ `<audio>` trỏ tới bản mix.

### Bảng phong cách Median (đã xem trực tiếp 2 video trên kênh, không đoán từ thumbnail)

- Nền đen #000, không gradient, không 3D, không camera move. Một vật thể ở giữa,
  khoảng trống lớn. Flat 2D line art.
- Palette: trắng #FFFFFF chính, xám #9A9A9A phụ, charcoal #1A1A1A–#222222 tô nền.
  Chỉ 2 màu nhấn, dùng khi có ý nghĩa: periwinkle #7E9BFF (điểm được chọn),
  mint #6FCF97 (câu hỏi). Tô slate-blue #5F7FA8, slate đậm #3A4A5A.
- Chữ: (1) toán bằng serif kiểu KaTeX/Computer Modern, biến nghiêng, rất lớn;
  (2) tiêu đề bằng sans đậm, sentence case, eyebrow xám tracked-caps ("PHẦN 1").
  Không trộn 2 hệ trong 1 khung.
- Chuyển động: fade chậm, blur-in/out, đường vẽ dần, hình mọc ra. Một yếu tố mỗi lần,
  đồng bộ với 1 câu thoại. 5–10 giây / 1 hình, giữ lâu sau câu hỏi.
- Công thức hiện nguyên khối, lớn, ở giữa, serif trắng — không gõ từng chữ, không hộp màu
  (trừ hộp recap nhỏ góc phải trên).
- Wordmark nhỏ, mờ, góc dưới phải: `"ten-video — 0N"`. Không dùng logo Median.
- **Thumbnail họ dùng khối 3D phát sáng, nhưng trong video không có 3D, không xúc xắc,
  không nổ tung — đừng thêm.**

### Quy tắc chuyển cảnh (quan trọng — đã sửa sau video 01)

- Các cảnh xếp chồng, **không bao giờ `display:none`**:
  `.scene{display:block;opacity:0;transition:opacity .5s ease;pointer-events:none}`
  `.scene.active{opacity:1}` — cảnh cũ mờ dần trong khi cảnh mới hiện dần (crossfade).
- Trong cảnh: `.f1` fade 1.4s, `.f2` trễ 1.2s, `.f3` trễ 2.4s; draw/grow 1.6s.
  Tất cả dùng `ease-in-out` (không dùng linear).
- JS: `showScene(i)` chỉ chạy khi chỉ số cảnh **thực sự đổi** (nó được gọi mỗi 100ms);
  caption cũng fade (opacity 0 → đổi chữ sau ~180ms → opacity 1).
- **Lỗi khoảng nghỉ (tìm ra 2026-11-26):** giữa 2 câu thoại có ~1.2s không cảnh nào
  khớp (`findIndex` trả -1). **Không bao giờ** fallback sang cảnh cuối
  (`idx<0 ? scenes.length-1`) — nó nháy sang cảnh kết 8 lần/video (video 01 bản đăng
  vẫn dính lỗi này). Trong khoảng nghỉ, **giữ nguyên cảnh cũ** (không làm gì trong
  `tick()`); `goTo()` thì fallback về cảnh 0.

### Điền nhịp sau bước 3

Sau khi đo giọng (bước 3), điền vào mảng `scenes[]` trong `animation.html`:
`t0` = thời điểm bắt đầu từng câu, `dur` = độ dài từng câu, `TOTAL` = tổng thời lượng
bản mix. Trỏ `<audio src>` tới bản mix ở bước 4. Kiểm tra JS: trích phần `<script>`
ra file riêng rồi `node --check`.

## 4. Lồng tiếng — giọng A

Giọng hiện tại (user chọn 2026-11-25): `avocado_v2:vd2_smoky_teacup`, giọng nam Việt,
trung trầm, rõ, speed 90.

```bash
python3 scripts/render_voice.py videos/NN-ten/lines.txt videos/NN-ten/audio/
```

Script render từng câu thành `vo-01.mp3`..., đo độ dài từng câu bằng ffprobe, in JSON
`{durations, starts, total}` — starts: câu đầu ở 0.8s, các câu sau cách câu trước 1.2s.
Copy số này vào `scenes[]` (bước 3) và `mix.json` (bước 5).

Giọng khác đã thử (chỉ dùng khi user yêu cầu): Gemini TTS Charon (nam trầm, cần key
Gemini), ElevenLabs `JnYgWPGqZl8gyvnE7Mdm` "DgNguyen - Deep Northern Narrator"
(gói free hay bận, chưa thử được tiếng thật). Edge TTS bị chặn mạng — đừng thử lại.

## 5. Trộn giọng + SFX + nhạc nền

Viết `videos/NN-ten/mix.json`:

```json
{"voice_starts": [0.8, 5.408, ...], "total": 68.72,
 "sfx": [{"file": "sfx-whoosh.wav", "at": 1.5}, {"file": "sfx-pop.wav", "at": 10.2}]}
```

SFX trong `assets/sfx/` (5 file wav, tái dùng cho mọi video):
`whoosh` (mũi tên/đường vẽ), `pop` (chấm đáp xuống), `tick` (đếm/vạch thước),
`thud` (cảnh "không có tài liệu", nốt trầm), `chime` (recap). Gắn SFX vào đúng thời
điểm chuyển động, không chèn nhạc chung chung rồi hy vọng khớp.

Nhạc nền: pad sine 110Hz + 165Hz, rất nhỏ, chạy suốt.

```bash
python3 scripts/mix_audio.py videos/NN-ten/audio/ videos/NN-ten/mix.json assets/sfx/ videos/NN-ten/audio-full.mp3
```

Script trộn bằng ffmpeg (voice adelay theo starts, SFX theo map, pad bên dưới),
đo peak rồi chuẩn hoá về -4.5 dB. Ra `audio-full.mp3`.

## 6. Xuất video 1080p

```bash
python3 scripts/export_video.py videos/NN-ten/animation.html <TOTAL> videos/NN-ten/audio-full.mp3 videos/NN-ten/video-1080p.mp4
```

Script tự tạo bản export của HTML (ẩn tiêu đề/caption/nút/ghi chú, sân khấu full
100vw x 100vh), ghi màn hình Chromium 1920x1080 trong lúc player chạy, cắt 1.5s
đoạn chờ trước khi bấm Phát, mux với bản mix (`libx264 yuv420p crf 20, AAC 160k`).

**Kiểm tra khung hình trước khi đăng:** trích 3 frame (đầu / giữa / cuối) bằng ffmpeg
và xem bằng mắt — cảnh đúng, chữ đúng, không nháy cảnh lạ trong khoảng nghỉ.

## 7. Tăng tốc 1.25x rồi đăng

Nhịp 60 giây bị user chê chậm (2026-11-25). Tăng tốc toàn bộ 1.25x, hình + tiếng
vẫn khớp nhau vì cả hai cùng co lại:

```bash
bash scripts/speedup.sh videos/NN-ten/video-1080p.mp4 videos/NN-ten/video-1080p-fast.mp4
# 60s -> ~48s. Kiểm tra 1 frame giữa video rồi mới đăng.
```

Đăng Reel lên page Bug 5h Chiều (page_id `1437664186102510`):

```bash
facebook-cli pages posts create --page-id '1437664186102510' \
  --text 'Dòng 1: câu chuyện.
Dòng 2: câu chuyện tiếp.
Dòng 3: ... — đó là <chủ đề>, <số giây> giây là hiểu.' \
  --privacy PUBLIC --file 'videos/NN-ten/video-1080p-fast.mp4'
```

- Caption: 3 dòng, giọng kể chuyện tự nhiên như nói với bạn, **không dòng trích nguồn**
  ("Bài gốc: ..." trông như AI), ghi đúng số giây của bản nhanh.
- Đọc lại bài đã đăng bằng `facebook-cli post read --post-id '<post_id>'` và gửi
  link Reel cho người xem.
- Quy tắc page: đăng bài hoàn chỉnh không cần hỏi lại từng lần; nội dung thật, không
  ảnh meme AI-generated; chờ ít nhất 6 tiếng giữa 2 bài.
- Hạn chế: bài Reel đã đăng **không xoá/sửa được qua facebook-cli** — đăng lại là
  tạo Reel mới, bài cũ phải xoá tay trên app Facebook nếu muốn.

## Checklist trước khi đăng

- [ ] Đọc thử kịch bản thành tiếng, bấm giờ: 55–65 giây (giọng A, speed 90)
- [ ] Đủ 9 cảnh, mỗi cảnh 1 ý, chuyển cảnh crossfade không cắt cứng
- [ ] Xem không bật tiếng vẫn hiểu ~80% (chữ trên màn hình đủ rõ)
- [ ] Nghe không nhìn hình vẫn hiểu câu chuyện
- [ ] Không dòng "Bài gốc", không credit AI, không hình AI-generated
- [ ] Đã tăng tốc 1.25x, caption ghi đúng số giây mới
- [ ] Đã xem 3 frame kiểm tra (đầu/giữa/cuối), không nháy cảnh lạ

## Các lỗi đã gặp (đừng lặp lại)

- Thumbnail Median dùng 3D phát sáng nhưng trong video không có — đừng thêm 3D.
- Giọng TTS đầu tiên ("Measured Sundial", nam Mỹ trầm) đọc tiếng Việt nghe chán —
  dùng giọng A, đừng quay lại giọng đó.
- Edge TTS bị chặn mạng (SSL tới speech.platform.bing.com) — đừng thử lại.
- Gemini TTS có thể 429 ở câu cuối — chờ ~65s rồi render lại đúng câu đó.
- Trong widget chat, animation chạy theo timer riêng, audio có thể không tự phát —
  mở file HTML trên trình duyệt thì hình + tiếng chạy cùng nhau.
- GitHub web upload làm phẳng thư mục — upload từng thư mục riêng, hoặc push bằng git.
