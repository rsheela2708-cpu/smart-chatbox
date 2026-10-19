import os
from google import genai
from google.genai.errors import APIError


def main():
    print("=" * 40)
    print("       GEMINI AI CHATBOT")
    print("=" * 40)

    # Read the key from the terminal environment
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("ERROR: GEMINI_API_KEY is not set.")
        print('Run: $env:GEMINI_API_KEY = "YOUR_NEW_KEY"')
        return

    try:
        client = genai.Client(api_key=api_key)

        chat = client.chats.create(
            model="gemini-3.5-flash-lite"
        )

        print("\nGemini chatbot is ready!")
        print("Type 'exit' or 'quit' to stop.\n")

        while True:
            try:
                user_input = input("You: ").strip()

                if user_input.lower() in ("exit", "quit"):
                    print("Gemini: Goodbye!")
                    break

                if not user_input:
                    continue

                response = chat.send_message(user_input)
                print(f"\nGemini: {response.text}\n")

            except APIError as error:
                print(f"\nGemini API error: {error}\n")

            except (KeyboardInterrupt, EOFError):
                print("\nChatbot stopped.")
                break

    except Exception as error:
        print(f"\nCould not start chatbot: {error}")


if __name__ == "__main__":
    main()









