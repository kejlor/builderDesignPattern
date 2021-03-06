from CarBuilder import CarBuilder


class BasicCarDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> CarBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: CarBuilder) -> None:
        self._builder = builder

    def build_minimal_car(self) -> None:
        self.builder.set_amount_of_doors(4)
        self.builder.set_colour("Gray")
        self.builder.set_engine("R4")

    def build_fast_basic_car(self) -> None:
        self.builder.set_amount_of_doors(3)
        self.builder.set_colour("Black")
        self.builder.set_engine("R6")
