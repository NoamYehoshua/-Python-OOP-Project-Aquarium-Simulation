from Exceptions import *
from Crab import Crab
class Shrimp (Crab):
    def __int__(self, name, age, x, y, directionH):
        Crab.__init__(self, name, age, x, y, directionH)
        self.width = 7
        self.height = 3

    def __str__(self):
        return f"The shrimp {self.name} is {self.age} years old and has {self.food} food."

    def get_animal(self):
        if self.directionH == 0:
            return [["*", " ", "*", " ", " ", " ", " "],
               [" ", "*", "*", "*", "*", "*", "*"],
               [" ", " ", "*", " ", "*", " ", " "]]
        else:
            return [[" ", " ", " ", " ", "*", " ", "*"],
                ["*", "*", "*", "*", "*", "*", " "],
                [" ", " ", "*", " ", "*", " ", " "]]