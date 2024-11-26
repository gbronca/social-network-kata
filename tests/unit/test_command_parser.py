from unittest.mock import Mock
from social_network_kata.command_parser import CommandParser

class TestCommandParser:

    def test_can_parse_post(self):
        parser = CommandParser()
        command = "Dave -> Hello"

        result = parser.parse_command(command)

        assert result == ("POST", ["Dave", "Hello"])