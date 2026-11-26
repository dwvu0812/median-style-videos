# Video 01 — RAG hoạt động như thế nào?
## Kịch bản + Storyboard — phong cách Median / Clockwork

- **Chủ đề:** RAG (Retrieval-Augmented Generation) — đúng project RAG chatbot của t, vừa học vừa làm portfolio
- **Độ dài mục tiêu:** 60–75 giây (kịch bản dưới đây ~70 giây đọc ở tốc độ bình thường)
- **Ngôn ngữ:** Tiếng Việt, giọng kể chuyện, không giọng AI
- **Phong cách hình:** Nền tối, chữ trắng, highlight vàng cho từ khóa, nhân vật que (stick figure) kiểu Alan Becker — đơn giản, chuyển động là chính, không cần vẽ đẹp
- **Nguyên tắc Median áp dụng ở đây:** Từng khung hình do người thiết kế, phải hiểu 100% kịch bản. AI (Claude Code) chỉ viết code chuyển động từ bản vẽ. Không giao hết cho AI.

---

## Ý tưởng cốt lõi — 1 câu duy nhất

> AI trả lời sai không phải vì nó dốt, mà vì nó đang thi mà không được mang tài liệu. RAG là cho nó mang tài liệu vào phòng thi.

Mọi cảnh trong video chỉ phục vụ 1 ý này. Không lan man sang training, fine-tuning, hay so sánh model.

---

## Kịch bản — lời thoại từng câu

| # | Thời gian | Lời thoại (đọc đúng từng chữ) | Số từ |
|---|-----------|-------------------------------|-------|
| 1 | 0:00–0:05 | AI trả lời sai, không phải vì nó dốt. | 9 |
| 2 | 0:05–0:11 | Mà vì nó đang thi, mà không được mang tài liệu. | 12 |
| 3 | 0:11–0:20 | Hỏi nó doanh thu quý 3 của công ty mình là bao nhiêu, nó chỉ còn cách đoán. | 19 |
| 4 | 0:20–0:28 | RAG làm một việc rất đơn giản: cho nó mang tài liệu vào phòng thi. | 15 |
| 5 | 0:28–0:38 | Đầu tiên, cắt tài liệu thành từng mảnh nhỏ, mỗi mảnh khoảng 500 ký tự. | 15 |
| 6 | 0:38–0:48 | Rồi biến mỗi mảnh thành một điểm trên bản đồ, mảnh nào giống nhau thì đứng gần nhau. | 19 |
| 7 | 0:48–0:57 | Khi có câu hỏi, nó cũng biến câu hỏi thành một điểm, rồi tìm 3 mảnh gần nhất. | 19 |
| 8 | 0:57–1:06 | Cuối cùng, đưa 3 mảnh đó cho AI, nó đọc rồi mới trả lời, kèm theo nguồn trích dẫn. | 19 |
| 9 | 1:06–1:12 | Không có tài liệu thì nó nói không biết, chứ không bịa nữa. | 14 |
| 10 | 1:12–1:18 | Đó là RAG: tìm trước, đọc rồi, mới trả lời. | 10 |

**Tổng: ~151 từ, ~72–78 giây.** Nếu đọc nhanh hơn 5 giây thì cắt câu 9 xuống còn: “Không có tài liệu, nó nói không biết.”

---

## Storyboard — từng cảnh, từng chuyển động

### Cảnh 1 — Hook: thi không tài liệu (0:00–0:11, câu 1–2)

- **Khung hình (vẽ trên Excalidraw):** Một nhân vật que ngồi ở bàn thi, trước mặt là tờ đề trắng. Trên đầu nó là một bộ não / đám mây suy nghĩ trống rỗng, có dấu “?”. Bên cạnh bàn có một cái cặp tài liệu bị gạch chéo đỏ, đặt ngoài phòng.
- **Chuyển động:** Camera zoom nhẹ vào nhân vật que. Dấu “?” trong đầu nó nhấp nháy 2 lần. Cái cặp tài liệu rung nhẹ rồi bị dấu X đỏ đóng xuống — đúng nhịp chữ “không được mang tài liệu”.
- **Chữ trên màn hình:** `AI trả lời sai` (trắng) → `không được mang tài liệu` (vàng, hiện sau)
- **Âm thanh gắn theo chuyển động:** Tiếng “cạch” khi dấu X đỏ đóng xuống. Không nhạc nền to, chỉ một nốt trầm.

### Cảnh 2 — Câu hỏi làm khó nó (0:11–0:20, câu 3)

