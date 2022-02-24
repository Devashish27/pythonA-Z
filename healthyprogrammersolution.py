from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # musiconloop("water.mp3.py", "stop")

    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking Time. Enter 'drank' to stop the alarm..")
            musiconloop('water.mp3.py', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye Exercise Time. Enter 'done eyes' to stop the alarm..")
            musiconloop('eyes.mp3.py', 'done eyes')
            init_eyes = time()
            log_now("Eyes Relaxed At")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'done Phy' to stop the alarm..")
            musiconloop('physical.mp3.py', 'done phy')
            init_exercise = time()
            log_now("Physical Activity Done At")

