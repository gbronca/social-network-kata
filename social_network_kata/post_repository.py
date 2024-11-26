from social_network_kata.post import Post
from social_network_kata.clock import Clock
class PostRepository:

    def __init__(self, clock: Clock):
        self.clock = clock
        self.posts = []

    def create_post(self, name: str, message: str) -> None:
        time = self.clock.get_date()
        post = Post(time, name, message)
        self.posts.append(post)

    def get_posts(self) -> list[Post]:
        return self.posts