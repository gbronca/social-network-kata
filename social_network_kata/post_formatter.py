from .clock import Clock
from .post import Post

class PostFormatter:
    def __init__(self, clock: Clock) -> None:
        self.clock = clock


    def format_posts(self, posts: list[Post]) -> [str]:
        time_now = self.clock.get_date()
        formatted_posts = []
        for post in posts:
            formatted_time = self.format_time(time_now, post.time)

            formatted_posts.append(
                f"{post.message} ({formatted_time} ago)"
            )

        return formatted_posts

    @staticmethod
    def format_time(read_time, post_time):
        time_delta = read_time - post_time
        total_seconds = time_delta.total_seconds()
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours:
            return f"{int(hours)} hours"

        return f"{int(minutes)} minutes"
