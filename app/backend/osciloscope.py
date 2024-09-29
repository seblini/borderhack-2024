import wave
import io
import numpy as np

def makeOsciList(wav_file):
    with wave.open(io.BytesIO(wav_file), 'rb') as f:
        if f.getnchannels() == 2:
            return [-1]
        osciList = np.frombuffer(f.readframes(-1), "int16").tolist()
    return osciList
    