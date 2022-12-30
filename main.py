import speech_recognition as sr
import time
pre_time = time.time()
r = sr.Recognizer()

with sr.AudioFile(r"D:\Company\Code\pythonProject\HopQuocHoi.wav") as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio, language="vi-VI")
    print("Text: " + s)
    print('time:', time.time()-pre_time)
except Exception as e:
    print("Exception: " + str(e))
