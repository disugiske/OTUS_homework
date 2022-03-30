from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, CargoOverload

class Vehicle(ABC):
    started = None
    weight = None
    fuel = None
    fuel_consumption = None
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    def start(self,started):
        if self.started != started:
            if self.fuel_consumption > 0:
                self.started = started
            else:
                raise LowFuelError
    def move(self):
        if self.fuel_consumption * self.weight <= self.fuel:
            self.fuel -= self.fuel_consumption * self.weight
