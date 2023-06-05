""""Multi level inheritance this uses the properties of both classes"""


class Flyer:
    def fly(self):
        print("can fly")


class Swimmer:
    def swim(self):
        print("can swim")


class Duck(Flyer, Swimmer):
    pass


duck = Duck()
print("Duck:")
duck.fly()
duck.swim()
