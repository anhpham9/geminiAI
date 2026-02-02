# lộ trình học GenAI LLM bằng Gemini

## 🧭 Tổng quan lộ trình (8–10 tuần)

Mục tiêu: **biết dùng Gemini API → làm chatbot / app GenAI → nâng cao với RAG & Agent**

## 0️⃣ Chuẩn bị nền tảng (tuần 0 – rất nhanh)

Cần biết:
- Python cơ bản (function, list, dict)
- HTTP / API là gì
- JSON

## 1️⃣ Hiểu Gemini & GenAI LLM (tuần 1)

### 📘 Kiến thức

- Gemini là gì? (Google LLM)
- Gemini vs GPT vs Claude
- Token, context window
- Prompt vs completion vs chat

### 🧠 Thực hành

- Dùng Google AI Studio
- Test prompt:
  - hỏi đáp
  - sinh code
  - tóm tắt
  - phân tích dữ liệu

### 🎯 Output: biết viết prompt tốt

## 2️⃣ Lập trình Gemini API cơ bản (tuần 2)

### 🔧 Setup

```
pip install google-generativeai
```

### 🔑 Code mẫu

```
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(
    "Giải thích GenAI LLM cho người mới"
)

print(response.text)
```

### 🎯 Output: gọi được Gemini bằng code

## 3️⃣ Prompt Engineering cho Gemini (tuần 3) 🔥

### 🧩 Kỹ thuật

- System instruction
- Few-shot prompting
- Chain-of-thought (ẩn)
- Output format (JSON, bullet, table)

### 📌 Ví dụ

```
prompt = """
Bạn là chuyên gia tài chính.
Trả lời bằng tiếng Việt.
Output dạng JSON:
{
  "summary": "",
  "risks": []
}
Câu hỏi: Lợi ích GenAI trong ngân hàng?
"""
```

### 🎯 Output: LLM trả về đúng format

## 4️⃣ Làm Chatbot GenAI (tuần 4)

### 🧠 Nội dung

- Lưu context hội thoại
- Giới hạn token
- Safety setting Gemini

### 🧩 Mini project

- Chatbot tư vấn sản phẩm
- Chatbot học tập
- Chatbot HR nội bộ

### 🎯 Output: chatbot chạy thật

## 5️⃣ Gemini Multimodal (tuần 5) 🖼️🎥

### 📘 Học gì?

- Text + Image
- PDF, video, bảng biểu
- Phân tích ảnh / tài liệu

### 🧩 Ví dụ

```
model.generate_content([
  "Giải thích biểu đồ này",
  image_data
])
```

### 🎯 Output: AI đọc được tài liệu & hình ảnh

## 6️⃣ RAG với Gemini (tuần 6–7) 📚

### 🔗 Kiến trúc

```
User question
→ Embedding
→ Vector DB
→ Gemini
```

### 🛠 Công cụ

- Embedding: Gemini / SentenceTransformer
- Vector DB: FAISS / Chroma
- Framework: LlamaIndex

### 🧩 Mini project

- Hỏi đáp tài liệu công ty
- Chat PDF / hợp đồng

### 🎯 Output: GenAI đọc dữ liệu riêng

## 7️⃣ Agent với Gemini (tuần 8) 🤖

### 🧠 Học gì?

- Tool calling
- Planning
- Multi-step reasoning

### 🧩 Ví dụ

- AI tự gọi API thời tiết
- AI phân tích dữ liệu + báo cáo

Framework:
- LangChain
- CrewAI

### 🎯 Output: AI biết “làm việc”

## 8️⃣ Project cuối (tuần 9–10) 🏆

### Chọn 1:

🔹 Chatbot CSKH doanh nghiệp

🔹 Trợ lý phân tích tài chính

🔹 AI đọc hợp đồng

🔹 AI hỗ trợ dev

### Stack đề xuất

- Backend: Python / FastAPI
- Frontend: Streamlit / Next.js
- Model: Gemini 1.5 Flash / Pro

## 📌 So sánh nhanh model Gemini

|Model|	Dùng khi|
|--|--|
|Gemini 1.5 Flash|	nhanh, rẻ|
|Gemini 1.5 Pro|	reasoning mạnh|
|Gemini Nano|	on-device|

## 🎯 Sau lộ trình này, bạn làm được:

✅ Lập trình GenAI bằng Gemini

✅ Xây chatbot & app thực tế

✅ Làm RAG & Agent

✅ Apply vào business / startup
