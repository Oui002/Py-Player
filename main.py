from mixer import Mixer
from time import sleep

import pygame; pygame.init()

if __name__ == "__main__":
    mixer = Mixer()

    mixer.load('MEGALOVANIA')
    mixer.play()

    sleep(100)