# bot.py
import ollama

def chatbot(prompt):
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

if __name__ == "__main__":
    print("🤖 Local AI Bot is ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        reply = chatbot(user_input)
        print(f"John-Bot: {reply}")
