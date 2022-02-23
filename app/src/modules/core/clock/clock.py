from pygame import time
from json import load

class Clock():

    def __init__(self,) -> None:
        with open('./modules/core/clock/config.json', 'r+') as config:
            self.config = load(config)

        self.clock = time.Clock()
    
    def tick(self,) -> None:
        self.clock.tick(int(self.config["fps_tick"]))