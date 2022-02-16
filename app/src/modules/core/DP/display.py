from pygame import display, FULLSCREEN
from json import load, dumps

class Display():

    def __init__(self, caption: str = 'Py-Player Music Player',) -> None:
        self.display = display

        with open('./modules/core/CK/config.json', 'r+') as config:
            self.config = load(config)

        display.set_caption(caption)
        self.screen = display.set_mode((self.display.Info().current_w, self.display.Info().current_h), FULLSCREEN)
    
    def update(self,):
        display.update()