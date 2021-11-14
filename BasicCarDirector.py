from CarBuilder import CarBuilder


class BasicCarDirector:
    @staticmethod
    def construct():
        constructed_car = CarBuilder()
        constructed_car.set_colour("Gray")
        constructed_car.set_engine("R4")
        constructed_car.set_amount_of_doors(5)
        return constructed_car.get_result()
