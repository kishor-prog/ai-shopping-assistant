import asyncio

from ai_assistant.chat_service import ChatService


async def main():
    chat = ChatService()

    while True:
        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            break

        try:
            response = await chat.chat(question)

            print("\nAssistant:\n")
            print(response)

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    asyncio.run(main())