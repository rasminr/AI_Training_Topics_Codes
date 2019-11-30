from playsound import playsound
import os
import datetime
import time

# Year = input("Year : ")
# Month = input("Month : ")
# Date = input("Date : ")
# Hour = input("Hour : ")
# Minutes = input("Minutes : ")

startTime = datetime.datetime(2019,11,30,10,41)
stopTime = datetime.datetime(2019,11,30,10,42)
soundCount = 1

# Audio Played for 1 Minute has Generated 232 samples.
# Playing Audio for 3 Minute can Generate a total 696 samples.
# Audio Length below 1 second

while datetime.datetime.now() < startTime:
    time.sleep(1)
while datetime.datetime.now() >= startTime and datetime.datetime.now() <= stopTime:
    for sounds in os.listdir("test"):
        playsound(os.path.join("test",sounds))
        print(f"Sound Played Count: {soundCount}")
        soundCount = soundCount + 1