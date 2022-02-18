from pygame import mixer
from pygame import event as pgevents
from pygame import USEREVENT

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

        self.MUSIC_END = USEREVENT

    def save_config(self,) -> None:
        with open('./modules/music_player/config.json', 'w') as config:
            config.write(dumps(self.config, indent=4))
        
        return
    
    def get_config(self,) -> object:
        return self.config
    
    def load(self, path: str, reset_start: bool = True) -> None:
        if path != ".mp3":
            try:
                self.pmixer.music.load(f"../music/{path}")
            except FileNotFoundError:
                raise SongNotFoundError(path=path, prefix="MIXER")
            
            self.config["current_song"]["path"] = path
            self.config["current_song"]["timestamp"] = "0"
            if reset_start:
                self.config["current_song"]["start_pos"] = "0"
        else:
            raise EmptyPathError(path=path, prefix="MIXER")
        
        self.save_config()

        return

    def play(self,) -> None:
        self.save_config()

        if self.pmixer.music.get_busy():
            self.paused = True

        self.pmixer.music.play(start=float((int(self.config["current_song"]["timestamp"]) + int(self.config["current_song"]["start_pos"])) / 1000))
        self.pmixer.music.set_endevent(self.MUSIC_END)

        self.paused = False

        return
    
    def stop(self,) -> None:
        self.pmixer.music.stop()

        return

    def set_volume(self, vol: float,) -> None:
        self.pmixer.music.set_volume(vol)

        self.config["volume"] = str(vol)
        self.save_config()

        return
    
    def set_playback_timestamp(self, start: str,) -> None:
        self.config["current_song"]["timestamp"] = start
        self.save_config()

        return
    
    def exit(self,) -> None:
        self.config["current_song"]["start_pos"] = str(int(self.config["current_song"]["timestamp"]) + int(self.config["current_song"]["start_pos"]))
        self.config["current_song"]["timestamp"] = "0"
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
            self.config["current_song"]["start_pos"] = "0"
            self.save_config()
    
            self.play()
        
        return

    def music_end(self,) -> None:
        if self.paused == False:
            self.config["current_song"]["timestamp"] = "0"
            self.config["current_song"]["start_pos"] = "0"
            self.save_config()
        
        return
