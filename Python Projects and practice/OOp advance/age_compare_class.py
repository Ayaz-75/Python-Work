# ----------- Program to write a method which compares the age of two persons -----------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def comp(self, other):
        if other.age > self.age:
            print(f"{other} is younger than {self.name}")
