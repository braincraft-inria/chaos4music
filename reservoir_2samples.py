import reservoirpy as rpy
from reservoirpy.nodes import *
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav


samples = 2
res = Reservoir(samples)


x = np.random.randn(100)

print(res.call(x))

samplerate, kick = wav.read("samples/808_drum_kit/kicks/808-Kicks01.wav")
sr, snare = wav.read("samples/808_drum_kit/snares/808-Clap01.wav")
samples = [kick, snare]


for _ in range(16):

    output = res.call(x)

    x = np.random.randn(100)

    sound = np.argmax(output)

    sd.play(samples[sound], samplerate)
    sd.wait()
