from CarBuilder import CarBuilder


class SportsCarDirector:
    @staticmethod
    def construct():
        constructed_car = CarBuilder()
        constructed_car.set_colour("Black")
        constructed_car.set_engine("V6")
        constructed_car.set_amount_of_doors(3)
        return constructed_car.get_result()
