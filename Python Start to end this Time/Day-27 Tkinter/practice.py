def add_nums(*args):
    total = 0
    for i in args:
        total += i

    return total


# print(add_nums(2, 3, 4, 5))


def calculate(n, **kwargs):
    # print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    # print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw['make']
        self.make = kw.get('model')
        # self.model = kw['model']
        self.model = kw.get('model')


my_car = Car(make='Lamborghini')

print(my_car.model)
