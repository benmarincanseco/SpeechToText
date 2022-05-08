import multiprocessing as mp
from random import randint
from time import sleep
import threading as th
import speech_recognition as s
import sys
import os

sound = ["1.wav", "2.wav", "3.wav"]
r = s.Recognizer()

def apiCallProcess(que,proc):
    callNum =que.get()
    with s.AudioFile(sound[callNum]) as source:
        audio = r.record(source)
    try:
        print("The audio file contains: " + r.recognize_google(audio))
        print("call %d complete on process %s " % (callNum, proc))
    except s.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

if __name__ == '__main__':
    q1 = mp.Queue()
    for i in range(3):
        p1 = mp.Process(target=apiCallProcess, args=(q1,1))
        p1.start()
    for num in range(3):
        q1.put(num)
    p1.join()
