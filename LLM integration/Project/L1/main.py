from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

print("🤖 AI CLI Bot is ready! Type 'exit' to quit.\n")

system_prompt = "You are a friendly AI tutor for college students. Explain concepts simply."

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Bye! Keep building cool AI stuff 🚀")
        break

    response = client.chat.completions.create(
        model="meta-llama/llama-3-8b-instruct",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
    )

    bot_reply = response.choices[0].message.content
    print("\nBot:", bot_reply, "\n")
