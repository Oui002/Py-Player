from pygame.locals import *
from pygame import event as pgevents
from pygame import quit
from pygame import FULLSCREEN, RESIZABLE

from sys import exit
from json import load, dumps

from modules.core.DP.display import Display
from ...music_player.mixer import Mixer

class Input():
    
    def __init__(self,) -> None:
        self.display = Display()
        self.mixer = Mixer()

        with open('./modules/core/CK/config.json', 'r+') as config:
            self.config = load(config)
    
    def handle_input(self,) -> None:
        for event in pgevents.get():
            if event.type == QUIT:
                self.mixer.exit()
                quit()
                exit(0)
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.mixer.exit()
                    quit()
                    exit(0)
                
                if event.key == K_k or event.key == K_SPACE:
                    if self.mixer.pmixer.music.get_busy():
                        self.mixer.pause()
                    elif self.mixer.paused:
                        self.mixer.resume()
                    else:
                        self.mixer.play()
                       
                    

                if event.key == K_r:
                    self.mixer.restart()
                
                if event.key == K_F11:
                    if self.display.display.get_window_size()[0] == 1920 and self.display.display.get_window_size()[1] == 1080:
                        self.display.display.set_mode((self.display.screen.get_width() / 2, self.display.screen.get_height() / 2), RESIZABLE)
                    else:
                        self.display.display.set_mode((self.display.screen.get_width(), self.display.screen.get_height()), FULLSCREEN)
