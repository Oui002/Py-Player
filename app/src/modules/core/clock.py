from pygame import time

class Clock():

    def __init__(self,) -> None:
        self.clock = time.Clock()
    
    def tick(self, fps: int = 60,) -> None:
        self.clock.tick(fps)