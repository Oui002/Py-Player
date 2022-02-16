from pygame.locals import *
from pygame import event as pgevents
from pygame import quit
from sys import exit

from modules.core.display import Display

from ..music_player.mixer import Mixer

class Input():
    
    def __init__(self,) -> None:
        pass
    
    def handle_input(self,):
        for event in pgevents.get():
            if event.type == QUIT:
                quit()
                exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                    exit(0)
                
                if event.key == K_p:
                    Mixer().play()
                
                if event.key == K_F11:
                    Display().display.toggle_fullscreen()