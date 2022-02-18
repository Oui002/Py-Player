from modules.music_player.mixer import Mixer
from modules.core.DP.display import Display
from modules.core.CK.clock import Clock
from modules.core.ES.events import Events

class Main():

    def __init__(self,) -> None:
        self.display = Display()
        self.clock = Clock()
        self.events = Events()

        self.mixer = Mixer()
    
    def run(self,):
        self.display.screen.fill((0,0,50))
        
        self.events.handle_input()

        self.display.update()
        self.clock.tick()