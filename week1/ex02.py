from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

contents = [
    types.Content(
        role="user",
        parts=[
            types.Part.from_text(text="GenAI là gì?")
        ]
    ),
    types.Content(
        role="model",
        parts=[
            types.Part.from_text(text="GenAI là trí tuệ nhân tạo có khả năng tạo ra nội dung mới.")
        ]
    ),
    types.Content(
        role="user",
        parts=[
            types.Part.from_text(text="Giải thích kỹ hơn, kèm ví dụ")
        ]
    )
]

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=contents
)

print(response.text)
