import os
import requests

# OPENROUTER_API_KEY = "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"
# OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_response(prompt: str) -> str:
    # headers = {
    #     "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    #     "Content-Type": "application/json"
    # }
    # json_data = {
    #     "model": "meta-llama/llama-3.1-8b-instruct:free",  # use your preferred model available in OpenRouter
    #     "messages": [
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": prompt}
    #     ],
    #     "temperature": 0.7,
    #     "max_tokens": 200
    # }

    # response = requests.post(OPENROUTER_URL, headers=headers, json=json_data)
    # response.raise_for_status()
    # data = response.json()

    return prompt
