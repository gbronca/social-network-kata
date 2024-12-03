from unittest.mock import Mock
from social_network_kata.clock import Clock
from social_network_kata.post_repository import PostRepository
from social_network_kata.post import Post
from datetime import datetime

import pytest


class TestPostRepository:
    def test_can_create_post(self):
        clock = Mock(Clock)
        clock.get_date.return_value = datetime.now()
        post_repo = PostRepository(clock)
        name = "Bob"
        message = "Good bye"
        
        post_repo.create_post(name,message)

        assert post_repo.get_posts() == [Post(clock.get_date.return_value, name, message)]

    @pytest.mark.parametrize("input, output", [("Bob", "Good"), ("McBob", "bye"), ("David", "I am a human")])
    def test_can_get_posts_by_user(self, input, output):
        clock = Mock(Clock)
        clock.get_date.return_value = datetime.now()
        post_repo = PostRepository(clock)
        
        post_repo.create_post(input, output)

        assert post_repo.get_posts_by_user(input) == [Post(clock.get_date.return_value, input, output)]
