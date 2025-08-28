import replicate
from dotenv import load_dotenv

load_dotenv()

prompt = "Mevsimler nas1l oluşur?"
system_prompt = "Sen yardimsever bir asistansin."

#Llama 2 70 B Chat

AI_Response = replicate.run(
    "meta/llama-2-70b-chat",
    input = {
        "temperature":0.5,
        "max_new_tokens": 256,
        "system_prompt": system_prompt,
        "prompt": prompt,
        "debug": False
    }
)

AI_Response = "".join(AI_Response)
print(AI_Response)
