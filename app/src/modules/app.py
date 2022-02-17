from modules.music_player.mixer import Mixer
from modules.core.DP.display import Display
from modules.core.CK.clock import Clock
from modules.core.IP.input import Input

class Main():

    def __init__(self,) -> None:
        self.display = Display()
        self.clock = Clock()
        self.input = Input()

        self.mixer = Mixer()
    
    def run(self,):
        self.display.screen.fill((0,0,50))
        
        self.input.handle_input()

        self.mixer.player_events()

        self.display.update()
        self.clock.tick()