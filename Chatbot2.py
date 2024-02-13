import os
from openai import OpenAI, AsyncOpenAI

# Choose between synchronous or asynchronous client based on your needs
# Use synchronous client for regular synchronous code
# Use asynchronous client if you want to use async/await syntax
USE_ASYNC_CLIENT = False

if USE_ASYNC_CLIENT:
    client = AsyncOpenAI(api_key=os.environ.get("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"))
else:
    client = OpenAI(api_key=os.environ.get("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"))


async def chat_with_gpt(prompt):
    # Use async client for asynchronous operations
    if USE_ASYNC_CLIENT:
        completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
    else:
        # Use synchronous client for regular synchronous code
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
    return completion.choices[0].message.content.strip()


if __name__ == "__main__":
    # For async client, define main function with async keyword
    if USE_ASYNC_CLIENT:
        import asyncio

        async def main():
            while True:
                user_input = input("You: ")
                if user_input.lower() in ["quit", "exit", "bye"]:
                    print("Goodbye!")
                    break

                response = await chat_with_gpt(user_input)
                print("Chatbot:", response)

        asyncio.run(main())
    else:
        # For synchronous client, regular while loop works
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit", "bye"]:
                print("Goodbye!")
                break

            response = chat_with_gpt(user_input)
            print("Chatbot:", response)
