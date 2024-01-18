# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:12:23 2023

@author: raamc
"""

from pytube import YouTube
import os
import speech_recognition as sr
from pydub import AudioSegment

def download_audio(video_url, audio_path):
    yt = YouTube(video_url)
    yt.streams.filter(only_audio=True).first().download(output_path=audio_path)

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    audio_segment = AudioSegment.from_file(audio_file_path, format="mp4")
    audio_segment.export("temp.wav", format="wav")
    
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        transcript = recognizer.recognize_sphinx(audio_data)
        
    os.remove("temp.wav")
    
    formatted_transcript = ""
    speaker_count = 1
    for sentence in transcript.split('.'):
        formatted_transcript += f"Speaker {speaker_count}: {sentence.strip()}\n"
        speaker_count = 1 if speaker_count == 2 else 2

    return formatted_transcript

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    audio_path = "./audio_files"
    audio_file_path = os.path.join(audio_path, "audio.mp4")

    # Download Audio
    download_audio(video_url, audio_path)

    # Transcribe Audio
    transcript = transcribe_audio(audio_file_path)
    print("Generated Transcript: \n", transcript)
