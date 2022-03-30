from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = None
    max_cargo = None
    def load_cargo(self, cargo):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
            return self.cargo
        else:
            raise CargoOverload
