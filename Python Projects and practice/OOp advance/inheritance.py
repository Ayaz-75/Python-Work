class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print(f"Eating: As it is Property of every animal")


class Mammal(Animal):
    def walk(self):
        print(f"Property of mammals: Walking")


class Fish(Animal):
    def swim(self):
        print(f"Property of Fishes: swim")


m = Mammal()
f = Fish()
print(f"age of Mammal: {m.age + 9}")
m.walk()
m.eat()


print(f"age of fish: {f.age + 1}")
f.swim()
f.eat()
