
from unittest.mock import Mock
from social_network_kata.io import IO
from social_network_kata.twitter import Twitter

class TestPostMessage:
    def test_user_can_post_message_to_timeline(self, capsys):
        io = Mock(IO)
        io.read.side_effect = ["Alice -> I love the weather today", "Alice"]
        twitter = Twitter(io)
        
        twitter.run()
        
        capture = capsys

        assert capture.out == "I love the weather today\n"
