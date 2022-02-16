from mixer import Mixer
from time import sleep

import pygame; pygame.init()

def test1():
    _mixer = Mixer()

    _mixer.load('MEGALOVANIA')
    _mixer.pmixer.music.play()
    _mixer.set_volume(0.35)

    print(round(_mixer.pmixer.music.get_volume() * 100))

    sleep(1000)

if __name__ == "__main__":
    test1()