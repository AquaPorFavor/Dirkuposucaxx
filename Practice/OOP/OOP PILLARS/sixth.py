class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        pass

class car(Vehicle):
    def move(self):
        return "drives on the road"

class Motorcycle(Vehicle):
    def move(self):
        return "speeds through traffic"

class Bicycle(Vehicle):
    def move(self):
        return "is pedaling"

c1 = car("Toyota", 100)
m1 = Motorcycle("Yamaha", 120)
b1 = Bicycle("Giant", 25)

print(f"{c1.brand} car {c1.move()}")
print(f"{m1.brand} car {m1.move()}")
print(f"{b1.brand} car {b1.move()}")