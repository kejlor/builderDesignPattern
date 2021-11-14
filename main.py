from BasicCarDirector import BasicCarDirector
from SportsCarDirector import SportsCarDirectory

if __name__ == "__main__":
    sports_car = SportsCarDirectory.construct()
    print(sports_car)
    basic_car = BasicCarDirector.construct()
    print(basic_car)
