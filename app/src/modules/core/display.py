from pygame import display, FULLSCREEN

class Display():

    def __init__(self, caption: str = 'Py-Player Music Player', start_size: tuple = (1920,1080),) -> None:
        self.display = display

        display.set_caption(caption)
        self.screen = display.set_mode(start_size, FULLSCREEN)
    
    def update(self,):
        display.update()