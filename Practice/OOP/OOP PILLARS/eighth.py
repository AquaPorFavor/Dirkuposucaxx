from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Fan(Appliance):
    def turn_on(self):
        return "Fan is spinning."

    def turn_off(self):
        return "Fan is stopped."


class AirConditioner(Appliance):
    def turn_on(self):
        return "Air conditioner is cooling."

    def turn_off(self):
        return "Air conditioner is off."


class WashingMachine(Appliance):
    def turn_on(self):
        return "Washing machine is washing clothes."

    def turn_off(self):
        return "Washing machine is off."


devices = [Fan(), AirConditioner(), WashingMachine()]

for d in devices:
    print(d.turn_on())
    print(d.turn_off())
    print()