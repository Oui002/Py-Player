from modules.app import Main
from modules.music_player.mixer import Mixer

import pygame; pygame.init()

# def test1():
#     _mixer = Mixer()

#     _mixer.load('MEGALOVANIA.mp3')
#     _mixer.play()

#     sleep(1000)

def main():
    app = Main()
    
    while True:
        app.run()

if __name__ == "__main__":
    main()