# WORKFLOW — Làm video giải thích phong cách Median, từ ý tưởng tới Reel

Một tài liệu duy nhất, đủ để làm lại video từ đầu. Đã kiểm chứng bằng 3 video thật:
01 RAG và 02 Embedding (video ngắn ~60s, tiếng Việt, đã đăng lên page Facebook
Bug 5h Chiều), 03 GPS (video dài tiếng Anh, cho kênh YouTube quốc tế — bản cuối v2.5 12:45 ở tốc độ 1.0x, kèm thumbnail) và 04 Birthday Paradox (video dài tiếng Anh 10:28, bản cuối v1.1, kèm thumbnail + 3 Shorts).

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

**Video dài tiếng Anh thì chọn chủ đề khác:** lấy từ research về khán giả quốc tế
(xem `research_notes/science-topics-foreign-viewers-*/report.md`): đánh giá theo gu
người Mỹ / Anh / EU / Úc — **không lấy gu người Việt làm chuẩn** (ví dụ: video bài
giảng luyện thi rất mạnh ở Việt Nam nhưng yếu hẳn với khán giả tiếng Anh; RPM Việt
Nam ~$0.16 so với Mỹ ~$4.96). Video 03 chọn chủ đề #1 trong danh sách 25 chủ đề của
research: "Why GPS Would Fail in 2 Minutes Without Einstein" — điện thoại là một thí
nghiệm thuyết tương đối đang chạy trong túi.

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

## 2b. Video dài (long-form) — 10–12 phút, tiếng Anh (video 03)

Video ngắn 60s và video dài 10–12 phút khác nhau ở nhịp và cấu trúc, không khác ở
phong cách. Video 03 làm mẫu:

- **Kịch bản:** ~1.500 từ, **38 câu thoại, 38 cảnh, 8 chương**. Mỗi chương có eyebrow
  tiếng Anh ("PART 1", "PART 2", … "RECAP"). Cơ chế chính phải bắt đầu hé lộ trước
  phút thứ 3 — khoảng trống tò mò phải đóng dần từ sớm.
- **Một câu hỏi xuyên suốt (through-line)** mang cả video, ví dụ: "Your phone would
  lie to you by 11 km a day — unless Einstein saves it." (xuất hiện ở đầu và ở kết).
- **Gắn với đời thường:** bản đồ, giao hàng tìm đúng cửa, chạy bộ đo đúng đường.
  Người xem phải thấy chuyện này chạm tới họ, không phải bài giảng.
- **Luật story pass (thu hút nhưng dễ hiểu):** câu ngắn, từ đơn giản, không thuật ngữ
  nào để lại mà không giải thích ngay bằng hình. Câu nào cần bằng vật lý mới hiểu thì
  viết lại. Số liệu vẫn giữ đúng tuyệt đối (video 03: SR −7.2 µs/ngày, GR +45.7,
  net +38 µs/ngày ≈ 11 km/ngày ≈ 8 m/phút).
- **Diễn đạt cẩn thận:** "fails in 2 minutes" nghĩa là *lời hứa độ chính xác* vỡ
  (sai số ~16 m > 5–10 m GPS hứa), KHÔNG phải mất sóng — bản đồ vẫn vẽ, chấm chỉ
  trôi sang đường khác.
- **Bắt mắt (video làm cho người khác xem):** 3 giây đầu phải là hình mạnh nhất
  video (điện thoại + đồng hồ tích tắc + vòng mint nhấp nháy); mỗi chương có một
  khoảnh khắc tương phản mạnh (số khổng lồ 110–120px, đếm số trực tiếp 0→38, số dài
  màu xanh); màu nhấn dùng đậm tay ở đúng chỗ đó.
- **Thumbnail (bắt buộc cho YouTube):** 1280x720, nền đen, **một** yếu tố lớn, tối đa
  3–4 chữ (video 03: "2 MINUTES" khổng lồ + "WITHOUT EINSTEIN" periwinkle). Làm từ
  frame mạnh nhất, kiểm tra bằng mắt ở cỡ nhỏ vẫn đọc được. File
  `videos/03-gps/thumbnail.png`.
- **Publish pack:** viết sẵn tiêu đề, mô tả, chapters, tags vào
  `videos/NN-ten/youtube-publish-pack.md` (mẫu: `videos/03-gps/youtube-publish-pack.md`).
  Chapter timestamps tính từ `mix.json` voice_starts (bản raw), làm tròn xuống từng giây. Video dài tiếng Anh xuất ở 1.0x nên không chia gì cả (cách chia 1.25 cũ chỉ đúng khi còn tăng tốc, đã bỏ từ video 03 v2.4). Mô tả thêm, theo mẫu kênh Quaselo: 1 câu hỏi thảo luận cho bình luận + danh sách nguồn sau phần chapters.
- Video dài tiếng Anh **KHÔNG đăng lên page Bug 5h Chiều** — page đó là nội dung
  tiếng Việt. Deliverable là file MP4 + thumbnail (+ publish pack).
