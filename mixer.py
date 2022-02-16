from pygame import mixer

import threading

class Mixer():

    def __init__(self,) -> None:
        self.loaded = list()
        self.currently_playing = None
        self.thread = None
        
        self.mixer = mixer
        self.mixer.init()
    
    def load(self, path) -> None:
        loaded_song = self.mixer.music.load("./" + path + ".mp3")
        self.currently_playing = loaded_song

        return

    def play_sound(self,) -> None:
        self.mixer.music.play()

        playing=True
        while playing:
            if self.mixer.music.get_busy():
                pass
            else:
                playing=False
                self.thread = None

        return

    def play(self,) -> None:
        play_thread = threading.Thread(target=self.play_sound)
        play_thread.daemon=True
        play_thread.start()

        self.thread = play_thread
    
    def stop(self,) -> None:
        self.mixer.music.stop()
