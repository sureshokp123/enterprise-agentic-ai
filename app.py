import asyncio

from services.agent_service import process_question


async def main():

    while True:

        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            break

        answer = await process_question(question)

        print(f"\nAgent: {answer}")


if __name__ == "__main__":
    asyncio.run(main())