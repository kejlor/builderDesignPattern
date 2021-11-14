from Car import Car
from ICarBuilder import ICarBuilder


class CarBuilder(ICarBuilder):

    def __init__(self):
        self.reset()

    def set_colour(self, value):
        self.car.colour = value

    def set_engine(self, value):
        self.car.engine = value

    def set_amount_of_doors(self, value):
        self.car.amount_of_doors = value

    def get_result(self):
        return self.car

    def car(self) -> Car:
        car = self.car
        self.reset()
        return car

    def reset(self) -> None:
        self.car = Car()
