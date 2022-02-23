from modules.core.GUI.elements.button import Button
from modules.core.typing.types import *

from pygame import font, mouse

class GUI():

    def __init__(self, screen,) -> None:
        self.screen = screen
        self.buttons = []

    def playlist_view(self,) -> None:
        self.screen.fill("black")

        self.buttons = [
            Button("play.png", (1920/2, 1080/2), "PLAY", font.SysFont("Arial", 100), (0, 20, 60), (60, 20, 0), BUTTON_PLAY), 
            Button("play.png", (1920/3, 1080/2), "PREVIOUS", font.SysFont("Arial", 100), (0, 20, 60), (60, 20, 0), BUTTON_PREVIOUS), 
            Button("play.png", (1920/3 * 2, 1080/2), "NEXT", font.SysFont("Arial", 100), (0, 20, 60), (60, 20, 0), BUTTON_NEXT)
        ]

        for button in self.buttons:
            button.change_color(mouse.get_pos())
            button.update(self.screen)
    
    def settings_view(self,) -> None:
        self.screen.fill("white")