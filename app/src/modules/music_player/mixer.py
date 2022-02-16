from pygame import mixer
from json import load, dumps
from ..logging.Exceptions import EmptyPathError, SongNotFoundError

class Mixer():

    def __init__(self,) -> None:
        with open('./modules/music_player/config.json', 'r+') as config:
            self.config = load(config)

        self.currently_loaded = self.config["current_song"]
        
        self.pmixer = mixer
        self.pmixer.init()
        self.set_volume(float(self.config["volume"]))
        self.load(self.config["current_song"]["path"])

        self.volume = int()
        self.paused = False

    def save_config(self,) -> None:
        with open('./modules/music_player/config.json', 'w') as config:
            config.write(dumps(self.config, indent=4))
        
        return
    
    def load(self, path: str,) -> None:
        if path != ".mp3":
            try:
                self.pmixer.music.load(f"../music/{path}")
            except FileNotFoundError:
                raise SongNotFoundError(path=path, prefix="MIXER")
            
            self.config["current_song"]["path"] = path
            self.config["current_song"]["timestamp"] = "0"
        else:
            raise EmptyPathError(path=path, prefix="MIXER")
        
        self.save_config()

        return

    def play(self,) -> None:
        self.pmixer.music.play()

        return
    
    def stop(self,) -> None:
        self.pmixer.music.stop()

        return

    def set_volume(self, vol: float,) -> None:
        self.pmixer.music.set_volume(vol)
        self.config["volume"] = str(vol)

        self.save_config()

        return
    
    def resume(self,) -> None:
        self.pmixer.music.unpause()
        self.paused = False
        
        return
    
    def pause(self,) -> None:
        self.pmixer.music.pause()
        self.paused = True
        
        self.config["current_song"]["timestamp"] = str(self.pmixer.music.get_pos())
        self.save_config()

        return
