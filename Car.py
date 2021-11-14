class Car:

    def __init__(self, colour="Gray", engine="R4", amount_of_doors=4):
        self.colour = colour
        self.engine = engine
        self.amount_of_doors = amount_of_doors

    def __str__(self):
        return f"This is {self.colour} car with a {self.engine} " \
         f"engine and with {self.amount_of_doors} doors"
