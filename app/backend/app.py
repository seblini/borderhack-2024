from flask import Flask
import io
import wave
import json
import base64

from get_wav_file_from_MW import get_wav_file_from_MW
from osciloscope import makeOsciList

app = Flask(__name__)

@app.route("/get_wav_data/<word>")
def get_wav_data(word):
    wav_file = get_wav_file_from_MW(word)

    wav_file_base64 = base64.b64encode(wav_file).decode('utf-8')

    osciList = makeOsciList(wav_file)

    data = {
        'wav_file': wav_file_base64,
        'frequency_list': osciList,
    }

    return osciList