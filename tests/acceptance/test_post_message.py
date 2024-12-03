
from unittest.mock import Mock

from social_network_kata.command_parser import CommandParser
from social_network_kata.clock import Clock
from social_network_kata.io import IO
from social_network_kata.post import Post
from social_network_kata.post_repository import PostRepository
from social_network_kata.twitter import Twitter


from datetime import datetime

class TestPostMessage:
    def test_user_can_post_message_to_timeline(self, capsys):
        io = Mock(IO)
        clock = Mock(Clock)
        post_repo = Mock(PostRepository)
        post_repo.get_posts_by_user.return_value = [Post(datetime.now(), "Alice", "I love the weather today")]
        command_parser = Mock(CommandParser)
        command_parser.parse_command.side_effect = [
            ("POST",["Alice", "I love the weather today"]),
            ("READ", ["Alice"])
        ]
        io.read.side_effect = ["Alice -> I love the weather today", "Alice", "exit"]
        post_time = datetime(2024, 12, 3, 10, 45)
        read_time = datetime(2024, 12, 3, 10, 50)
        clock.get_date.side_effect = [post_time, read_time]
        clock.get_time_difference.return_value = read_time - post_time
        twitter = Twitter(io, clock, post_repo, command_parser)
        
        twitter.run()
        
        capture, _ = capsys.readouterr()

        assert capture == """I love the weather today (5 minutes ago)\nBye!\n"""