- **Quy tắc điện ảnh cho video dài — xem §9 (bắt buộc từ 2026-11-28):** đổi hình
  mỗi 2–5s, cảnh tối đa ~10s, `scenes[].events` xuyên suốt cảnh, morph giữa các
  cảnh (dissolve chỉ ở ranh giới chương), Write cho công thức/số chính mỗi cảnh,
  zoom tiết kiệm (một push-in mỗi phép tính), payoff NÓI RA trước 5 giây, mở vòng
  lặp trước ~0:18, móc lại mỗi 2–3 phút, hay nhất ở ~2/3, chương là chuỗi vòng lặp.
  Chạy `scripts/check_density.py` và phải PASS trước khi xuất — GPS v2.5 fail nó
  (5 sự kiện/60s đầu, payoff ở 18s).

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

### Quy tắc chuyển cảnh và motion (đã sửa sau video 01, tinh chỉnh ở video 03 v2.1)

- Các cảnh xếp chồng, **không bao giờ `display:none`**:
  `.scene{display:block;opacity:0;transition:opacity .9s ease,filter .9s ease;filter:blur(6px);pointer-events:none}`
  `.scene.active{opacity:1;filter:blur(0)}` — cảnh cũ mờ dần + nhòe dần trong khi
  cảnh mới hiện dần (dissolve 0.45s, blur chỉ ở cảnh ĐI — cảnh tới giữ nét; trước v2.2 là 0.9s blur cả hai chiều, làm ~1s mỗi lần chuyển đều mờ không đọc được).
- **Vào hình là blur-in chậm, không bao giờ bật ra:** `.f1..f6` dùng
  `blurFade` 1.8s `cubic-bezier(.22,1,.36,1)` (opacity 0→1 + blur(8px)→0), trễ
  0s / 2s / 4s / 6s / 8s / 10s (v3, 2026-11-28 — xem §9: mở rộng từ f1/f2/f3
  0/0.8/1.6s của v2.2 thành đồng hồ build xuyên suốt cảnh; muốn kích đúng cụm
  từ nói thì dùng `scenes[].events`) — một yếu tố mỗi lần, theo từng câu thoại.
  Khoảnh khắc lớn dùng `arrive` thay cho slam: scale 1.06→1 + blur(6px)→0 + fade,
  1.8s, cùng đường cong. Số đếm trực tiếp (0→38) chạy LINEAR ~3s, không ease-out
  (đuôi ease-out bị thước 1fps đọc là đóng băng).
- **Vẽ đường chậm:** `draw` 2.5s ease-in-out; đặt `pathLength="100"` lên đường/path
  và dùng `stroke-dasharray:100` để dash luôn là toàn bộ độ dài (dasharray 600 cũ
  từng để sót 40px cuối của một tia dài 640px). Hình mọc ra: ease-out chậm, không snap.
- **Tối đa 2 thứ chuyển động cùng lúc trong một cảnh.** Vòng lặp thở chậm: chu kỳ
  5–6s, biên độ nhỏ (breathe scale 1.03, opacity .92; pulse opacity .45–1; bob −6px;
  drift 10px), ease-in-out. Chấm bay SMIL: ~4–5s mỗi chuyến. **Ngoại lệ: quỹ đạo vệ
  tinh và kim đồng hồ giữ linear** — tốc độ không đổi là đúng vật lý.
- JS: `showScene(i)` chỉ chạy khi chỉ số cảnh **thực sự đổi** (nó được gọi mỗi 100ms);
  caption cũng fade (opacity 0 → đổi chữ sau ~180ms → opacity 1).
- **Đồng hồ cảnh PHẢI là `performance.now()`** — `elapsed = (performance.now() - startPerf) / 1000`,
  tính lại mỗi tick, `startPerf` reset trong `play()`/`goTo()`. Hai cách cũ đều sai:
  (1) accumulator `elapsed+=0.1` trong `setInterval(tick,100)` bị chậm ~1–2s ở cuối
  video 10 phút; (2) đồng hồ `<audio>` `currentTime` còn tệ hơn — dưới tải ghi hình,
  audio của headless Chromium chạy chậm ~2% (đo được: audio chỉ tiến ~58.7s sau 60s
  thời gian thực), hình chậm hơn tiếng ~13s ở cuối và cảnh cuối không bao giờ xuất hiện
  (bản export v2.1 đầu tiên, đã bỏ). Thẻ `<audio>` chỉ để nghe thử; video ghi xong
  mux với bản mix sau, nên cảnh phải theo thời gian tường, không theo audio.
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

**Video dài tiếng Anh (video 03) — đã thử cả 3 giọng, kết quả thật:**
- Gemini TTS Charon: đọc được 16/38 câu rồi dính tường 429 của gói free (~55 phút
  thử lại liên tục không xong). Đừng kỳ vọng render dài bằng Gemini free.
- ElevenLabs Magnus (giọng nam Anh trầm): đọc được 7 câu, rồi user từ chối phê duyệt
  connector và bỏ ElevenLabs hẳn. Giọng hay nhưng tốn credit (~200 credit/câu) và
  mỗi lần gọi cần phê duyệt — không hợp làm video dài.
