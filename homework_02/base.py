from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False
    weight = 1
    fuel = 0
    fuel_consumption = 20
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo
    def start(self, started):
        if started == False:
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
