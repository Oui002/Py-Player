from time import sleep
from pygame import mixer

import threading

class Mixer():

    def __init__(self,) -> None:
        self.loaded = list()
        self.currently_playing = None
        self.volume = float()
        self.thread = None
        
        self.pmixer = mixer
        self.pmixer.init()
    
    def load(self, path: str) -> None:
        loaded_song = self.pmixer.music.load(f"./{path}.mp3")
        self.currently_playing = loaded_song

        return

    def set_volume(self, vol: float) -> None:
        self.volume = round(vol * 100)
        self.pmixer.music.set_volume(vol)

        return

    # def playsound_target(self,) -> None:
    #     self.pmixer.music.play()

    #     return

    # def play(self,) -> None:
    #     play_thread = threading.Thread(name="mixer-music-thread", target=self.playsound_target)
    #     play_thread.daemon=True
    #     play_thread.start()

    #     self.thread = play_thread

    #     return
    
    def stop(self,) -> None:
        self.pmixer.music.stop()

        return
