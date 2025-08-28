import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    provider="fal-ai",
    api_key=os.getenv("HF_TOKEN"),
)

output = client.automatic_speech_recognition("chunkk_0.wav", model="openai/whisper-large-v3")
print(output["text"])


# from pydub import AudioSegment

# audio = AudioSegment.from_file("audio.wav")
# chunk_length_ms = 60 * 1000  # 1 dakika
# for i, chunk in enumerate(audio[::chunk_length_ms]):
#     chunk.export(f"chunkk_{i}.wav", format="wav")