class Vehicle:
    default_color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


'''class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


print()
bus = Bus("School bus", 300, 30)
print(f"Color: {bus.default_color}, Name of bus: {bus.name}, Maximum Speed of Bus:{bus.max_speed}, Mileage: {bus.mileage}, "
      f"Seats:{bus.seating_capacity(50)}")
car = Car("Civic", 250, 5)
print(f"Color: {car.default_color}, Name of car: {car.name}, Maximum Speed of car:{car.max_speed}, Mileage: {car.mileage}, "
      f"Seats:{car.seating_capacity(50)}")'''
