from Exceptions import *
from Animal import Animal
class Crab (Animal):
    def __init__(self, name, age, x, y, directionH):
        Animal.__init__(self, name, age, x, y, directionH)

    def __str__(self):
        pass

    def get_animal(self):
        pass

    def move(self):
        if self.directionH == 0:
            self.x -= 1
        else:
            self.x += 1