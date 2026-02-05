from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

history = []

def chat(user_input: str) -> str:
    # user message
    history.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)]
        )
    )

    # call model
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=history
    )

    # assistant message
    history.append(
        types.Content(
            role="model",
            parts=[types.Part.from_text(text=response.text)]
        )
    )

    return response.text


# vòng lặp chat
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bye 👋")
        break

    reply = chat(user_input)
    print("AI:", reply)
