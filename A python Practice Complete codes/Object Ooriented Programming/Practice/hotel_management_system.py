
class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(1, "Ayaz")
user2 = User(2, "Zahoor")

user1.follow(user2)
# user2.follow(user1)

print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)











# class Waiter:
#     def __init__(self, has, does):
#         self.has = has
#         self.does = does
#
#
# waiter = Waiter("Waiting skills", "Takes order from customer to chef")
# print("Waiter has: ", waiter.has)
# print("Waiter does: ", waiter.does)
#
#


# class Employee:
#     raise_amount = 1.04
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.mail = first + "." + last + "@company.com"
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
#
# class Developer(Employee):
#     raise_amount = 1.10
#
#
#
# dev1 = Developer("corey", "shafer", 50000)
# dev2 = Developer("Test", "User", 60000)
#
# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
