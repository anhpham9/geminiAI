from google import genai
import os

def main():
    if "GEMINI_API_KEY" not in os.environ:
        raise RuntimeError("Chưa set biến môi trường GEMINI_API_KEY")

    client = genai.Client(
        api_key=os.environ["GEMINI_API_KEY"]
    )

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents="GenAI là gì?"
    )

    print(response.text)

if __name__ == "__main__":
    main()
