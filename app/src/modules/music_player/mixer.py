from pygame import mixer
from json import load, dumps
from ..logging.Exceptions import EmptyPathError, SongNotFoundError

class Mixer():

    def __init__(self,) -> None:
        with open('./modules/music_player/config.json', 'r+') as config:
            self.config = load(config)
        
        self.pmixer = mixer
        self.pmixer.init()
        self.set_volume(float(self.config["volume"]))
        self.load(self.config["current_song"]["path"], False)

        self.volume = int()
        self.paused = False

    def save_config(self,) -> None:
        with open('./modules/music_player/config.json', 'w') as config:
            config.write(dumps(self.config, indent=4))
        
        return
    
    def load(self, path: str, reset_timestamp: bool) -> None:
        if path != ".mp3":
            try:
                self.pmixer.music.load(f"../music/{path}")
            except FileNotFoundError:
                raise SongNotFoundError(path=path, prefix="MIXER")
            
            self.config["current_song"]["path"] = path
            if reset_timestamp:
                self.config["current_song"]["timestamp"] = "0"
        else:
            raise EmptyPathError(path=path, prefix="MIXER")
        
        self.save_config()

        return

    def play(self, start,) -> None:
        self.pmixer.music.play(start=float(int(start) / 100))

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
    
    def restart(self,) -> None:
        if not self.pmixer.music.get_pos() == 0:
            if not self.paused:
                self.pause()
            
            self.config["current_song"]["timestamp"] = "0"
            self.save_config()
    
            self.stop()
            self.play(self.config["current_song"]["timestamp"])
        
        return
