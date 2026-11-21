from abc import ABC, abstractmethod

class Person(ABC):
    
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def special_skill(self):
        pass
    
    def __init__(self, name, hp=100):
        self.name = name
        self.__hp = hp
    
    def take_damage(self, damage):
        self.__hp -= damage
    
    def heal(self, amount):
        self.__hp += amount

    def get_hp(self):
        return self.__hp

class Warrior(Person):
    def attack(self):
        return f"{self.name} swings a sword!"

    def special_skill(self):
        return f"{self.name} uses Berserk Slash!"


class Mage(Person):
    def attack(self):
        return f"{self.name} casts a fireball!"

    def special_skill(self):
        return f"{self.name} uses Arcane Storm!"


class Archer(Person):
    def attack(self):
        return f"{self.name} shoots an arrow!"

    def special_skill(self):
        return f"{self.name} uses Rain of Arrows!"

team = [
    Warrior("Leon"),
    Mage("Luna"),
    Archer("Kai")
]

for c in team:
    print(c.attack())
    print(c.special_skill())
    print("HP:", c.get_hp())
    print()


team[0].take_damage(30)
print(f"{team[0].name} HP after damage:", team[0].get_hp())

team[0].heal(20)
print(f"{team[0].name} HP after heal:", team[0].get_hp())

