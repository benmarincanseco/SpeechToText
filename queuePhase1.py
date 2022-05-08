import multiprocessing as mp
from random import randint
from time import sleep
import threading as th
import speech_recognition as s
import sys
import os

def apiCallProcess(que,proc):
    callNum =que.get()

    print("Received call %d running on process %s " % (callNum, proc))
    timer=randint(1,3)
    print("call %d runningon process %s " % (callNum, proc))
    sleep(timer)
    print("call %d complete on process %s " % (callNum, proc))


if __name__ == '__main__':
    q1 = mp.Queue()
    q2 = mp.Queue()
    q3 = mp.Queue()
    q4 = mp.Queue()
    for i in range(10):
        p1 = mp.Process(target=apiCallProcess, args=(q1,1))
        p1.start()
        p2 = mp.Process(target=apiCallProcess, args=(q2,2))
        p2.start()
        p3 = mp.Process(target=apiCallProcess, args=(q3,3))
        p3.start()
        p4 = mp.Process(target=apiCallProcess, args=(q4,4))
        p4.start()
    for num in range(10):
        q1.put(num)
        q2.put(num)
        q3.put(num)
        q4.put(num)
    p1.join()
    p2.join()
    p3.join()
    p4.join()
