from homework_02.base import Vehicle
from homework_02.engine import Engine





class Car(Vehicle):
    engine=Engine()
    @property
    def set_engine(self):
        return self.engine
    @set_engine.setter
    def set_engine(self, engine):
        self.engine = engine
