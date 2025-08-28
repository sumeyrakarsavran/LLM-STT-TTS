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

The project provides two different TTS implementations:

#### Hugging Face TTS (tts.py)
Use Hugging Face's TTS service:
```python
python tts.py
```
Features:
- Uses the Kokoro-82M model
- Generates MP3 output
- Requires Hugging Face API token
- Good for general-purpose TTS tasks

#### Coqui TTS (tts2.py)
Use local Coqui TTS model:
```python
python tts2.py
```
Features:
- Uses Turkish Common Voice Glow-TTS model
- Generates WAV output
- Runs locally without API requirements
- Specialized for Turkish language
- Can list available models with `TTS.list_models()`

### Speech-to-Text (STT)
Use `stt.py` to transcribe audio to text:
```python
python stt.py
```
The script uses OpenAI's Whisper model to transcribe audio files.

### Language Models (LLM)

The project includes multiple LLM implementations:

#### OpenAI GPT-4 (app.py)
Use OpenAI's latest GPT-4 model:
```python
python app.py
```
Features:
- Uses `gpt-4-1106-preview` model
- Temperature and max_tokens control
- System prompt support
- Requires OpenAI API key
- Perfect for complex reasoning and dialogue tasks

#### GPT OSS (gptoss.py)
Use the open-source GPT model via Hugging Face:
```python
python gptoss.py
```
Features:
- Uses the `openai/gpt-oss-20b` model
- Chat completion API similar to OpenAI's interface
- Requires Hugging Face API token

#### LLaMA (llama.py)
Access Meta's LLaMA model through Hugging Face:
```python
python llama.py
```
Features:
- Uses `meta-llama/Meta-Llama-3-8B-Instruct` model
- Optimized for instruction-following tasks
- Chat completion interface
- Requires Hugging Face API token

#### Replicate Integration (replicate.py)
Use Replicate's API to access LLaMA 2:
```python
python replicate.py
```
Features:
- Access to LLaMA 2 70B Chat model
- Customizable parameters (temperature, max tokens)
- System prompt support
- Requires Replicate API token

Each LLM implementation can be configured through environment variables in your `.env` file:

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
