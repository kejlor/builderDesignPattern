class Car:

    def __init__(self, colour="Gray", engine="R4", amount_of_doors=4):
        self.colour = colour
        self.engine = engine
        self.amount_of_doors = amount_of_doors

    def __str__(self):
        return f"This is a car of colour: {self.colour} with an {self.engine} " \
         "engine and with {self.amount_of_doors} doors"
