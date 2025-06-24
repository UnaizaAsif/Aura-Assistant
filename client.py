import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
print("Loaded OpenRouter API Key:", api_key)

API_URL = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def ask_ai(prompt):
    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are Aura, a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        print("AI Response:", reply)  # Debugging output
        return reply
    except requests.exceptions.RequestException:
        return "AI service is currently unavailable."
    except Exception as e:
        return "Sorry, I couldn't understand that."
