import os
import requests


url = "https://api.deepseek.com/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ.get('DEEPSEEK_API_KEY')}"
}


data = {
    "model": "deepseek-v4-pro",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello, please reply with OK."
        }
    ],
    "temperature": 0.2
}


response = requests.post(
    url,
    headers=headers,
    json=data
)


print(response.status_code)

print(response.text)
