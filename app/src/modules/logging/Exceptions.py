class EmptyPathError(Exception):

    def __init__(self, path, prefix,) -> None:
        self.message = f"[{prefix}] This program can not use file: {path}"
        super().__init__(self.message)

class SongNotFoundError(Exception):

    def __init__(self, path, prefix) -> None:
        self.message = f"[{prefix}] Could not find file: {path}"
        super().__init__(self.message)