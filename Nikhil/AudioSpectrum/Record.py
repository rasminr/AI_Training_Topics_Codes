import sounddevice as sd
from scipy.io import wavfile
import os as os
import datetime
import time

try:
    os.mkdir("Recordings")
except FileExistsError:
    pass

FramesperSec = 44100
RecDur = 1
count = 0
recount = 0
startTime = datetime.datetime(2019,11,29,22,25)
stopTime = datetime.datetime(2019,11,29,22,28)

while datetime.datetime.now() < startTime:
    time.sleep(1)

while datetime.datetime.now >= startTime and datetime.datetime.now() <= stopTime:
    recordAudio = sd.rec((RecDur * FramesperSec),samplerate=FramesperSec,channels=2)
    sd.wait()
    wavfile.write(os.path.join("Recordings",f"recorded {recount}.wav"),FramesperSec,recordAudio)
    recount = recount + 1
    count = count + 1