from .io import IO
from .clock import Clock

class Twitter:
    
    def __init__(self, io: IO, clock: Clock) -> None:
        self.io = io
        self.clock = clock
        
    def run(self):
        while True:
            command = self.io.read()
            if command == 'exit':
                break
            
        print('Bye!')