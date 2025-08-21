This is my first attempt at getting into AI by creating this simple chatbot using the ollama library. In order to use this, you'll need to install the ollama models (https://ollama.com). If you want to use Open AI, then create your .env file and add the OPENAI_API_KEY inside. Then, you'll make your bot.py something like this:

# bot.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-4o, gpt-4o-mini
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("🤖 AI Bot is ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        reply = chatbot(user_input)
        print(f"Bot: {reply}")

