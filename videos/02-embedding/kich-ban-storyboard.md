# Video 02 — Embedding là gì?
## Kịch bản + Storyboard — phong cách Median / Clockwork

- **Chủ đề:** Embedding — nối tiếp cảnh 5 của video 01 (RAG), đào sâu 1 ý duy nhất
- **Độ dài mục tiêu:** ~60 giây đọc ở tốc độ giọng A (speed 90), sau tăng tốc 1.25x còn ~48 giây
- **Ngôn ngữ:** Tiếng Việt, giọng kể chuyện, không giọng AI
- **Phong cách hình:** Nền đen #000, 1 vật thể ở giữa, serif toán + sans tiêu đề, chỉ 2 màu nhấn (periwinkle #7E9BFF cho điểm được chọn, mint #6FCF97 cho câu hỏi) — theo đúng bảng phong cách Median đã kiểm chứng
- **Chuyển cảnh:** crossfade 0.5s giữa các cảnh (sửa từ video 01 vốn cắt cứng), easing ease-in-out — xem skill `median_video_production`

---

## Ý tưởng cốt lõi — 1 câu duy nhất

> Máy không hiểu chữ, máy chỉ hiểu số. Embedding là biến chữ thành số, để cái gì giống nhau thì đứng gần nhau.

Mọi cảnh chỉ phục vụ 1 ý này. Không lan man sang training, tokenization hay chiều vector cụ thể.

---

## Kịch bản — lời thoại từng câu (đọc đúng từng chữ)

| # | Lời thoại | Ghi chú |
|---|-----------|---------|
| 1 | Chữ thì máy không hiểu. Máy chỉ hiểu số. | Hook |
| 2 | Embedding là phép biến một câu thành một dãy số — một điểm trên bản đồ. | Định nghĩa |
| 3 | Ví dụ nhé: doanh thu quý ba và lợi nhuận quý ba, nghĩa gần nhau, nên hai điểm đứng gần nhau. | Gần |
| 4 | Còn doanh thu quý ba với cách nấu phở — chẳng liên quan gì, hai điểm đứng xa nhau. | Xa |
| 5 | Gần hay xa, máy đo bằng khoảng cách giữa hai điểm. Càng gần, càng giống nhau. | Khoảng cách = giống nhau |
| 6 | Trong project RAG của t, mỗi mảnh tài liệu năm trăm ký tự được biến thành một điểm như vậy, bằng Gemini. | Số thật trong project |
| 7 | Câu hỏi cũng thành một điểm, rồi máy tìm ba điểm gần nhất — đó là lúc RAG tìm tài liệu. | Nối về RAG |
| 8 | Không có embedding, máy không biết mảnh nào liên quan, nó chỉ còn cách đọc hết cả tài liệu, hoặc đoán mò. | Không có thì sao |
| 9 | Nên nhớ một câu thôi: embedding là biến chữ thành số, để cái gì giống nhau thì đứng gần nhau. | Tóm lại |

---

## Storyboard — từng cảnh, từng chuyển động

### Cảnh 1 — Hook: chữ → số (câu 1)
- **Khung hình:** Giữa màn hình, chữ serif nghiêng `a` màu xám mờ bên trái, một mũi tên mỏng vẽ sang phải, số serif trắng `0.42` bên phải. Dưới: `máy chỉ hiểu số`.
- **Chuyển động:** Mũi tên vẽ dần từ trái sang phải, số `0.42` blur-in khi mũi tên chạm tới. Giữ lâu 1 nhịp.
- **Chữ trên màn hình:** `chữ → số`
- **Âm thanh:** whoosh nhẹ khi mũi tên vẽ, tick khi số hiện.

### Cảnh 2 — Một câu thành một điểm (câu 2)
- **Khung hình:** Trên cùng, câu serif trắng `doanh thu quý 3`. Dưới, một dãy số nhỏ xám `0.12  0.87  -0.34  0.56 …` mọc dần, rồi thu lại thành một chấm tròn trắng giữa mặt phẳng.
- **Chuyển động:** Dãy số hiện từng số một, rồi cả dãy thu nhỏ về một điểm (grow ngược). Chấm tròn pop nhẹ khi đáp xuống.
- **Chữ trên màn hình:** `một câu = một điểm`
- **Âm thanh:** tick từng số, pop khi thành điểm.

### Cảnh 3 — Nghĩa gần nhau, điểm gần nhau (câu 3)
- **Khung hình:** Mặt phẳng 2D có trục xám. Hai chấm gần nhau ở giữa: một mint, một periwinkle. Nhãn hai câu bên cạnh từng chấm. Đoạn thẳng ngắn nối hai chấm, chữ `gần` ở giữa.
- **Chuyển động:** Hai chấm fade-in lần lượt, đoạn nối vẽ ra sau, chữ `gần` blur-in cuối.
- **Chữ trên màn hình:** `doanh thu quý 3` (mint) — `lợi nhuận quý 3` (periwinkle)
- **Âm thanh:** pop, pop, tick.

