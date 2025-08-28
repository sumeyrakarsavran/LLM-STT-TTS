from TTS.api import TTS

#print(TTS.list_models())

tts = TTS("tts_models/tr/common-voice/glow-tts")

tts.tts_to_file(text=("Merhaba, nasılsın? Bugün hava çok güzel. Yağmur yağacak gibi görünüyor. Güneş açacak mı? Bilmiyorum.").lower(),
                file_path="voicee.wav")
