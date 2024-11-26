
from unittest.mock import Mock
from social_network_kata.io import IO
from social_network_kata.post_repository import PostRepository
from social_network_kata.twitter import Twitter
from social_network_kata.clock import Clock
from social_network_kata.command_parser import CommandParser

class TestPostMessage:
    def test_user_can_post_message_to_timeline(self, capsys):
        io = Mock(IO)
        clock = Mock(Clock)
        post_repo = Mock(PostRepository)
        command_parser = Mock(CommandParser)
        command_parser.parse_command.side_effect = [
            ("POST",["Alice", "I love the weather today"]),
            ("WALL", ["Alice"])
        ]
        io.read.side_effect = ["Alice -> I love the weather today", "Alice", "exit"]
        clock.get_time_difference.side_effect = ["5 minutes"]
        twitter = Twitter(io, clock, post_repo, command_parser)
        
        twitter.run()
        
        capture, _ = capsys.readouterr()

        assert capture == """I love the weather today (5 minutes ago)\nBye!\n"""
