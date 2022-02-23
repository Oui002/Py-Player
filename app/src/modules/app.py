from modules.music_player.mixer import Mixer
from modules.core.clock.clock import Clock
from modules.core.display.display import Display
from modules.core.GUI._ import GUI
from modules.core.events.events import Events
from modules.core.typing.types import *

class Main():

    def __init__(self,) -> None:
        self.GUI_ENABLED = True

        self.mixer = Mixer()

        self.clock = Clock()
        self.display = Display()
        self.gui = GUI(self.display.screen)
        self.events = Events(self.mixer)

        self.view = PLAYLIST_VIEW
    
    def run(self,):
        self.display.screen.fill((20,100,200))

        self.events.update_buttons(self.gui.buttons)
        self.events.handle_events()

        if self.view == PLAYLIST_VIEW:
            self.gui.playlist_view()
        if self.view == SETTINGS_VIEW:
            self.gui.settings_view()

        self.display.update()
        self.clock.tick()