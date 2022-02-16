class EmptyPathError(Exception):

    def __init__(self, prefix, message='This program can not use file: ".mp3"',) -> None:
        self.message = f"[{prefix}] {message}"
        super().__init__(self.message)