from json import load, dumps
from ffmpeg import probe
from os import listdir

class Playlist():

    def __init__(self, name: str,) -> None:
        self.pl_name = name
        self.pl_pos = 1

        with open(f'../playlists/{self.pl_name}.json', "r+") as playlist:
            try:
                self.data = load(playlist)
            except:
                self.data = {}
            
            if self.data == {}:
                preset = open('./modules/Models/default.json', "r")
                self.data = load(preset)
                self.save_playlist()

                preset.close()
        
        self.current = self.data["playlist"][str(self.pl_pos)]

        self.calculate_duration()
    
    def load_playlist(self,) -> None:
        with open(f'../playlists/{self.pl_name}.json') as playlist:
            self.data = load(playlist)
        
        return
    
    def save_playlist(self,) -> None:
        with open(f'../playlists/{self.pl_name}.json', "w") as playlist:
            playlist.write(dumps(self.data, indent=4))
    
    def calculate_duration(self,) -> None:
        duration = 0

        for key in list(self.data["playlist"].keys()):
            if self.data["playlist"][key] != {}:
                _path = self.data["playlist"][key]["name"] + ".ogg"
                _duration = round(float(probe(f"../music/{_path}")["format"]["duration"]) * 100) * 10

                duration += _duration
            else:
                pass

        self.data["metadata"]["duration"] = str(duration)
        if not len(self.data["playlist"].keys()) == 0:
            self.save_playlist()

        return

    def add_song(self, name: str,) -> None:
        if self.data["playlist"]["1"] != {}:
            self.data["playlist"][str(len(self.data.keys()) + 1)]["name"] = name
            self.save_playlist()
        else:
            self.data["playlist"][str(1)]["name"] = name
            self.save_playlist()

        return
    
    def next(self, update_pos: bool = True,) -> str:
        _next = self.data["playlist"][str(self.pl_pos + 1)]["name"]

        if update_pos:
            self.pl_pos += 1
        self.current = self.data["playlist"][str(self.pl_pos)]
        
        return _next
    
    def previous(self, update_pos: bool = True,) -> str:
        _previous = self.data["playlist"][str(self.pl_pos - 1)]["name"]

        if update_pos:
            self.pl_pos -= 1
        self.current = self.data["playlist"][str(self.pl_pos)]

        return _previous
    
    def release(self,) -> None:
        self.data = {}

        return

Playlist("ALL")

# minutes and seconds
# flt = str(round(int(Playlist("ALL").data["metadata"]["duration"]) / 10 / 60) / 100).split(".")
# minutes = int(flt[0])
# seconds = round((int(flt[1]) / 100) * 60)

# print(minutes)
# print(seconds)