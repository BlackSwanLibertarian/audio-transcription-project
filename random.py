import openai
import json

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            file=audio_file,
            model="whisper-1",
            response_format="text",
            language="en"
        )

    return transcript

def format_output(transcript):
    formatted_output = ""
    for item in transcript["alternatives"][0]:
        if "speaker_label" in item:
            formatted_output += "\nSpeaker: {}\n".format(item["speaker_label"])
        formatted_output += item["content"] + "\n"

    return formatted_output

if __name__ == "__main__":
    input_file = "C:\\Users\\raamc\\Downloads\\Peter Thiel on the Global Economy, the State of Our Technology, and Artificial Intelligence.mp3"
    transcript = transcribe_audio(input_file)
    formatted_output = format_output(transcript)

    print(formatted_output)