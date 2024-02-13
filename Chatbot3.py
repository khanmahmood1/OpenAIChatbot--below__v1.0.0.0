import os
import asyncio
from openai import AsyncOpenAI

# Set your API key here or as an environment variable
API_KEY = "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"

async def chat_with_gpt(prompt):
    async with AsyncOpenAI(api_key=API_KEY) as client:
        completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
    return completion.choices[0].message.content.strip()


async def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response = await chat_with_gpt(user_input)
        print("Chatbot:", response)

asyncio.run(main())
