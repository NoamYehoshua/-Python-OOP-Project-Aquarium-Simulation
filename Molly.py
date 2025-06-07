from Exceptions import *
from Fish import Fish
from Animal import Animal
class Molly (Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        Fish.__init__(self, name, age, x, y, directionH, directionV)
        self.width = 8
        self.height = 3

    def __str__(self):
        return f"The molly {self.name} is {self.age} years old and has {self.food} food."

    def get_animal(self):
        if self.directionH == 0:
            return [[" ", "*", "*", "*", "*", " ", " ", "*"],
              ["*", "*", "*", "*", "*", "*", "*", "*"],
              [" ", "*", "*", "*", "*", " ", " ", "*"]]
        else:
            return [["*", " ", " ", "*", "*", "*", "*", " "],
               ["*", "*", "*", "*", "*", "*", "*", "*"],
               ["*", " ", " ", "*", "*", "*", "*", " "]]