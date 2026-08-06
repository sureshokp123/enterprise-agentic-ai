from ollama import chat

response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": "Say Hello",
        }
    ],
)

print(response["message"]["content"])