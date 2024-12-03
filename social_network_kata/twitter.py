from .io import IO
from .clock import Clock
from .post_repository import PostRepository
from .command_parser import CommandParser
from .post import Post

class Twitter:
    
    def __init__(self, io: IO, clock: Clock, post_repo: PostRepository, command_parser: CommandParser) -> None:
        self.io = io
        self.clock = clock
        self.post_repo = post_repo
        self.command_parser = command_parser
        
    def run(self):
        while True:
            command = self.io.read()
            if command == 'exit':
                break

            action, args = self.command_parser.parse_command(command)
            
            if action == "POST":
                name, message = args
                self.create_post(name, message)

            if action == "READ":
                name = args[0]
                self.get_posts_by_user(name)
            
        print('Bye!')
        
    def create_post(self, name: str, message: str):
        self.post_repo.create_post(name, message)

    def get_posts_by_user(self, name: str) -> list[Post]:
        return self.post_repo.get_posts_by_user(name)