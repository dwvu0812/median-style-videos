# WORKFLOW — Làm video giải thích phong cách Median, từ ý tưởng tới Reel

Một tài liệu duy nhất, đủ để làm lại video từ đầu. Đã kiểm chứng bằng 3 video thật:
01 RAG và 02 Embedding (video ngắn ~60s, tiếng Việt, đã đăng lên page Facebook
Bug 5h Chiều) và 03 GPS (video dài 10–12 phút, tiếng Anh, cho kênh YouTube quốc tế —
bản nhanh cuối 8:13, kèm thumbnail).

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
  Chapter timestamps tính từ `mix.json` voice_starts (bản raw) chia cho 1.25, làm tròn
  xuống từng giây, đối chiếu với độ dài thật của bản nhanh.
- Video dài tiếng Anh **KHÔNG đăng lên page Bug 5h Chiều** — page đó là nội dung
  tiếng Việt. Deliverable là file MP4 + thumbnail (+ publish pack).

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
  cảnh mới hiện dần (crossfade 0.9s kèm blur dissolve; trước v2.1 chỉ 0.5s opacity).
- **Vào hình là blur-in chậm, không bao giờ bật ra:** `.f1/.f2/.f3` dùng
  `blurFade` 1.8s `cubic-bezier(.22,1,.36,1)` (opacity 0→1 + blur(8px)→0), trễ
  0s / 1.4s / 2.8s — một yếu tố mỗi lần, theo từng câu thoại. Khoảnh khắc lớn dùng
  `arrive` thay cho slam: scale 1.06→1 + blur(6px)→0 + fade, 1.8s, cùng đường cong.
  Số đếm trực tiếp (0→38) ease-out ~3s, không linear.
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
- **Giọng cuối cùng: Muse TTS giọng A, tiếng Anh, speed 105** — đọc lại hết 38 câu
  trong ~5 phút, một giọng thống nhất. Đánh đổi (user đã chấp nhận): giọng Anh mang
  âm Việt vì catalog chỉ có giọng Việt. `render_voice.py` mặc định speed 90 cho
  video tiếng Việt; video tiếng Anh dùng speed 105. Script trong `scripts/`:
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
100vw x 100vh), ghi màn hình Chromium 1920x1080 trong lúc player chạy, cắt 1.5s
đoạn chờ trước khi bấm Phát, mux với bản mix (`libx264 yuv420p crf 20, AAC 160k`).

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
vẫn khớp nhau vì cả hai cùng co lại. **1.25x là lựa chọn theo ý user, không phải
luật cứng** — video 03 (dài) vẫn giữ 1.25x theo ý user: raw 616.7s → bản nhanh
493.4s (8:13). Video dài vốn chậm có chủ ý theo kiểu Median; chỉ tăng tốc khi user
đã xem và thấy chậm.

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

**Checklist thêm cho video dài (video 03):**

- [ ] Có through-line 1 câu hỏi xuyên suốt + chuyện đời thường gắn vào
- [ ] 3 giây đầu là hình mạnh nhất; mỗi chương có 1 khoảnh khắc tương phản mạnh
- [ ] Thumbnail 1280x720 đã làm, đọc được ở cỡ nhỏ
- [ ] Đã xem 4–5 frame (hook/giữa/số chính/recap/cuối), hình–tiếng khớp ở **cuối**
- [ ] Publish pack (tiêu đề/mô tả/chapters/tags) đã viết xong
- [ ] Không đăng lên page Bug 5h Chiều (video tiếng Anh cho YouTube)

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
