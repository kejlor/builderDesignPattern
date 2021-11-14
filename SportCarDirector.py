from CarBuilder import CarBuilder


class SportCarDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> CarBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: CarBuilder) -> None:
        self._builder = builder

    def build_sport_car(self) -> None:
        self.builder.set_amount_of_doors(3)
        self.builder.set_colour("Black")
        self.builder.set_engine("R6")

    def build_super_sport_car(self) -> None:
        self.builder.set_amount_of_doors(2)
        self.builder.set_colour("Red")
        self.builder.set_engine("quad-turbo, 8.0-liter W-16")
