import wave
import numpy as np

def makeOsciList(wavFile):
    if wavFile.getnchannels() == 2:
        return [-1]
    return np.fromBuffer(wavFile.readFrames(-1), "int16").tolist()
    