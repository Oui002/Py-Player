from modules.core.DP.display import Display
from modules.core.CK.clock import Clock
from modules.core.IP.input import Input

class Main():

    def __init__(self,) -> None:
        self.display = Display()
        self.clock = Clock()
        self.input = Input()
    
    def run(self,):
        self.display.screen.fill((0,0,50))
        
        self.input.handle_input()

        self.display.update()
        self.clock.tick()