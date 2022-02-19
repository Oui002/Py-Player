from pygame import mixer
from pygame import USEREVENT

from json import load, dumps
from ffmpeg import probe
from time import sleep

import asyncio
import threading

from ..logging.Exceptions import EmptyPathError
from ..converters.mp32ogg import mp32ogg

class Mixer():

    def __init__(self,) -> None:
        with open('./modules/music_player/config.json', 'r+') as config:
            self.config = load(config)
        
        self.pmixer = mixer
        self.pmixer.init()
        self.set_volume(float(self.config["volume"]))
        self.load(self.config["current_song"]["path"], False)

        self.volume = int()
        self.saved_mixer_pos = 0
        self.paused = False
        self.pause_block = False

        self.MUSIC_END = USEREVENT

        self.convert_music()
        
        self.start_pos_update()
        

    def save_config(self,) -> None:
        if int(self.config["current_song"]["timestamp"]) < 0:
            self.config["current_song"]["timestamp"] = "0"

        with open('./modules/music_player/config.json', 'w') as config:
            config.write(dumps(self.config, indent=4))
        
        return
    
    def get_config(self,) -> object:
        return self.config
    
    def convert_music(self,) -> None:
        mp32ogg()
        
        return

    def start_pos_update(self,) -> None:
        t = threading.Thread(target=self._pos_update_loop)
        t.daemon = True
        t.start()

    def _pos_update_loop(self,) -> None:
        while True:
            if not self.paused and self.pmixer.music.get_busy():
                self.config["current_song"]["timestamp"] = str(self.pmixer.music.get_pos() - self.saved_mixer_pos + int(self.config["current_song"]["timestamp"]))
                self.save_config()

                self.saved_mixer_pos = self.pmixer.music.get_pos()

            sleep(0.05)
    
    def load(self, path: str, reset_start: bool = True) -> None:
        if path != ".ogg":
            self.pmixer.music.load(f"../music/{path}")
            
            self.config["current_song"]["path"] = path
            self.config["current_song"]["timestamp"] = "0"
            self.config["current_song"]["length"] = str(int(float(probe(f"../music/{path}")["format"]["duration"])) * 1000)

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

        self.saved_mixer_pos = 0

        self.paused = False

        return
    
    def stop(self,) -> None:
        self.pause()
        self.pmixer.music.stop()

        return

    def set_volume(self, vol: float,) -> None:
        self.pmixer.music.set_volume(vol)

        self.config["volume"] = str(vol)
        self.save_config()

        return
    
    def increment_playback_timestamp(self, amount: int,) -> None:
        self.pause()

        current_pos = int(self.config["current_song"]["timestamp"])
        new_pos = amount + current_pos

        if new_pos < 0:
            new_pos = 0

            res = current_pos - amount
            self.config["current_song"]["start_pos"] = str(int(self.config["current_song"]["start_pos"]) - res)

            if int(self.config["current_song"]["start_pos"]) < 0:
                self.config["current_song"]["start_pos"] = "0"

        self.config["current_song"]["timestamp"] = str(new_pos)
        self.save_config()

        self.play()

        return
    
    def exit(self,) -> None:
        self.stop()

        self.config["current_song"]["start_pos"] = str(int(self.config["current_song"]["timestamp"]) + int(self.config["current_song"]["start_pos"]))
        self.config["current_song"]["timestamp"] = "0"
        self.save_config()

        return
    
    def pause(self,) -> None:
        self.pmixer.music.pause()
        self.paused = True
        
        if self.saved_mixer_pos > self.pmixer.music.get_pos():
            self.config["current_song"]["timestamp"] = str(self.pmixer.music.get_pos() + int(self.config["current_song"]["timestamp"]))
            self.save_config()

            return

        self.config["current_song"]["timestamp"] = str(self.pmixer.music.get_pos() - self.saved_mixer_pos + int(self.config["current_song"]["timestamp"]))
        self.save_config()

        return
    
    def restart(self,) -> None:
        if not self.pmixer.music.get_pos() == 0:
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
