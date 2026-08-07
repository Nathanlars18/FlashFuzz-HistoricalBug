import requests

url="https://ollama1.aaaab3n.moe/v1/chat/completions"

data={
    "model":"gpt-oss:120b",
    "messages":[
        {
            "role":"user",
            "content":"Say hello"
        }
    ]
}


r=requests.post(
    url,
    json=data,
    timeout=60
)

print(r.status_code)
print(r.text[:500])
