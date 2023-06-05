# enemies = 1
#
#
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"new enemy inside function is {enemies} ")
#
#
# print(f"old enemy outside function is {enemies}")
# increase_enemies()
#
EASY = 10
HARD = 5


def set_l():
    level = input("Enter diff: ")
    if level == 'easy':
        return EASY
    else:
        return HARD


attempts = set_l()

