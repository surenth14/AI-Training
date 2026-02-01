from openai import OpenAI
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

if not os.getenv("OPENROUTER_API_KEY"):
    print(" OPENROUTER_API_KEY not found. Check your .env file.")
    exit(1)

# Load prompts
with open("prompts/system.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

with open("prompts/user.txt", "r", encoding="utf-8") as f:
    user_template = f.read()

# Hardcoded model & parameters (trainer-controlled)
MODEL_NAME = "mistralai/mistral-7b-instruct"
TEMPERATURE = 0.3       # Lower = more factual
MAX_TOKENS = 300       # Response length


# Init OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

print(" AI CLI Chatbot ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Bot: Bye! Keep building cool AI apps 🚀")
        break

    final_user_prompt = user_template.format(question=user_input)

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": final_user_prompt}
            ],
        )

        bot_reply = response.choices[0].message.content
        print("\nBot:", bot_reply, "\n")

    except Exception as e:
        print(" Error communicating with AI:", e)