- **Khung hình:** Tờ đề phóng to, hiện câu hỏi: “Doanh thu quý 3 của công ty mình là bao nhiêu?” Nhân vật que toát mồ hôi, trên đầu hiện 3 con số nhảy loạn: 10 tỷ, 50 tỷ, 100 tỷ.
- **Chuyển động:** Các con số nhảy loạn rồi dừng ở một số ngẫu nhiên, bị gạch chéo đỏ, hiện chữ “ĐOÁN”.
- **Chữ trên màn hình:** Câu hỏi giữ nguyên. Chữ `ĐOÁN` màu đỏ hiện ở cuối cảnh.
- **Âm thanh:** Tiếng “tíc tíc” khi số nhảy, tiếng “bíp” sai khi bị gạch.

### Cảnh 3 — RAG xuất hiện (0:20–0:28, câu 4)

- **Khung hình:** Cái cặp tài liệu lúc nãy được mở ra, bay vào phòng thi, đặt lên bàn nhân vật que. Nhân vật que ngẩng lên, dấu “?” biến thành bóng đèn sáng.
- **Chuyển động:** Cặp tài liệu bay theo đường cong từ ngoài vào, hạ xuống bàn đúng nhịp chữ “mang tài liệu vào phòng thi”. Bóng đèn sáng lên với hiệu ứng tỏa sáng 0,3 giây.
- **Chữ trên màn hình:** `RAG` to, ở giữa màn hình, dưới có dòng nhỏ: `Retrieval-Augmented Generation`
- **Âm thanh:** Tiếng “vút” khi cặp bay vào, tiếng “ting” khi bóng đèn sáng.

### Cảnh 4 — Cắt tài liệu thành mảnh nhỏ (0:28–0:38, câu 5)

- **Khung hình:** Một tài liệu dài (hình chữ nhật dọc, có nhiều dòng chữ) nằm giữa màn hình. Một đường cắt chạy ngang, tài liệu tách thành 4–5 mảnh nhỏ xếp thành hàng.
- **Chuyển động:** Đường cắt chạy từ trái sang phải, mỗi lần cắt xong một mảnh tách ra với khoảng cách đều nhau. Mỗi mảnh hiện số thứ tự 1, 2, 3, 4.
- **Chữ trên màn hình:** `500 ký tự / mảnh` — đây là con số thật trong project của t (ingest.py: chunk 500 ký tự, overlap 50).
- **Âm thanh:** Tiếng “xoẹt” mỗi lần cắt, 4 lần, đều nhịp.

### Cảnh 5 — Biến mảnh thành điểm trên bản đồ (0:38–0:48, câu 6)

- **Khung hình:** Các mảnh nhỏ bay lên, biến thành các chấm tròn trên một mặt phẳng 2D. Các chấm cùng chủ đề tụ lại thành cụm: cụm “doanh thu”, cụm “quý 3”, cụm “báo cáo”.
- **Chuyển động:** Mảnh → chấm: thu nhỏ dần trong 0,4 giây. Các chấm di chuyển về cụm của mình, có đường mờ nối lại rồi biến mất.
- **Chữ trên màn hình:** `Embedding` (vàng) + dòng nhỏ: `mỗi mảnh = 1 điểm, giống nhau thì đứng gần nhau`
- **Âm thanh:** Tiếng “pop” nhẹ mỗi khi một chấm đáp xuống cụm.

### Cảnh 6 — Câu hỏi đi tìm 3 mảnh gần nhất (0:48–0:57, câu 7)

- **Khung hình:** Câu hỏi lúc đầu (câu doanh thu quý 3) biến thành một chấm hỏi màu vàng, rơi xuống bản đồ. Từ chấm hỏi tỏa ra 3 đường nối tới 3 chấm gần nhất, 3 chấm đó sáng lên, các chấm khác mờ đi.
- **Chuyển động:** Chấm hỏi rơi xuống, nảy nhẹ 1 lần. 3 đường nối vẽ ra lần lượt, mỗi đường 0,3 giây. 3 chấm được chọn phóng to nhẹ.
- **Chữ trên màn hình:** `Top 3` to ở góc, 3 chấm được chọn đánh số ①②③
- **Âm thanh:** Tiếng “ting ting ting” 3 lần, mỗi lần một chấm sáng lên.

### Cảnh 7 — Đọc rồi mới trả lời, có trích dẫn (0:57–1:06, câu 8)

- **Khung hình:** 3 mảnh được chọn bay về phía nhân vật que, xếp thành chồng trước mặt nó. Nhân vật que đọc, gật đầu, rồi nói ra câu trả lời trong bong bóng thoại. Dưới câu trả lời hiện 3 nguồn: `[1] [2] [3]`.
- **Chuyển động:** 3 mảnh bay về theo đường cong, xếp chồng. Bong bóng thoại hiện ra từng chữ (typewriter, khớp giọng đọc). Dấu tick xanh hiện sau câu trả lời.
- **Chữ trên màn hình:** Câu trả lời mẫu: `Doanh thu quý 3 là 42 tỷ. [1][2][3]`
- **Âm thanh:** Tiếng lật giấy khi 3 mảnh bay về, tiếng “tick” khi dấu xanh hiện.

