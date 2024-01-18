import whisper
import spacy

# Function to load the Whisper model
def load_whisper_model():
    return whisper.load_model("base")

# Function to prompt for file path
def get_file_path():
    return input("Enter the file path to your MP3 file: ")

# Function to transcribe audio using Whisper
def transcribe_audio(model, file_path):
    return model.transcribe(file_path)

# Function to format the transcript
def format_transcript(transcript_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(transcript_text)
    formatted_text = ''

    for sent in doc.sents:
        formatted_text += str(sent).strip() + '\n\n'

    return formatted_text

# Main execution flow
def main():
    model = load_whisper_model()
    file_path = get_file_path()
    result = transcribe_audio(model, file_path)
    formatted_transcript = format_transcript(result["text"])
    print(formatted_transcript)

# Execute the main function
if __name__ == "__main__":
    main()
