from mixer import Mixer
from time import sleep

import pygame; pygame.init()

if __name__ == "__main__":
    mixer = Mixer()

    mixer.load('MEGALOVANIA')
    mixer.pmixer.music.play()
    mixer.set_volume(0.35)

    print(round(mixer.pmixer.music.get_volume() * 100))

    sleep(100)

    # while True:
    #     song_time = mixer.pmixer.music.get_pos() / 1000
    #     print(song_time)
    #     sleep(0.1)