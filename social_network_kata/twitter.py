from .io import IO

class Twitter:
    
    def __init__(self, io: IO) -> None:
        self.io = io
        
    def run(self):
        while True:
            command = self.io.read()
            if command == 'exit':
                break
            
        print('Bye!')