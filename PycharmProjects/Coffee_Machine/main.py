class User:
    def __init__(self, user_name, user_id):
        self.name = user_name
        self.id = user_id
        self.following = 0
        self.followers = 0

    def follow(self, user):
        self.followers += 1
        self.following += 1


user_1 = User("Ayaz", 75)
user_2 = User("Anwar", 76)


user_1.follow(user_2)
user_2.follow(user_1)
