class Animal:
    def __init__(self, name):
        self.name = name
        
    
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"


d1 = Dog("Buddy")
c1 = Cat("Luna")
d2 = Dog("Max")


for x in (d1, c1, d2):
    print(f"{x.name} says {x.speak()}")


