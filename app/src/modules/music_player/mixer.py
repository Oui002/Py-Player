from pygame import mixer
from json import load, dumps

class Mixer():

    def __init__(self,) -> None:
        self.currently_loaded = None
        self.volume = int()
        with open('./modules/music_player/config.json', 'r+') as config:
            self.config = load(config)
        
        self.pmixer = mixer
        self.pmixer.init()
        self.set_volume(float(self.config["volume"]))

    def save_config(self,) -> None:
        with open('./modules/music_player/config.json', 'w') as config:
            config.write(dumps(self.config, indent=4))
    
    def load(self, path: str,) -> None:
        loaded_song = self.pmixer.music.load(f"../music/{path}.mp3")
        self.currently_loaded = loaded_song

        return

    def play(self,) -> None:
        self.pmixer.music.play()

        return

    def set_volume(self, vol: float,) -> None:
        self.pmixer.music.set_volume(vol)
        self.config["volume"] = str(vol)

        return
    
    def stop(self,) -> None:
        self.pmixer.music.stop()

        return
