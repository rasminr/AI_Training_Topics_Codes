import numpy as np
import wavio
import os

try:
    os.mkdir("test")
except FileExistsError:
    pass

ratepersecond = 22050
time = 1
freq = 1000.0
count = 400

while count <= 4000:
    linspace = np.linspace(count,time, time*ratepersecond, endpoint=False)
    sinewave = np.sin(2*np.pi * count * linspace)
    wavio.write(os.path.join("test",f"sine {count}.wav"), sinewave, ratepersecond, sampwidth=3)
    count = count + 400