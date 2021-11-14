from abc import ABCMeta, abstractstaticmethod


class ICarBuilder(metaclass=ABCMeta):
    """The CarBuilder Interface"""

    @abstractstaticmethod
    def set_colour(self, value):
        """Set the car colour"""

    @abstractstaticmethod
    def set_engine(self, value):
        """Set the car engine"""

    @abstractstaticmethod
    def set_amount_of_doors(self, value):
        """Set amount of the doors"""

    @abstractstaticmethod
    def get_result(self):
        """Return the car"""
