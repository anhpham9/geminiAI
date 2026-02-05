from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# ===== SYSTEM PROMPT (dưới dạng instruction) =====
SYSTEM_PROMPT = (
    "Bạn là trợ giảng AI về Trí tuệ nhân tạo. "
    "Giải thích ngắn gọn, dễ hiểu, bằng tiếng Việt. "
    "Ưu tiên ví dụ thực tế cho người mới học."
)

history = []

def chat(user_input: str) -> str:
    # Nếu là lượt đầu → gộp system prompt
    if not history:
        full_input = SYSTEM_PROMPT + "\n\n" + user_input
    else:
        full_input = user_input

    history.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=full_input)]
        )
    )

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=history
    )

    history.append(
        types.Content(
            role="model",
            parts=[types.Part.from_text(text=response.text)]
        )
    )

    return response.text


# ===== CHAT LOOP =====
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bye 👋")
        break

    reply = chat(user_input)
    print("AI:", reply)