- **Giọng cuối cùng (từ video 03 v2.3, dùng cho cả video 04): Muse TTS giọng B Quivering Oak (`avocado_v2:vd2_quivering_oak`, nam Anh rất trầm, median pitch 101 Hz), tiếng Anh, speed 80** — tốc độ thật 116.9 wpm ở 1.0x, nghe đúng như lúc thử giọng. Quy tắc tốc độ hiệu dụng: wpm cuối = wpm TTS × hệ số tăng tốc — giọng A ở TTS 105 × 1.25x ≈ 200 wpm nghe vội và méo, đó là lý do video dài tiếng Anh bỏ tăng tốc hẳn (xem §7). Giọng A (`vd2_smoky_teacup`, speed 90) vẫn dùng cho video ngắn tiếng Việt. `render_voice.py` mặc định speed 90 cho video tiếng Việt; video dài tiếng Anh dùng giọng B speed 80. Script trong `scripts/`:
  `render_voice_muse.py`, `render_voice_gemini.py`, `render_voice_elevenlabs.py`.

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
100vw x 100vh), ghi màn hình Chromium 1920x1080 trong lúc player chạy, cắt đúng độ lệch click ĐO ĐƯỢC (thời gian từ lúc tải trang tới khi bấm Phát: v2.2 đo 1.948s, v2.3 2.078s, v2.5 3.072s, video 04 v1.1 2.487s) — không bao giờ cắt cố định 1.5s, và `-ss` phải đặt TRƯỚC `-i` của video (đặt giữa 2 `-i` sẽ cắt nhầm AUDIO), mux với bản mix (`libx264 yuv420p crf 20, AAC 160k`).

Video dài ghi hình **theo thời gian thực**: video 10–12 phút thì ghi mất 10–12 phút,
chạy nền, đừng poll liên tục. Kiểm tra frame ở 4–5 mốc (hook, giữa, cảnh số chính,
recap, frame cuối) và **đối chiếu đồng bộ hình–tiếng ở cuối video**, không chỉ ở đầu.

**Gotcha Playwright:** sau khi VM thay mới, Playwright Python biến mất — cài lại
`pip3 install --break-system-packages playwright` (build Chromium trong
`~/.cache/ms-playwright/` vẫn còn, không cần tải lại).

**Kiểm tra khung hình trước khi đăng:** trích 3 frame (đầu / giữa / cuối) bằng ffmpeg
và xem bằng mắt — cảnh đúng, chữ đúng, không nháy cảnh lạ trong khoảng nghỉ.

## 7. Tăng tốc 1.25x rồi đăng

Nhịp 60 giây bị user chê chậm (2026-11-25). Tăng tốc toàn bộ 1.25x, hình + tiếng
vẫn khớp nhau vì cả hai cùng co lại. **1.25x CHỈ dùng cho video ngắn tiếng Việt.** Video dài tiếng Anh KHÔNG tăng tốc nữa (quy tắc từ video 03 v2.4, sau khi user chỉ ra tăng tốc làm giọng vội và méo, không giống lúc nghe thử): bản cuối chính là bản raw 1.0x — video 03 v2.5 là 765.28s (12:45), video 04 v1.1 là 627.6s (10:28). Nếu thấy chậm thì sửa kịch bản/tốc độ TTS, không tua nhanh audio đã xong.

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

**Video dài tiếng Anh thì không đăng Facebook** — deliverable là MP4 + thumbnail
(+ publish pack, xem §2b). Đăng YouTube bằng tay với publish pack.

## Checklist trước khi đăng

- [ ] Đọc thử kịch bản thành tiếng, bấm giờ: 55–65 giây (giọng A, speed 90)
- [ ] Đủ 9 cảnh, mỗi cảnh 1 ý, chuyển cảnh crossfade không cắt cứng
- [ ] Xem không bật tiếng vẫn hiểu ~80% (chữ trên màn hình đủ rõ)
- [ ] Nghe không nhìn hình vẫn hiểu câu chuyện
- [ ] Không dòng "Bài gốc", không credit AI, không hình AI-generated
- [ ] Đã tăng tốc 1.25x, caption ghi đúng số giây mới
- [ ] Đã xem 3 frame kiểm tra (đầu/giữa/cuối), không nháy cảnh lạ
- [ ] `check_density.py` PASS; bài kiểm tra xem lại (§9: gần-đóng-băng hook ≤10%, burst ≥25, mật độ hook ≥6, frame-diff sàng ≥1.5) đã ghi vào build note

**Checklist thêm cho video dài (video 03):**

- [ ] Có through-line 1 câu hỏi xuyên suốt + chuyện đời thường gắn vào
- [ ] 3 giây đầu là hình mạnh nhất; mỗi chương có 1 khoảnh khắc tương phản mạnh
- [ ] Thumbnail 1280x720 đã làm, đọc được ở cỡ nhỏ
- [ ] Đã xem 4–5 frame (hook/giữa/số chính/recap/cuối), hình–tiếng khớp ở **cuối**
- [ ] Publish pack (tiêu đề/mô tả/chapters/tags) đã viết xong
- [ ] Không đăng lên page Bug 5h Chiều (video tiếng Anh cho YouTube)
- [ ] `check_density.py` PASS trên 60 giây đầu (payoff nói ra trước 5 giây); bài kiểm tra xem lại §9 đã ghi vào build note

