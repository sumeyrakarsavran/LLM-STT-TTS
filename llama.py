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

# Modelden çıktı al
completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "iphone 15 turkiyede kac tl?"
        }
    ],
)

print(completion.choices[0].message.content)

