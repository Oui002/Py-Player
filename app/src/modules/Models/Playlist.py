from json import load, dumps
from ffmpeg import probe

class Playlist():

    def __init__(self, name: str,) -> None:
        self.pl_name = name

        with open(f'../playlists/{self.pl_name}.json', "r+") as playlist:
            try:
                self.data = load(playlist)
            except:
                self.data = {}
            
            if self.data == {}:
                preset = open('./modules/Models/default_playlist.json', "r")
                
                self.data = load(preset)
                self.save_playlist()

                preset.close()

        self.pl_pos = int(self.data["metadata"]["pl_pos"])
        self.data["metadata"]["name"] = self.pl_name
        self.save_playlist()
        
        # self.current = self.data["playlist"][str(self.pl_pos)]

        self.calculate_duration()
    
    def load_playlist(self,) -> None:
        with open(f'../playlists/{self.pl_name}.json') as playlist:
            self.data = load(playlist)
            self.calculate_duration()
        
        return
    
    def save_playlist(self,) -> None:
        with open(f'../playlists/{self.pl_name}.json', "w") as playlist:
            try:
                self.data["metadata"]["pl_pos"] = str(self.pl_pos)
            except:
                self.pl_pos = 1
                self.data["metadata"]["pl_pos"] = str(self.pl_pos)
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
    
    def songs(self,) -> dict:
        return {song: self.data["playlist"].get(song) for song in self.data["playlist"]}

    def add_song(self, name: str,) -> None:
        if self.data["playlist"]["1"] != {}:
            self.data["playlist"][str(len(self.data.keys()) + 1)]["name"] = name
            self.save_playlist()

        else:
            self.data["playlist"][str(1)]["name"] = name
            self.save_playlist()
        
        self.calculate_duration()

        return
    
    def next(self, update_pos: bool = True,) -> str:
        self.load_playlist()

        if update_pos:
            self.pl_pos += 1
            if self.pl_pos > len(list(self.data["playlist"].keys())):
                self.pl_pos = 1
            
            self.save_playlist()

        _next = self.data["playlist"][str(self.pl_pos)]["name"]

        # self.current = self.data["playlist"][str(self.pl_pos)]
        
        return _next
    
    def current(self,) -> str:
        return self.data["playlist"][str(self.pl_pos)]["name"]
    
    def previous(self, update_pos: bool = True,) -> str:
        self.load_playlist()

        if update_pos:
            self.pl_pos -= 1
            if self.pl_pos <= 0:
                self.pl_pos = len(list(self.data["playlist"].keys()))
            
            self.save_playlist()

        _previous = self.data["playlist"][str(self.pl_pos)]["name"]

        # self.current = self.data["playlist"][str(self.pl_pos)]

        return _previous
    
    def release(self,) -> None:
        self.data = {}

        return

# Playlist("ALL").songs()

# minutes and seconds
# flt = str(round(int(Playlist("ALL").data["metadata"]["duration"]) / 10 / 60) / 100).split(".")
# minutes = int(flt[0])
# seconds = round((int(flt[1]) / 100) * 60)

# print(minutes)
# print(seconds)