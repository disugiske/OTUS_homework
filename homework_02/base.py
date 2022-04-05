from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False
    weight = 1
    fuel = 1
    fuel_consumption = 10
    def __init__(self, weight = weight, fuel = fuel, fuel_consumption = fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    def start(self):
            if self.fuel > 0:
                self.started = True
                return self.started
            raise LowFuelError
    def move(self, dist):
        if self.fuel_consumption * dist <= self.fuel:
            self.fuel -= self.fuel_consumption * dist
            return self.fuel
        else:
            raise NotEnoughFuel
