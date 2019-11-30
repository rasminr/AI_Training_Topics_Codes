from playsound import playsound
from pydub import AudioSegment
import os as os
import AudioConverter as ac


soundcount = 0
audioNames = []
for files in os.listdir("testsounds"):
    if files.endswith(".mp3"):
        Convertfrom = AudioSegment.from_mp3(os.path.join("testsounds",files))
        ConvertDes = Convertfrom.export(os.path.join("testsounds",f"Sounds {soundcount}.wav",format="wav"))
        soundcount = soundcount+1
        # os.remove(files)
    else:
        pass