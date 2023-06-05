"""Counting the followers and followings of a user using oop"""


class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(75, "Ayaz")
user_2 = User(61, "Zahoor")

user_1.follow(user_2)
# user_2.follow(user_1)
# if we will un comment the object creation for 2nd user then both will have 1 follower and 1 following

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
