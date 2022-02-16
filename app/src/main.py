from modules.music_player.mixer import Mixer
from time import sleep

import pygame; pygame.init()

def test1():
    _mixer = Mixer()

    _mixer.load('.mp3')
    _mixer.play()
    _mixer.set_volume(0.45)

    print(round(_mixer.pmixer.music.get_volume() * 100))

    sleep(1000)

if __name__ == "__main__":
    test1()