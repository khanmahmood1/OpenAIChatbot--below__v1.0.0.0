#import package 
import openai

# from openai import OpenAI

#add open AI key
openai.api_key = "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"
from openai import OpenAI





#creating a function
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]

    )
    
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = ("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]: #to break the chat with bot
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)