from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo=50
    def load_cargo(self, cargo):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
            return self.cargo
        else:
            raise CargoOverload
    def remove_all_cargo(self):
        cargo = 0
        return cargo
