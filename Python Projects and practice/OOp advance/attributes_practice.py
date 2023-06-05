"""Attributes and methods practice in oop"""

'''class Car:
    def __init__(self, seats):
        self.seats = seats


my_car = Car(5)
print(f"Number of seats in car is: {my_car.seats}")'''


def follow():
    user_1.follower += 1
    user_2.following += 1


class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.follower = 0
        self.following = 0


user_1 = User("001", "Ayaz Lakho")
user_2 = User("002", "Zahoor Gabole")

print(f"1st user: {user_1.user_name}")
print(f"2nd user: {user_2.user_name}")

follow()

print(f"{user_1.follower}")
print(f"{user_1.following}")
print(f"{user_2.follower}")
print(f"{user_2.following}")
