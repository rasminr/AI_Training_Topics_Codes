import speech_recognition as sr

rec = sr.Recognizer()
mic = sr.Microphone(device_index=0)
with mic as source:
    print("You can Talk Now!!! ")
    audio = rec.adjust_for_ambient_noise(source)
    audio = rec.listen(source)
    try:
        text = rec.recognize_google(audio, language="en-US")
        print(f"You said {text}")
    except:
        print("Sorry Couldnot hear your Sound")