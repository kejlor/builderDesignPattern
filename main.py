from SportCarDirector import SportCarDirector
from BasicCarDirector import BasicCarDirector
from CarBuilder import CarBuilder

if __name__ == "__main__":
    basic_director = BasicCarDirector()
    sport_director = SportCarDirector()
    builder = CarBuilder()
    basic_director.builder = builder
    sport_director.builder = builder
    basic_director.build_minimal_car()
    print(builder.car.__str__())
    print("\n")
    basic_director.build_fast_basic_car()
    print(builder.car.__str__())
    print("\n")
    builder.set_amount_of_doors(5)
    builder.set_engine("W6")
    builder.set_colour("Yellow")
    print(builder.car.__str__())
    print("\n")
    sport_director.build_super_sport_car()
    print(builder.car.__str__())
