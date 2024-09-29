from urllib.request import urlopen
from dotenv import load_dotenv
import os
import json
import string

def get_wav_file_from_MW(word):
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
        wav_file = r.read()

    return wav_file