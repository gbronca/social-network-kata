from unittest.mock import Mock
from social_network_kata.clock import Clock
from social_network_kata.io import IO
from social_network_kata.twitter import Twitter
from social_network_kata.post_repository import PostRepository


class TestTwitter:
    def test_can_start_and_stop(self, capsys):
        io = Mock(IO)
        clock = Mock(Clock)
        post_repo = Mock(PostRepository)
        twitter = Twitter(io, clock, post_repo)
        
        io.read.side_effect = ["exit"]
        twitter.run()
        
        capture, _ = capsys.readouterr()

        assert capture == "Bye!\n"
        
    
    def test_can_post(self, capsys):
        io = Mock(IO)
        clock = Mock(Clock)
        
        post_repo = Mock(PostRepository)
        twitter = Twitter(io, clock, post_repo)
        
        twitter.create_post("Dave -> Hello")
        
        post_repo.create_post.assert_called_with("Dave -> Hello")