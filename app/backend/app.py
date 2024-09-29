from flask import Flask
from urllib.request import urlopen
from dotenv import load_dotenv
import os
import sys
import json
import string
import io
import wave

app = Flask(__name__)

@app.route("/<word>")
def get_from_api(word):
    load_dotenv()
    MW_COLLEGIATE_API_KEY = os.getenv('MW_COLLEGIATE_API_KEY')
    with urlopen(f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={MW_COLLEGIATE_API_KEY}') as r:
        data = json.load(r)
    
    audio = data[0]['hwi']['prs'][0]['sound']['audio']

    language_code = 'en'
    country_code = 'us'
    audio_format = 'wav'

    subdirectory = audio[0]
    if 'bix' == audio[:3]:
        subdirectory = 'bix'
    elif 'gg' == audio[:2]:
        subdirectory = 'gg'
    elif audio[0] in string.punctuation or audio[0].isdigit():
        subdirectory = 'number'
    
    base_filename = audio

    with urlopen(f'https://media.merriam-webster.com/audio/prons/{language_code}/{country_code}/{audio_format}/{subdirectory}/{base_filename}.{audio_format}') as r:
        wav_data = r.read()

    with wave.open(io.BytesIO(wav_data), 'rb') as wav_file:
        sample_rate = wav_file.getframerate()
        num_channels = wav_file.getnchannels()
        num_frames = wav_file.getnframes()
        audio_data = wav_file.readframes(num_frames)

    return f'{audio_data}'