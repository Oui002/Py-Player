from pygame.locals import *
from pygame import event as pgevents
from pygame import quit, mouse
from pygame import FULLSCREEN, RESIZABLE, USEREVENT

from sys import exit
from json import load

from modules.core.display.display import Display
from modules.core.typing.types import *

class Events():
    
    def __init__(self, mixer,) -> None:
        self.display = Display()

        with open('./modules/core/events/config.json', 'r+') as config:
            self.config = load(config)

        self.mixer = mixer

        self.buttons = []
    
    def handle_events(self,) -> None:
        for event in pgevents.get():

            # Window close event
            if event.type == QUIT:
                self.mixer.exit()
                quit()
                exit(0)
            
            # Handling input
            elif event.type == KEYDOWN:
                # Alternative for window close event
                if event.key == K_ESCAPE:
                    self.mixer.exit()
                    quit()
                    exit(0)
                
                # Switching between fullscreen and windowed
                if event.key == K_F11:
                    if self.display.display.get_window_size()[0] == 1920 and self.display.display.get_window_size()[1] == 1080:
                        self.display.display.set_mode((self.display.screen.get_width() / 2, self.display.screen.get_height() / 2), RESIZABLE)
                        # self.gui.update_gui(False)
                    else:
                        self.display.display.set_mode((self.display.screen.get_width(), self.display.screen.get_height()), FULLSCREEN)
                        # self.gui.update_gui(True)

            # Mixer events
            if event.type == USEREVENT:
                self.mixer.music_end()
            
            # Mixer controls
            if event.type == KEYDOWN:
                # Player pos control
                if event.key == K_l or event.key == K_RIGHT:
                    self.mixer.offset_playback_timestamp(+10000)
                    self.mixer.play()

                if event.key == K_j or event.key == K_LEFT:
                    self.mixer.offset_playback_timestamp(-15000)
                    self.mixer.play()
                
                # Volume control
                if event.key == K_PLUS or event.key == K_EQUALS or event.key == K_UP:
                    self.mixer.offset_volume(0.05)
                
                if event.key == K_MINUS or event.key == K_UNDERSCORE or event.key == K_DOWN:
                    self.mixer.offset_volume(-0.05)
                
                # Pausing and unpausing
                if event.key == K_k or event.key == K_SPACE:
                    if self.mixer.pmixer.music.get_busy():
                        self.mixer.stop()
                    else:
                        self.mixer.play()

                # Restarting the song
                if event.key == K_r:
                    self.mixer.restart()
                
                # Enabling/disabling looping of the currently loaded song.
                if event.key == K_e:
                    self.mixer.loop = True

            # Buttons
            if event.type == MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button_res = button.check_for_input(mouse.get_pos())

                    if button_res == True:
                        if button.type == BUTTON_PLAY:
                            self.mixer.play()

                        elif button.type == BUTTON_PREVIOUS:
                            self.mixer.play_prev()

                        elif button.type == BUTTON_NEXT:
                            self.mixer.play_next()
                    
                    

    def update_buttons(self, buttons: list,) -> None:
        self.buttons = buttons
