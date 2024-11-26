from unittest.mock import Mock
from social_network_kata.clock import Clock
from social_network_kata.io import IO
from social_network_kata.twitter import Twitter
from social_network_kata.post_repository import PostRepository
from social_network_kata.command_parser import CommandParser


class TestTwitter:
    def test_can_start_and_stop(self, capsys):
        io = Mock(IO)
        clock = Mock(Clock)
        post_repo = Mock(PostRepository)
        command_parser = Mock(CommandParser)
        twitter = Twitter(io, clock, post_repo, command_parser)
        
        io.read.side_effect = ["exit"]
        twitter.run()
        
        capture, _ = capsys.readouterr()

        assert capture == "Bye!\n"
        
    
    def test_can_post(self, capsys):
        io = Mock(IO)
        clock = Mock(Clock)
        io.read.side_effect = ["Dave -> Hello", "exit"]
        post_repo = Mock(PostRepository)
        command_parser = Mock(CommandParser)
        command_parser.parse_command.side_effect = [("POST", ["Dave", "Hello"])]
        twitter = Twitter(io, clock, post_repo, command_parser)

        twitter.run()
        
        post_repo.create_post.assert_called_with("Dave","Hello")

    
    def test_can_get_wall(self):
        io = Mock(IO)
        clock = Mock(Clock)
        io.read.side_effect = ["Dave", "exit"]
        post_repo = Mock(PostRepository)
        command_parser = Mock(CommandParser)
        command_parser.parse_command.side_effect = [("WALL", ["Dave"])]
        twitter = Twitter(io, clock, post_repo, command_parser)

        twitter.run()
        
        post_repo.get_wall.assert_called_with("Dave")