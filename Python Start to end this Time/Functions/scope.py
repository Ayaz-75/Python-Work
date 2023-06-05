enemies = 1


def increase_enemies():
    print(f'first: {enemies}')
    return enemies + 2


enemies = increase_enemies()
print(f'second: {enemies}')
