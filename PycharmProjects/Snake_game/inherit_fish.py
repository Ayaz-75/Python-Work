class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("inhale", "exhale")


class Fish(Animal):
    def __init__(self):
        super(Fish, self).__init__()

    def breathe(self):
        super(Fish, self).breathe()
        print("This upside was a super classes method")

    def swim(self):
        print("moving in water")


fish = Fish()
fish.breathe()
fish.swim()
print("Eyes =", fish.eyes)
