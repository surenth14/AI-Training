from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

print("🤖 AI CLI Bot is ready! Type 'exit' to quit.\n")

system_prompt = "You are a friendly AI tutor for college students. Explain concepts simply."

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Bye! Keep building cool AI stuff 🚀")
        break

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
    )

    bot_reply = response.choices[0].message.content
    print("\nBot:", bot_reply, "\n")
