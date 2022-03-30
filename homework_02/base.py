from abc import ABC
from homework_02.exceptions import LowFuelError

class Vehicle(ABC):
    started = 1
    weight = 1
    fuel = 1
    fuel_consumption = 1
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo
    def start(self,started):
        if self.started != started:
            if self.fuel_consumption > 0:
                self.started = started
            else:
                raise LowFuelError
    def move(self, dist):
        if self.fuel_consumption * dist <= self.fuel:
            self.fuel -= self.fuel_consumption * dist
            return self.fuel
