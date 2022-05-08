import speech_recognition as sr

AUDIO_FILE = ("test1.wav")


r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:

    audio = r.record(source)

try:
    print("The audio file contains: " + r.recognize_google(audio))

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
