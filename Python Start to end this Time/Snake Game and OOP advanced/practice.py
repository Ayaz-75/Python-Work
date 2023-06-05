class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breath(self):
        print("Breathing: inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Fish breaths Under water")

    def swim(self):
        print("Swimming: Moving in water")


fi = Fish()
print("Number of eyes: ", fi.num_of_eyes)
fi.swim()
fi.breath()
