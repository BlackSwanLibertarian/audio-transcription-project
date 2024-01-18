# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:41:13 2023

@author: raamc
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import os

# Spotify API credentials
client_id = 'ac5fd647f712470687894d9804a79421' 
client_secret = '5ee6e81c57144e6bbce4fc1e167e62dd'

# Authenticate with Spotify 
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Get podcast episode link from user
link = input("https://open.spotify.com/episode/7jpE3mTJSUPkUHhtnCxtSv")

# Parse link to get episode id
episode_id = link.split('/')[-1].split('?')[0]

# Get episode metadata
episode = sp.episode(episode_id)

# Construct file path to save to desktop
path = f"C:\\Users\\raamc\\OneDrive\\Desktop\\Projects\\banklessafrica.mp3"

# Download audio
response = requests.get(episode['audio_preview_url'])

with open(path, 'wb') as f:
    f.write(response.content)

print(f"C:\\Users\\raamc\\OneDrive\\Desktop\\Projects")
