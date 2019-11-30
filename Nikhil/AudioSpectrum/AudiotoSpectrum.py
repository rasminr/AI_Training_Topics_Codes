from playsound import playsound
import os as os
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

playcount = 0
for sounds in os.listdir("testsounds"):
    fs, WaveFile = wavfile.read(os.path.join("testsounds",sounds))
    N = 500
    a, b, c = signal.spectrogram(WaveFile,fs,window=signal.blackman(N),nfft=N)
    plt.pcolormesh(b,c,10*np.log10(c))
    plt.plot(WaveFile)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [seg]')
    plt.title('Spectrogram with scipy.signal',size=16)
    plt.show()
    playcount = playcount+1
print("Done!!!")
