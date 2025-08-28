# LLM-STT-TTS Project

This project combines Language Models (LLM), Speech-to-Text (STT), and Text-to-Speech (TTS) capabilities using various AI models and APIs. It provides a suite of tools for converting between text and speech, with additional language model integration.

## Features

- 🎙️ **Speech-to-Text (STT)**: Convert audio files to text using OpenAI's Whisper model
- 🔊 **Text-to-Speech (TTS)**: Generate natural-sounding speech from text using Hugging Face models
- 🤖 **LLM Integration**: Support for various language models
- 🔄 **Audio Processing**: Tools for handling and processing audio files
- 🌐 **Multiple AI Providers**: Integration with providers like Hugging Face and Replicate

## Prerequisites

- Python 3.x
- Hugging Face API Token
- OpenAI API Token (if using OpenAI features)
- Replicate API Token (if using Replicate features)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd LLM-STT-TTS
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python createvenv.py
# or manually:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root and add your API keys:
```env
HF_TOKEN=your_huggingface_token
OPENAI_API_KEY=your_openai_api_key
REPLICATE_API_TOKEN=your_replicate_token
```

## Usage

### Text-to-Speech (TTS)
Use `tts.py` to convert text to speech:
```python
python tts.py
```
This will generate an audio file (`output.mp3`) using the Kokoro-82M model.

### Speech-to-Text (STT)
Use `stt.py` to transcribe audio to text:
```python
python stt.py
```
The script uses OpenAI's Whisper model to transcribe audio files.

### Audio Processing
The project includes functionality to:
- Split audio files into chunks
- Process large audio files
- Convert between different audio formats

## Project Structure

- `app.py`: Main application file
- `stt.py`: Speech-to-Text functionality
- `tts.py`: Text-to-Speech functionality
- `llama.py`: LLaMA model integration
- `replicate.py`: Replicate API integration
- `requirements.txt`: Project dependencies
- `createvenv.py`: Virtual environment setup script

## Dependencies

- python-dotenv: Environment variable management
- streamlit: Web interface (if applicable)
- huggingface_hub: Hugging Face model access
- TTS: Text-to-Speech library
- pydub: Audio file processing
- replicate: Replicate API client
- openai: OpenAI API integration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your chosen license here]

## Acknowledgments

- Hugging Face for providing AI models and inference API
- OpenAI for the Whisper model
- Other contributors and open-source projects used
