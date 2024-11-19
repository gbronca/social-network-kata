from .io import IO
from .clock import Clock
from .post_repository import PostRepository

class Twitter:
    
    def __init__(self, io: IO, clock: Clock, post_repo: PostRepository) -> None:
        self.io = io
        self.clock = clock
        self.post_repo = post_repo
        
    def run(self):
        while True:
            command = self.io.read()
            if command == 'exit':
                break
            
        print('Bye!')
        
    def create_post(self, content: str):
        raise NotImplementedError