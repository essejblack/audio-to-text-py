from groq import Groq
from dotenv import load_dotenv
import os
import json


load_dotenv()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
api_key = os.getenv("AI_API_KEY")

if api_key is None:
    raise ValueError("AI_API_KEY environment variable is not set.")


def transcribe_audio(audio_file_path):
    client = Groq(
        api_key=api_key,
    )    

    if not os.path.exists(audio_file_path):
        print(f"File '{audio_file_path}' not found.")
        return

    try:
        global transcription
        with open(audio_file_path, "rb") as audio_file:
            transcription  = client.audio.transcriptions.create(
                model="whisper-large-v3-turbo",
                file=audio_file
            )
        
        with open("transcription.txt", "w", encoding="utf-8") as f:
            f.write(transcription.text)

        print("Transcription saved to 'transcription.txt'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    transcribe_audio("audio.mp3")
