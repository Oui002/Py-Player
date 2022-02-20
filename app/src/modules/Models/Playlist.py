from json import load

class Playlist():

    def __init__(self, name: str,) -> None:
        self.pl_name = name
        self.pl_pos = 1

        with open(f'../playlists/{self.pl_name}.json') as playlist:
            self.data = load(playlist)
        
        self.current = self.data["playlist"][str(self.pl_pos)]
    
    def update_playlist(self,) -> None:
        with open(f'../playlists/{self.pl_name}.json') as playlist:
            self.data = load(playlist)
        
        return

    def add_song(self, name: str,) -> None:
        self.data["playlist"][str(len(self.data.keys()) + 1)]["name"] = name
        self.update_playlist()

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

print(Playlist("testPL").next())