## 2c. Bài học review + đo Median thật (video 03 v2.2–v2.5, video 04 v1.1)

- Dissolve 0.45s, blur chỉ ở cảnh đi; vật chuyển động không bao giờ được chạy qua chữ (kiểm tra từng quỹ đạo/chấm bay với hộp chữ); hình hook chính phải lên màn hình trong 3 giây đầu; không cảnh nào chỉ có 2 dòng thoại mà kéo 17 giây; số kiểu "millionths" phải diễn đạt lại cho TTS ("seven parts in a million"); gạch chân dài đúng bề rộng chữ đo bằng `getBBox()`.
- Âm thanh: chuẩn hoá mix về khoảng −14 LUFS (mix giọng có crest factor cao nên trần thực tế ~−16.8 LUFS ở TP −1 — đừng nén giọng thêm; YouTube tự chuẩn hoá phần còn lại).
- **Đo Median thật (84 frame, pixel script): KHÔNG có light pool, glow, vignette hay gradient** — nền đen thuần (#000 / #0A0A0A). Cảm giác "điện ảnh" đến từ vật thể: khối tô đặc (charcoal #212120, xám #464845, slate-blue #6980A5), mặt khối tô 2 tông (mặt trên sáng hơn mặt bên, như có key light từ trên), mật độ ~8 yếu tố/khung (mình ~4), ink coverage median 2.9% toàn khung / 5.2% vùng giữa (mình 1.7% / 2.5%). Bố cục: 2 cột (sơ đồ + phép tính), cặp so sánh, đường kích thước + vạch + nhãn. Áp dụng ở video 03 v2.5 (ink vùng giữa 6.69%, hơi vượt Median) và video 04 v1.1 (đường cong xác suất thật + bảng people-vs-chance).
- **Chuẩn chất lượng (user đặt 2026-11-27): video phải là thứ mình tự hào và muốn xem lại; phải có giá trị tham khảo để người xem xem đi xem lại.** Trước khi gọi xong: xem lại toàn bộ bản cuối như người xem thật, ghi rõ đoạn nào muốn tua, khung nào muốn chụp lại, chỗ nào chán — sửa chỗ tệ nhất. Mỗi video cần ít nhất 2 khung "đáng chụp lại" (bảng tính/phép tính làm ra, không phải minh họa cho có); recap nói được trong 1 câu.

## 8. Cắt Shorts từ video dài — VERTICAL-NATIVE (đổi 2026-11-28, sau flop: Short cũ letterbox chỉ 4.1% / 31.8% ở lại)

Mỗi video dài cắt 2–3 Shorts (30–60s, 1 ý mỗi cái, hook 2 giây đầu), đăng mỗi ngày 1 cái: cái đầu công khai ngay, các cái sau hẹn 09:00 ICT.

- **Format: 1080x1920 full-bleed, vertical-native. KHÔNG letterbox.** Cách cũ (video 16:9 scale 1080x607 đặt giữa nền đen) đã nghỉ hưu: khung video chỉ 31.6% chiều cao khung hình và tự nó ~96% đen, nên frame 1 là 95–98% đen và 5 giây đầu không có gì chuyển động (median frame-diff 0.00–0.17) — đó là lý do Short flop. Dựng animation trực tiếp ở 1080×1920 (template dọc riêng), hoặc crop/zoom master 16:9 sao cho hình vẽ lấp đầy khung. Xem quy tắc đầy đủ ở skill §"Cinematic rules — Shorts".
- **Motion ngay frame 1:** Short bắt đầu giữa chuyển động (chấm đang chạy / số đang đếm), không fade-in, không title card tĩnh. Mục tiêu: median frame-diff 5 giây đầu ≥1.0.
- **Payoff to ngay frame 1 — TRONG HÌNH, không chỉ ở tiêu đề overlay:** một hình đầy khung + một dòng chữ khổng lồ (≤6 từ hoặc một con số) nêu payoff, đọc được khi tắt tiếng. Bài học từ cinematic v2: frame 1 của v2 chỉ có "+45 vs −7" và "= 0", không có "11 km/day" ở đâu cả — người xem trong feed phải đợi ~20s mới biết Short nói về cái gì. **Đặt payoff (to, mint) vào chính frame 1, gắn với phần setup** (ví dụ: tug-of-war ở trên, "11 km / day" khổng lồ ở dưới) — đừng đợi tới beat chứng minh mới nêu đáp án. Thắng thua ở feed quyết định trong ~1 giây đầu.
- **Dùng hết chiều cao dọc:** dựng bố cục cho toàn bộ 1080×1920 — rải yếu tố theo chiều dọc (eyebrow, vật chính, thước/bảng, payoff, phụ đề mỗi thứ một vùng riêng theo chiều dọc), làm vật chính cao hơn, và **không bao giờ để trống 1/3 khung hình**. Bài học từ cinematic v2: mọi bố cục v2 là một dải ngang nổi giữa nền đen — trên trống ~25%, dưới trống ~35% ở mọi khung hình. Vùng dùng được là y≈150–1330 (phụ đề ở 1335–1393, dưới y≈1420 để trống cho UI của YouTube).
- **Kết vòng lặp được:** giây cuối chảy về frame 1 để Short lặp lại mượt mà. H.264 + AAC 160k, yuv420p, faststart. Script: `videos/NN-ten/shorts/build_shorts.py` (bản cũ letterbox) — bản dựng vertical-native mới: `cinematic-v2/` trong thư mục Shorts của video (xem GPS Short 1 cinematic v2 làm mẫu).
- Mô tả Short gắn link video dài thật (điền sau khi video dài đã lên sóng). Nút "Related video" cần xác minh kênh 1 lần (xác minh bằng số điện thoại trong Studio) — chưa xác minh thì bỏ qua, chỉ dùng link trong mô tả.
- Ví dụ: GPS Shorts (`videos/03-gps/shorts/`, 3 cái, đã đăng 27/11) và Birthday Shorts (`videos/04-birthday/shorts/`, 3 cái, đã đăng 27/11).

## 9. Quy tắc điện ảnh — nhịp điệu, kể chuyện, hình ảnh (2026-11-28)

Ghi sau chẩn đoán flop 28/11: kênh 3 subs, video dài 10/0/0 lượt xem với 3/7/1
impressions; GPS Short 1: 186 lượt xem nhưng chỉ 4.1% ở lại. Audit đo được video
của mình là **slideshow có lồng tiếng** — một hình tĩnh cho mỗi câu thoại, hiệu
ứng vào xong trong ~3.4s rồi khung hình đóng băng ~15s — trong khi bên thắng thay
đổi hình mỗi giây. Thay đổi hình trung bình mỗi giây (~1fps, 320×180): mình ~0.2,
Median ~1.5, Animated Math ~3–5, 3Blue1Brown ~5–9. Birthday đóng băng 52%, Telescopes
43%; cảnh dài 11–19s (Median: 5–10s/hình); mình cắt cảnh mỗi ~13–19s trong khi
Animated Math ~1/134s, 3Blue1Brown ~1/1633s — họ biến hình, không cắt. Code KHÔNG
phải vấn đề (Median, Animated Math, 3B1B đều làm bằng code) — vấn đề là code của
mình làm ra cái gì. Các quy tắc dưới đây là bắt buộc, không phải nice-to-have,
và ngồi TRÊN bảng phong cách Median (§3) — không nới lỏng phong cách.

### Nhịp điệu — hình phải đổi mỗi giây
- Tần suất đổi hình: Shorts **mỗi 1–2s**, video dài **mỗi 2–5s**. "Đổi" là một biến
  đổi nhỏ (thêm yếu tố, biến hình, vật đang chạy, số đang đếm), KHÔNG phải cắt cảnh.
- Cảnh tối đa **~10s**. Câu thoại nào trên ~12s thì tách làm 2 hình, hoặc thêm
  build event giữa cảnh. GPS trung bình 18.9s/cảnh — mục tiêu ≤10s.
- **`build` (bắt buộc):** yếu tố hình mới mỗi **2–4s xuyên suốt cảnh**, không chỉ
  lúc vào. Mở rộng f1/f2/f3 thành f1…f6 (trễ 0/2/4/6/8/10s); cảnh nào ≥12s phải có
  ≥4 yếu tố dàn xếp, mỗi cái rơi đúng một cụm từ nói. Quy tắc cũ "tối đa 3 yếu tố,
  xong trong 3.4s đầu" đã bị thay — chính nó tạo ra slideshow.
- **Khôi phục `travel` (`<animateMotion>`) làm primitive bắt buộc.** Mỗi cảnh có
  một yếu tố chạy có mục đích: chấm chạy trên đường, xung chạy dọc dây, mốc trượt
  trên thước. GPS có 24 lần dùng; Birthday/Telescopes chỉ 1 lần mỗi video — tụt
  đó là lỗi review, không phải lựa chọn phong cách. Chú ý bài học GPS: chuyển động
  phải NHÌN THẤY (chấm to trên đường, số đang đếm), không chỉ "có mặt" (kim đồng
  hồ mỏng không nhúc nhích được thước đo).
- **Biến hình, đừng cắt.** Đổi toàn bộ hình mỗi ~13–19s bằng dissolve 0.45s là
  kiểu đổi gây xao lãng nhất mà lại chậm nhất. Ưu tiên fade, morph, push-in trong
  một không gian cảnh liên tục; cắt cứng hiếm (Animated Math ~1/134s, 3B1B ~1/1633s).
- **Thước frame-diff (chỉ để SÀNG, không để xếp hạng):** lấy mẫu ~1 khung/giây ở
  320×180, chênh lệch xám trung bình giữa 2 khung liên tiếp (0–255). **Median ≥1.5**
  là mức sàng — dưới 1.0 thì video là slideshow, thêm chuyển động, đừng xuất.
  Nhưng nó KHÔNG xếp hạng video thắng: Manim chậm (3B1B Neural Net, Reducible) và
  simulation của Primer đo 0.15–0.59 median giữa video, thấp như mình — chuyển động
  của họ nhỏ nhưng có ý nghĩa và liên tục (chấm bò, lưới biến dạng), còn mình thì
  không có gì. Các ngưỡng thật sự phân biệt nằm ở bài kiểm tra xem lại dưới đây.
  **Thước bị bóp trên video dọc — đã bác bỏ 28/11/2026:** Short v3 đo cùng một file
  ở 320×180 (legacy) và 180×320 (tỉ lệ gốc) cho số gần như giống hệt (median 1.65
  so với 1.64, gần-đóng-băng <0.2 là 2.1% cả hai) — bóp dọc KHÔNG giấu chuyển động.
  Điểm mù thật của thước là fade tương phản thấp: fade giữa hai khung gần như đen
  hoàn toàn chỉ đo ~0.1 dù mắt thấy rõ chuyển cảnh (giây 8→9 của v3, morph B1→B2).
  Vẫn báo CẢ hai tỉ lệ (legacy để so với audit/v2, gốc để đúng); nếu lệch nhau thì
  tin tỉ lệ gốc.

### Kể chuyện — cấu trúc giữ người xem
- **Payoff NÓI RA trong 5 giây.** Claim phải nói thành lời trong 5 giây đầu, số
  đầu tiên hiện trước 3 giây. GPS nói payoff ("2 minutes") ở giây 18 — quá muộn,
  dù hình đã có từ frame 1. Giọng và hình phải hạ payoff cùng lúc.
- **Mở vòng lặp trước ~0:18.** 30 giây đầu theo ngữ pháp chung của bên thắng:
  0:00–0:03 câu lạnh — hứa hẹn của tiêu đề hiện/nói ngay, không chào hỏi, không
  logo; 0:03–0:10 chứng minh tiêu đề bằng một ví dụ cụ thể; 0:10–0:18 nâng stakes /
  mở vòng lặp (tại sao quan trọng với *bạn*, bạn sẽ sai chỗ nào); 0:18–0:30 lộ
  trình một dòng, rồi rẽ cứng vào thân bài.
- **Móc lại mỗi 2–3 phút; khoảnh khắc hay nhất ở ~2/3.** Coi giữa video (~40–60%,
  điểm võng) như hook thứ hai: sự thật gây ngạc nhiên nhất, leo stakes, ngắt nhịp.
  Đặt khoảnh khắc hay nhất ở khoảng 2/3, không phải cuối — đa số người xem không
  bao giờ tới cuối.
- **Chương là chuỗi vòng lặp.** 3–6 chương, mỗi chương là mini ba hồi; **không bao
  giờ đóng một vòng lặp mà không mở vòng tiếp theo** — câu nhử/chuyển tiếp trước
  mỗi cuối chương ("nhưng cái thứ ba mới là cái làm số nhảy"). Payoff nhỏ giữa
  video để đường retention đi lên, không chỉ phẳng; callback trả một vòng cũ rồi
  mở vòng mới.
- **60 giây đầu phải xứng đáng với phút tiếp theo.** GPS giữ ~65% ở 0:30 rồi rơi
  xuống ~30% ở 1:00 — rò rỉ nằm ở phần setup (0:30–1:30), nơi video quay về nền
  trước payoff tiếp theo. Đổi hình ít nhất mỗi 5 giây trong phút đầu; không đoạn
  30 giây nào thiếu payoff, con số, hay sự kiện hình mới.

### Hình ảnh — các primitive còn thiếu (code trong template/player.html)
- **`morph` (biến hình):** một `<g id="stage">` bền vững ngoài các nhóm `.scene`
  giữ những yếu tố sống qua lần đổi cảnh. `flipMorph(el, applyNew, dur=1200)` —
  FLIP: đo bbox cũ, đặt thuộc tính mới, đảo bằng transform, animate về identity
  trong ~1.2s. `pathMorph(pathEl, toD, dur=1200)` — lấy mẫu cả hai path về cùng
  số điểm rồi nội suy `d`. Giữ dissolve 0.45s CHỈ ở ranh giới chương; trong chương
  thì morph.
- **`Write` (vẽ công thức):** class `.write` trên `<text>` SVG với
  `pathLength="100"`: `stroke-dasharray:100; stroke-dashoffset:100`, animate
  dashoffset 100→0 trong ~1.5s ease-in-out, rồi `fill-opacity 0→1` trong 0.6s.
  Một công thức/số chính mỗi cảnh, **≥48px** (chữ nhỏ nét vẽ bị mờ). Bắt đầu lúc
  cảnh active (`.active .write`); muốn vẽ giữa cảnh thì kích từ `scenes[].events`
  với `cls:'on'`.
- **`zoom` (camera viewBox):** `zoomTo(x, y, w, h, dur)` nội suy 4 số viewBox
  ease-in-out trên đồng hồ wall-clock (CSS không transition được viewBox). Khai
  báo: `scenes[].zoom = {x, y, w, h, dur, at}`. Tiết kiệm: một push-in mỗi phép
  tính làm ra, **1.15–1.4×, 3–5s**; không zoom tới mức chữ nhỏ nhất <14px ở
  1080p. KHÔNG phải hành vi Median — primitive của 3B1B/Animated Math.
- **`build` (đồng hồ sự kiện):** `scenes[].events = [{t, el, cls, sfx}]` — `t`
  tính bằng giây trong cảnh; `tick()` kích mỗi event đúng 1 lần. Cảnh ≥12s phải
  có ≥4 events, mỗi cái rơi đúng cụm từ nói.
- **`count` (số đếm tổng quát):** mọi `<text>` có `data-count="from:to:dur"` +
  `data-count-at="giây tuyệt đối"` sẽ đếm theo đồng hồ tường khi cảnh của nó
  active; `data-fmt`: `int` | `1dp` | `km` | `1dpkm`. LINEAR, không ease-out —
  đuôi ease-out chạy chậm dần và thước 1fps đọc đuôi đó là đóng băng.
- **`travel` + `trace` (bắt buộc):** mỗi cảnh một yếu tố chạy có mục đích
  (`<animateMotion>`, chấm r ≥ 6, tô đặc màu nhấn, thời lượng = thời lượng cảnh);
  `trace` là cùng đường đó với stroke-dashoffset chạy bằng JS trong TOÀN BỘ cảnh
  (không phải `draw` 2.5s rồi dừng). Vật chạy không bao giờ cắt qua chữ. Thiếu
  travel/trace trong một cảnh là lỗi review.
- **Kiểm tra mật độ hook trước khi xuất — `scripts/check_density.py`:**
  `python3 scripts/check_density.py <animation.html> --payoff "<regex>"`.
  FAIL (exit 1) trừ khi: sự kiện hình trong 60 giây đầu ≥6; không cảnh nào ≥12s
  có <4 events; payoff được nói trước 5 giây (kiểm tra với CAPTIONS[] cho Shorts,
  caps của scenes[] cho video dài — caps giữ số, nên dùng dạng caption, ví dụ
  `"two minutes|2 minutes"`). Script đếm những gì HTML khai báo — khai TẤT CẢ
  sự kiện build theo thời gian trong `events[]`, kể cả lúc bắt đầu đếm số và lúc
  morph, nếu không nó đếm thiếu. Đây là ngưỡng sàn, không phải xếp hạng: GPS v2.5
  FAIL (5 sự kiện/60s đầu, payoff ở 18s), cinematic-v2 PASS (20 sự kiện, payoff
  ở 2.26s).

### Video dài — cùng quy tắc, số của video dài
Quy tắc điện ảnh KHÔNG chỉ cho Shorts. Workflow video dài (§2b) mang cùng quy tắc
với số của video dài — chẩn đoán flop đo trên video dài trước (GPS retention ~65%
ở 0:30 → ~30% ở 1:00, Birthday đóng băng 52%, Telescopes 43%).
- Nhịp: đổi hình **mỗi 2–5s** (Shorts: 1–2s). Cảnh tối đa **~10s** — câu thoại nào
  trên ~12s thì tách làm 2 hình hoặc thêm build event giữa cảnh.
- Build: `scenes[].events` xuyên suốt cảnh; cảnh ≥12s phải có ≥4 events.
- Morph giữa các cảnh qua `<g id="stage">` + `flipMorph`/`pathMorph`; dissolve
  0.45s CHỈ ở ranh giới chương (video 03 có 8 chương — tối đa 7 dissolve cả video).
- Write cho công thức/số chính mỗi cảnh (≥48px). Zoom tiết kiệm — một push-in mỗi
  phép tính làm ra, 1.15–1.4×, 3–5s.
- Kể chuyện: payoff NÓI RA trước 5 giây; mở vòng lặp trước ~0:18; móc lại mỗi
  2–3 phút; hay nhất ở ~2/3; chương là chuỗi vòng lặp.
- Kiểm tra trước khi xuất: `check_density.py` kiểm tra cả 60 giây đầu của video
  dài (đọc `scenes[]` + caps) — phải PASS mới xuất. GPS v2.5 fail; đó chính là
  ý nghĩa của nó.
- Bài kiểm tra xem lại dưới đây áp dụng cho cả video dài lẫn Shorts (video dài:
  cửa sổ hook = 60 giây đầu; Shorts: 5 giây đầu).

**Chỉ-Shorts vs dùng chung.** Dùng chung (cả hai dạng): nhịp đổi hình (2–5s dài /
1–2s Shorts), trần cảnh, build events, morph-đừng-cắt, Write, zoom, count,
travel/trace, payoff trước 5 giây, mở vòng lặp, móc lại, chương chuỗi vòng lặp,
mật độ (§2c), bài kiểm tra xem lại. Chỉ-Shorts: dọc 1080×1920 full-bleed (không
letterbox), kết vòng lặp được, chữ payoff khổng lồ ngay frame 1, phụ đề đốt trong
vùng an toàn, một ý mỗi Short, 15–60 giây. Chỉ-video-dài: chương + through-line,
publish pack, thumbnail.

### Bài kiểm tra xem lại — có ngưỡng đã sửa (chuẩn chất lượng user đặt 27/11; sửa 28/11)
Trước khi gọi xong video, TẤT CẢ phải đạt. Sửa từ research kênh nổi tiếng (report
§0): **median frame-diff là thước SÀNG, không phải thước xếp hạng.** Nó bắt được
slideshow (mình ~0.2, nửa video gần-đóng-băng) so với Median/Animated Math/
Transformers (~2–4.5), nhưng KHÔNG xếp hạng video thắng — Manim chậm (3B1B Neural
Net, Reducible) và simulation của Primer đo 0.15–0.59 median giữa video, thấp như
mình, vì chuyển động của họ nhỏ nhưng có ý nghĩa và liên tục. Ngưỡng thật sự phân
biệt thắng với slideshow là (a), (b), (c) dưới đây.
1. **(a) Gần-đóng-băng trong cửa sổ hook ≤10%.** Trong 60 giây đầu (video dài) /
   5 giây đầu (Shorts), tối đa 10% số giây lấy mẫu được gần-đóng-băng (Δ<0.2).
   Bên thắng: 0–32% trong 60 giây đầu, 0% trong cửa sổ 25–35 giây; mình từng
   45–73%. Đây là ngưỡng video cũ rớt nặng nhất.
2. **(b) Độ bùng (burst size).** Thay đổi lớn nhất trong một giây (max Δ) phải
   **≥25** — bên thắng đổi hình là đổi LỚN (Animated Math 82, Reducible 83,
   3B1B-Transformers 28, Primer 55; mình 6–16 — cả lưới biến dạng, phương trình
   biến hình, camera push-in). Video mà giây lớn nhất chỉ là dissolve 0.45s thì
   vẫn là slideshow.
3. **(c) Mật độ hook.** **≥6 sự kiện hình trong 60 giây đầu** (bên thắng: 7 điểm
   gián đoạn trong riêng cửa sổ 25–35 giây; Kurzgesagt cắt mỗi 1.3–2.2 giây).
   Ép trước khi xuất bằng `check_density.py` — phải PASS mới xuất.
4. **Median frame-diff (chỉ sàng): ≥1.5** (Shorts 5 giây đầu ≥1.0) — đo trên bản
   xuất cuối ở tỉ lệ gốc (xem ghi chú thước bị bóp ở trên), ghi vào build note.
   Dưới 1.0 = slideshow, đừng xuất. Trên 1.5 = qua sàng, chưa chứng minh là hay —
   (a)–(c) mới quyết định.
5. **Thời gian đóng băng sau hiệu ứng vào ~0%** — không cảnh nào đứng yên sau khi
   hiệu ứng vào xong.
6. **≥2 khung "đáng chụp lại"** (bảng tính/phép tính làm ra mà người xem muốn chụp).
7. **Recap nói được trong 1 câu; hook trong 3 giây đầu; payoff nói ra trước 5 giây.**
8. **Bài kiểm tra con người, nói thật trong build note:** mình (người làm) có muốn
   xem lại không? Đoạn 10 giây nào muốn tua, khung nào muốn chụp, chỗ nào còn
   chán? Không tự khen — nêu lỗi tệ nhất còn lại và nó đã sửa hay cố tình để vậy.

## Các lỗi đã gặp (đừng lặp lại)

- Thumbnail Median dùng 3D phát sáng nhưng trong video không có — đừng thêm 3D.
- Giọng TTS đầu tiên ("Measured Sundial", nam Mỹ trầm) đọc tiếng Việt nghe chán —
  dùng giọng A, đừng quay lại giọng đó.
- Edge TTS bị chặn mạng (SSL tới speech.platform.bing.com) — đừng thử lại.
- Gemini TTS có thể 429 ở câu cuối — chờ ~65s rồi render lại đúng câu đó.
- Đồng hồ cảnh: `elapsed+=0.1` và `<audio>` currentTime đều sai ở video dài —
  chỉ dùng `performance.now()`, xem §3.
- Vẽ đường bằng dasharray cố định (600) có thể để sót đuôi — dùng `pathLength="100"`.
- Video 03 v1: chữ phụ bị đường quỹ đạo che — dời chữ lên trên đường quỹ đạo.
- Playwright Python mất sau khi VM thay mới — cài lại bằng pip, Chromium vẫn còn.
- Trong widget chat, animation chạy theo timer riêng, audio có thể không tự phát —
  mở file HTML trên trình duyệt thì hình + tiếng chạy cùng nhau.
- GitHub web upload làm phẳng thư mục — upload từng thư mục riêng, hoặc push bằng git.
