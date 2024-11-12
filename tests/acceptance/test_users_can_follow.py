"following: <user name> follows <another user>"
class TestUsersCanFollow:

    def test_user_can_follow(self):
        twitter = Twitter()
        user_1 = User("bob")
        user_2 = User("alice")

        twitter.follow(user_1, user_2)
