from .io import IO

class Twitter:
    def __init__(self, io: IO) -> None:
        self.io = io
        
    def run(self):
        raise NotImplementedError