# Audio Transcription with OpenAI Whisper

This Python project transcribes speech from an `audio.mp3` file into text using the Groq Whisper API. The resulting text is saved to a file named `transcription.txt`.

## Features

- Converts `.mp3` audio to text using Groq's `whisper-3` model.
- Saves the transcribed text to a local file.
- Secure: API key is requested at runtime and not hardcoded.

## Requirements

- Python v3.7+
- Groq
- Donenv

Install the required Python package:

```bash
pip install groq
pip install python-dotenv
```
## Usage
1. Place your audio.mp3 file in the project directory.
2. Run the script:
```bash
python main.py
```
3. The transcription will be saved to transcription.txt