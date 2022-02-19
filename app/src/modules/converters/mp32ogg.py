from pydub import AudioSegment
from os import listdir, remove

def mp32ogg(path: str = "../music"):
    files = listdir(path)
    for file in files:
        if not f"{file[:-4]}.ogg" in files:
            if file.endswith('.mp3'):
                try:
                    AudioSegment.from_mp3(f"{path}/{file}").export(f"{path}/{file[:-4]}.ogg", format="ogg")
                    remove(f"{path}/{file}")

                except:
                    remove(f"{path}/{file}")
                    remove(f"{path}/{file[:-4]}.ogg")

                    pass
                