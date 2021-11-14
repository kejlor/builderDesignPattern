from BasicCarDirector import BasicCarDirector
from SportsCarDirector import SportsCarDirector

if __name__ == "__main__":
    sports_car = SportsCarDirector.construct()
    print(sports_car)
    basic_car = BasicCarDirector.construct()
    print(basic_car)
