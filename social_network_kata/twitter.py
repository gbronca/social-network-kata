from .io import IO
from .clock import Clock
from .command_parser import CommandParser
from .post import Post
from .post_formatter import PostFormatter
from .post_repository import PostRepository



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

            if action not in ["POST", "READ"]:
                return ValueError

            if action == "POST":
                name, message = args
                self.create_post(name, message)

            if action == "READ":
                name = args[0]
                posts = self.get_posts_by_user(name)
                post_formatter = PostFormatter(self.clock)
                formatted_posts = post_formatter.format_posts(posts=posts)
                for post in formatted_posts:
                    print(post)


            
        print('Bye!')
        
    def create_post(self, name: str, message: str):
        self.post_repo.create_post(name, message)

    def get_posts_by_user(self, name: str) -> list[Post]:
        return self.post_repo.get_posts_by_user(name)