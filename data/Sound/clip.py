import os
import librosa
import numpy as np

folder = 'ori/'

All = os.listdir(folder)
for i in All:
    I, fs = librosa.load(folder + i)
    I_new = I[:50000]
    librosa.output.write_wav(folder + 'cut_' + i, I_new, fs)
