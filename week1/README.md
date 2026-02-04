# 1️⃣ Gemini là gì? (Google LLM)

**Gemini** là **Large Language Model (LLM)** do **Google** phát triển, kế nhiệm PaLM.

## 🧠 Đặc điểm chính

- Là GenAI đa phương thức (multimodal):
  - Text
  - Image
  - Audio
  - Video
  - PDF / tài liệu

- Context window rất lớn (hàng trăm nghìn đến triệu token)
- Tích hợp mạnh với hệ sinh thái Google (Search, Docs, Drive…)

## 📌 Dùng Gemini khi:

- Phân tích tài liệu dài (PDF, report)
- Chatbot doanh nghiệp
- Ứng dụng cần đa phương thức
- Muốn chi phí tối ưu (Flash)

## 👉 Hiểu ngắn gọn:

```
Gemini = LLM mạnh về đa phương thức + context lớn
```

# 2️⃣ Gemini vs GPT vs Claude

## 🧾 So sánh tổng quan

|Tiêu chí	|Gemini (Google)	|GPT (OpenAI)	|Claude (Anthropic)|
|--|--|--|--|
|Chủ sở hữu	|Google	|OpenAI	|Anthropic|
|Multimodal	|⭐⭐⭐⭐	|⭐⭐⭐⭐	|⭐⭐|
|Context window	|⭐⭐⭐⭐⭐	|⭐⭐⭐⭐	|⭐⭐⭐⭐⭐|
|Reasoning	|⭐⭐⭐⭐	|⭐⭐⭐⭐⭐	|⭐⭐⭐⭐|
|An toàn	|⭐⭐⭐⭐	|⭐⭐⭐⭐	|⭐⭐⭐⭐⭐|
|Giá	|Rẻ (Flash)	|Trung bình	|Khá cao|

## 📌 Khi nào dùng cái nào?

- Gemini → đọc tài liệu dài, multimedia, Google stack
- GPT → code, logic, agent phức tạp
- Claude → văn bản dài, pháp lý, policy

👉 Không có cái nào “tốt nhất”, chỉ có phù hợp nhất

**Chú thích:**

👉 Multimodal nghĩa là AI hiểu & xử lý nhiều loại dữ liệu cùng lúc, không chỉ văn bản (Chữ + ảnh + âm thanh + video). **Multimodal = nhiều “giác quan”**

👉 **Reasoning** = khả năng **suy luận, phân tích logic, giải quyết vấn đề nhiều bước**. Không chỉ trả lời `đúng`, mà trả lời `có lý do`

🧠 Ví dụ đơn giản

**Không reasoning (pattern matching):**
```
2 + 2 = 4
```

**Có reasoning:**
```
Nếu A > B và B > C → A > C
```

# 3️⃣ Token & Context Window

## 🔹 Token là gì?

**Token** là **đơn vị nhỏ mà LLM hiểu**, không phải từ.

Ví dụ:
```
"Tôi yêu GenAI"
→ ["Tôi", "yêu", "Gen", "AI"]
```

👉 1 từ ≈ 1–2 token (tiếng Việt thường nhiều token hơn tiếng Anh)

## 🔹 Context window là gì?

Là **số token tối đa** mà model:

- có thể nhận vào
- ghi nhớ
- tạo ra

Ví dụ:

- Context 128k token → đọc được ~300 trang PDF
- Context 1M token → cả cuốn sách

## 📌 Hệ quả khi lập trình:

- Quá token → lỗi
- Context lớn → RAG mạnh
- Context nhỏ → phải tóm tắt / chunk

# 4️⃣ Prompt vs Completion vs Chat

## 🔹 Prompt là gì?

**Prompt** = đầu vào bạn đưa cho LLM

Ví dụ:
```
"Giải thích Gemini là gì"
```

## 🔹 Completion là gì?

**Completion** = output LLM sinh ra từ prompt

```
Prompt → LLM → Completion
```

👉 Dạng **1 câu hỏi – 1 câu trả lời**

## 🔹 Chat là gì?

**Chat** = prompt có ngữ cảnh hội thoại

Ví dụ:
```
[
  {"role": "system", "content": "Bạn là giảng viên AI"},
  {"role": "user", "content": "Gemini là gì?"},
  {"role": "assistant", "content": "Gemini là..."},
  {"role": "user", "content": "So sánh với GPT"}
]
```

👉 Chat = nhiều prompt + lưu context

# 🧠 So sánh nhanh

|Khái niệm	|Dùng khi|
|--|--|
|Prompt	|gửi yêu cầu|
|Completion	|nhận kết quả|
|Chat	|hội thoại, chatbot|

# 🧩 Tổng kết cực ngắn (để nhớ)

- **Gemini** = LLM đa phương thức của Google
- **GPT / Claude** = mạnh reasoning / an toàn
- **Token** = đơn vị xử lý
- **Context window** = trí nhớ LLM
- **Prompt** = input
- **Completion** = output
- **Chat** = prompt có ngữ cảnh

# Thực hành

VD đơn giản: Hiển thị list models có thể hoạt động

`modelsList.py`

VD tạo prompt với nội dung đơn giản GenAI là gì? và chạy

`ex01.py`

AIzaSyCrjiRgdxT7oKS2jFPpLrzYocbuWOJLE4