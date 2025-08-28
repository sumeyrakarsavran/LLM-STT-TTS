import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    provider="fal-ai",
    api_key=os.getenv("HF_TOKEN"),
)

# audio is returned as bytes
audio = client.text_to_speech(
    "The answer to the universe is 42",
    model="hexgrad/Kokoro-82M",
)

# Ses dosyasını kaydet
output_path = "output.mp3"
with open(output_path, "wb") as f:
    f.write(audio)

print(f"Ses kaydedildi: {output_path}")