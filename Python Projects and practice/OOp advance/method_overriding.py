class Animal:
    def __init__(self):
        print(f"Animal class constructor")
        self.age = 10

    def eat(self):
        print("eating")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print(f"Mammal class constructor")
        self.weight = 20


# a = Animal()
m = Mammal()
print(m.age)
print(m.weight)
