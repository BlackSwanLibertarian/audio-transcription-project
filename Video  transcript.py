import speech_recognition as sr
from pydub import AudioSegment

def mp3_to_text(filename):
    # Convert mp3 to wav
    sound = AudioSegment.from_mp3(filename)
    wav_filename = filename.split('.')[0] + ".wav"
    sound.export(wav_filename, format="wav")

    # Recognize the content
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_filename) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    file_name = input("C:\\Users\\raamc\\Downloads\\yt5s.com - Copy of In Tech We Trust_ A Debate with Peter Thiel and Marc Andreessen (128 kbps).mp3")
    result = mp3_to_text(file_name)
    if result:
        print("Transcription:\n", result)
