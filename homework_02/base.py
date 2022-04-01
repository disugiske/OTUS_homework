from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = None
    weight = None
    fuel = None
    fuel_consumption = None
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    def start(self, started):
        if not started:
            if self.fuel > 0:
                started = True
                return started
            else:
                raise LowFuelError
    def move(self, dist):
        if self.fuel_consumption * dist <= self.fuel:
            self.fuel -= self.fuel_consumption * dist
            return self.fuel
        else:
            raise NotEnoughFuel
