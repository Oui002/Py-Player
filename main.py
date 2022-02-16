from mixer import Mixer
from time import sleep
from sys import exit

import pygame; pygame.init()

if __name__ == "__main__":
    mixer = Mixer()

    mixer.load('MEGALOVANIA')
    mixer.play()

    sleep(1000)

    # while True:
    #     if mixer.mixer.music.get_busy():
    #         pass
    #     else:
    #         print("exiting")
    #         exit(0)