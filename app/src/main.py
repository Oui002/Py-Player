from modules.music_player.mixer import Mixer
from time import sleep

import pygame; pygame.init()

def test1():
    _mixer = Mixer()

    _mixer.load('MEGALOVANIA.mp3')
    _mixer.play()

    sleep(1000)

if __name__ == "__main__":
    test1()