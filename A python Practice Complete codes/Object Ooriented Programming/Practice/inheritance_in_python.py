
class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breadth(self):
        print("inhale and exhale")



class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Fishes can swim")

    def breadth(self):
        super().breadth()
        print("doing this underwater")

fish = Fish()
# fish.swim()
fish.breadth()


