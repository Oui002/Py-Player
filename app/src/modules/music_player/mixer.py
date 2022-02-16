from pygame import mixer

class Mixer():

    def __init__(self,) -> None:
        self.loaded = list()
        self.currently_loaded = None
        self.volume = float()
        self.thread = None
        
        self.pmixer = mixer
        self.pmixer.init()
    
    def load(self, path: str,) -> None:
        loaded_song = self.pmixer.music.load(f"../music/{path}.mp3")
        self.currently_loaded = loaded_song

        return

    def play(self,) -> None:
        self.pmixer.music.play()

        return

    def set_volume(self, vol: float,) -> None:
        self.volume = round(vol * 100)
        self.pmixer.music.set_volume(vol)

        return
    
    def stop(self,) -> None:
        self.pmixer.music.stop()

        return