from unittest.mock import Mock
from social_network_kata.io import IO
from social_network_kata.twitter import Twitter


class TestTwitter:
    def test_can_start_and_stop(self, capsys):
        io = Mock(IO)
        
        twitter = Twitter(io)
        io.read.side_effect = ["exit"]
        twitter.run()
        
        capture, _ = capsys.readouterr()

        assert capture == "Bye!\n"