### Cảnh 4 — Không liên quan, điểm xa nhau (câu 4)
- **Khung hình:** Cùng mặt phẳng, một chấm mint ở góc trái dưới (`doanh thu quý 3`), một chấm trắng ở góc phải trên (`cách nấu phở`). Đường nét đứt dài nối hai chấm, chữ `xa` ở giữa.
- **Chuyển động:** Hai chấm fade-in, đường nét đứt vẽ chậm từ chấm này sang chấm kia — nhấn mạnh độ dài.
- **Chữ trên màn hình:** `cách nấu phở`
- **Âm thanh:** whoosh dài theo đường vẽ.

### Cảnh 5 — Khoảng cách chính là độ giống nhau (câu 5)
- **Khung hình:** Hai chấm, đoạn thẳng nối có vạch thước chia đều. Dưới: công thức serif trắng `gần = giống nhau`.
- **Chuyển động:** Vạch thước hiện dần từ trái sang phải, công thức blur-in khi thước chạy xong.
- **Chữ trên màn hình:** `khoảng cách = độ giống nhau`
- **Âm thanh:** tick đều theo từng vạch thước.

### Cảnh 6 — Mảnh tài liệu thành điểm, bằng Gemini (câu 6)
- **Khung hình:** Một đoạn thẳng (tài liệu) chia 4 mảnh như video 01 cảnh 4. Một mảnh sáng periwinkle, mũi tên cong từ mảnh đó xuống một chấm trên mặt phẳng nhỏ bên dưới. Góc phải trên, hộp nhỏ ghi `gemini-embedding-001`.
- **Chuyển động:** Mảnh sáng lên, mũi tên vẽ cong xuống, chấm pop lên trên mặt phẳng.
- **Chữ trên màn hình:** `mỗi mảnh 500 ký tự = 1 điểm`
- **Âm thanh:** whoosh + pop.

### Cảnh 7 — Câu hỏi tìm 3 điểm gần nhất (câu 7)
- **Khung hình:** Như video 01 cảnh 6: chấm hỏi mint ở trên, 3 chấm periwinkle sáng bên dưới nối bằng 3 đoạn thẳng, các chấm khác mờ xám. Hộp góc phải: `top 3`.
- **Chuyển động:** 3 đoạn thẳng vẽ lần lượt, 3 chấm sáng dần lên, còn lại mờ đi (spotlight).
- **Chữ trên màn hình:** `tìm 3 điểm gần nhất`
- **Âm thanh:** ting ting ting, 3 lần.

### Cảnh 8 — Không có embedding thì mù (câu 8)
- **Khung hình:** Mặt phẳng đầy chấm xám mờ, giữa là dấu `?` serif trắng lớn. Dưới: `không biết mảnh nào liên quan`.
- **Chuyển động:** Dấu `?` blur-in chậm, giữ lâu. Các chấm xám mờ dần thêm — nhấn mạnh sự mù.
- **Chữ trên màn hình:** `không có embedding = không biết đường`
- **Âm thanh:** im lặng 0,5 giây rồi một nốt trầm (thud nhẹ).

### Cảnh 9 — Kết: 1 công thức (câu 9)
- **Khung hình:** Giữa màn hình, công thức serif trắng lớn `Embedding = chữ → số`. Hộp góc phải trên: `giống nhau → gần nhau`.
- **Chuyển động:** Công thức blur-in nguyên khối, giữ lâu. Không thêm gì nữa.
- **Chữ trên màn hình:** `Embedding = chữ → số`
- **Âm thanh:** chime kết.

---

## Kiểm tra độ chính xác (số thật trong project)
- Chunk 500 ký tự, overlap 50 — đúng ingest.py
- Embedding bằng Gemini `gemini-embedding-001` — đúng project
- Lưu trong Chroma, retrieve top-3 — đúng project
- Không nêu số chiều vector cụ thể (không chắc project dùng 3072 hay 768) — chỉ nói "một dãy số"
- Đừng nói "AI tự tìm trên mạng" — chỉ tìm trong tài liệu của mình

## Checklist trước khi đăng
- [ ] Đọc thử kịch bản thành tiếng, bấm giờ: phải trong 55–65 giây (giọng A, speed 90)
- [ ] Đủ 9 cảnh, mỗi cảnh 1 ý, chuyển cảnh crossfade không cắt cứng
- [ ] Xem video không bật tiếng vẫn hiểu được 80% nội dung
- [ ] Xem video không nhìn hình, chỉ nghe tiếng, vẫn hiểu được câu chuyện
- [ ] Không có chữ "Bài gốc", không có dòng credit AI, không có hình AI-generated
- [ ] Tăng tốc 1.25x trước khi đăng, caption ghi đúng số giây mới
