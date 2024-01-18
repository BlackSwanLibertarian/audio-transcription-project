Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import deepspeech
... import wave
... import moviepy.editor as mp
... 
... # Load the mp3 file
... clip = mp.AudioFileClip("input.mp3")
... 
... # Convert mp3 to wav
... clip.write_audiofile("converted.wav") 
... 
... # Load DeepSpeech model
... model = deepspeech.Model("deepspeech-0.9.3-models.pbmm")
... model.enableExternalScorer("deepspeech-0.9.3-models.scorer")
... 
... # Transcribe audio
... wav = wave.open("converted.wav", "rb") 
... audio = model.stt(wav)
... 
