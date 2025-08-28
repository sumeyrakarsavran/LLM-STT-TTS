import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# .env yükle
load_dotenv()
api_key = os.getenv("HF_TOKEN")

if api_key is None:
    raise ValueError("HF_TOKEN bulunamadı!")

# API client
client = InferenceClient(api_key=api_key)

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "tell me a joke about programming"
        }
    ],
)

print(completion.choices[0].message.content)