### Cảnh 8 — Không có tài liệu thì nói không biết (1:06–1:12, câu 9)

- **Khung hình:** Cùng khung hình cảnh 7, nhưng 3 mảnh biến mất, chỉ còn bàn trống. Nhân vật que nhún vai, bong bóng thoại hiện: “Mình không tìm thấy trong tài liệu.”
- **Chuyển động:** 3 mảnh mờ dần và biến mất. Nhân vật que nhún vai 1 lần, chậm.
- **Chữ trên màn hình:** `Không bịa nữa.` (xanh lá)
- **Âm thanh:** Im lặng 0,5 giây rồi một nốt nhạc nhẹ — nhấn mạnh sự khác biệt với cảnh 2.

### Cảnh 9 — Kết: 3 bước, 1 câu (1:12–1:18, câu 10)

- **Khung hình:** Màn hình tối lại, chỉ còn 3 ô xếp ngang: `1. TÌM` → `2. ĐỌC` → `3. TRẢ LỜI`. Dưới là chữ `RAG`.
- **Chuyển động:** 3 ô hiện lần lượt, mỗi ô 0,4 giây, có mũi tên nối. Chữ RAG hiện cuối cùng, phóng to nhẹ.
- **Chữ trên màn hình:** `Tìm trước — Đọc rồi — Mới trả lời`
- **Âm thanh:** 3 tiếng “tock” đều nhau, rồi một hợp âm kết.

---

## Ghi chú sản xuất — làm theo đúng quy trình Median

1. **Vẽ trước, code sau:** Vẽ đủ 9 khung hình trên Excalidraw, từng khung là 1 ảnh tĩnh. Không được nhảy sang code khi chưa chốt khung hình.
2. **AI viết code theo từng câu:** Đưa từng khung hình + 1 câu thoại vào Claude Code, nhờ nó viết code chuyển động cho đúng cảnh đó, trên thư viện animation của t (Remotion / Canvas / mini-Clockwork tự viết). Xong 1 cảnh mới sang cảnh sau.
3. **Chỉnh tay:** Xem lại từng cảnh, chỉnh easing, thời gian, vị trí cho mượt. Hiệu ứng nào chưa có thì code thêm vào thư viện, để video sau dùng lại.
4. **Âm thanh cuối cùng:** Thu / tạo giọng đọc trước (ElevenLabs, tiếng Việt), rồi gắn SFX vào đúng thời điểm chuyển động — không chèn nhạc nền chung chung rồi hy vọng nó khớp.
5. **Kiểm tra độ chính xác:** Các con số trong video phải đúng project thật của t:
   - Chunk 500 ký tự, overlap 50
   - Embedding bằng Gemini `gemini-embedding-001`
   - Lưu trong Chroma, retrieve top-3
   - Trả lời kèm citations thật, không có tài liệu thì `retrieved: false`, nói không biết
   - Đừng nói “AI tự tìm trên mạng” — RAG ở đây chỉ tìm trong tài liệu của mình.

## Checklist trước khi đăng

- [ ] Đọc thử kịch bản thành tiếng, bấm giờ: phải trong 60–80 giây
- [ ] Đủ 9 khung hình Excalidraw, mỗi khung ghi rõ chuyển động + SFX
- [ ] Xem video không bật tiếng vẫn hiểu được 80% nội dung (chữ trên màn hình đủ rõ)
- [ ] Xem video không nhìn hình, chỉ nghe tiếng, vẫn hiểu được câu chuyện
- [ ] Không có chữ “Bài gốc”, không có dòng credit AI, không có hình AI-generated
- [ ] Tiêu đề gợi ý: `AI trả lời sai không phải vì nó dốt` / `RAG là gì trong 70 giây`
- [ ] Mô tả video: link repo RAG của t (https://github.com/dwvu0812/vietnamese-rag-chatbot), 1 câu về project

## Video tiếp theo (đừng làm cùng lúc)

- Video 02: `Embedding là gì?` — nối tiếp cảnh 5, đào sâu 1 ý duy nhất
- Video 03: `Vì sao chatbot không có RAG hay bịa?` — nối tiếp cảnh 2 + 8
- Làm xong video 01, xem retention ở 5 giây đầu và 30 giây đầu rồi mới quyết định video 02 làm gì tiếp.
