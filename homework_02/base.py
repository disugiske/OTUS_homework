from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False
    weight = 1
    fuel = 0
    fuel_consumption = 1
    max_cargo = 1
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    def start(self, started):
        if started is False:
            if self.fuel_consumption > 0:
                return started is True
            else:
                raise LowFuelError
    def move(self, dist):
        if self.fuel_consumption * dist <= self.fuel:
            self.fuel -= self.fuel_consumption * dist
            return self.fuel
        else:
            raise NotEnoughFuel
