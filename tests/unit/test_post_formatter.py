from unittest.mock import Mock
from social_network_kata.clock import Clock
from social_network_kata.post import Post
from social_network_kata.post_formatter import PostFormatter
from social_network_kata.post_repository import PostRepository

from datetime import datetime

import pytest


class TestPostFormatter:
    @pytest.mark.parametrize("input, output", [("Ned", "Winter is coming"), ("Frink", "Zoinks"), ("ZoidBerg", "Why not Zoidberg?")])
    def test_can_format_posts(self, input, output):
        clock = Mock(Clock)
        clock.get_date.return_value = datetime.now()
        post_time = datetime(2024, 12, 3, 10, 45)
        read_time = datetime(2024, 12, 3, 10, 50)
        clock.get_date.side_effect = [post_time, read_time]
        clock.get_time_difference.return_value = read_time - post_time

        posts = [
            Post(post_time, input, output),
        ]
        post_formatter = (PostFormatter(clock=clock))
        formatted_posts = post_formatter.format_posts(posts=posts)


        assert formatted_posts == [
            f"{output} (5 minutes ago)"
        ]

    def test_format_time(self):
        clock = Mock(Clock)
        read_time = datetime(2024, 12, 3, 10, 50)
        post_time = datetime(2024, 12, 3, 10, 45)
        post_formatter = PostFormatter(clock)
        clock.get_time_difference.return_value = (read_time - post_time)

        formatted_time = post_formatter.format_time(read_time, post_time)

        assert formatted_time == "5 minutes"
