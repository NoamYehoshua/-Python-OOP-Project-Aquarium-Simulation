from Exceptions import *
from Crab import Crab
class Ocypode (Crab):
    def __int__(self, name, age, x, y, directionH):
        Crab.__init__(self, name, age, x, y, directionH)
        self.width = 7
        self.height = 4

    def __str__(self):
        return f"The ocypode {self.name} is {self.age} years old and has {self.food} food."

    def get_animal(self):
        return [[" ", "*", " ", " ", " ", "*", " "],
           [" ", " ", "*", "*", "*", " ", " "],
           ["*", "*", "*", "*", "*", "*", "*"],
           ["*", " ", " ", " ", " ", " ", "*"]]