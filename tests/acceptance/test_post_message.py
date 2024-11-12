
class TestPostMessage:
    def test_user_can_post_message_to_timeline(self, capsys):
        twitter = Twitter()
        twitter.command("Alice -> I love the weather today")
        capture = capsys.readouterr()

        twitter.command("Alice")
        assert capture.out == "I love the weather today\n"
