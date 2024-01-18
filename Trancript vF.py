import whisper
import os

def transcribe_and_format(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found. Please check the file path.")
        return

    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio
    result = model.transcribe(file_path)

    # Initialize variables for speaker tracking
    current_speaker = None
    speaker_count = {}

    # Format and print the transcription
    for segment in result["segments"]:
        speaker = segment['speaker']
        if speaker != current_speaker:
            current_speaker = speaker
            speaker_count[speaker] = speaker_count.get(speaker, 0) + 1
            print(f"\nSpeaker {speaker_count[speaker]}:\n")
        print(segment['text'], end=" ")

# File path to the MP3 file
file_path = "C:\\Users\\raamc\\Downloads\\Sam Altman_ OpenAI CEO on GPT-4, ChatGPT, and the Future of AI _ Lex Fridman Podcast #367.mp3"

# Transcribe and format the audio file
transcribe_and_format(file_path)
