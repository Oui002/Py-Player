from pygame import FULLSCREEN, display
from json import load

class Display():

    def __init__(self, caption: str = 'Py-Player Music Player [WIP]',) -> None:
        self.display = display

        with open('./modules/core/CK/config.json', 'r+') as config:
            self.config = load(config)

        display.set_caption(caption)
        self.screen = display.set_mode((self.display.Info().current_w, self.display.Info().current_h), FULLSCREEN)

        self.window_startup()
    
    def update(self,) -> None:
        self.display.update()
    
    def window_startup(self,) -> None:
        self.display.set_mode((self.screen.get_width() / 2, self.screen.get_height() / 2), FULLSCREEN)
