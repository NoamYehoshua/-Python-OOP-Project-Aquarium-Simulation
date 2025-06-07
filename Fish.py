from Exceptions import *
from Animal import Animal
class Fish (Animal):
    def __init__(self, name, age, x, y, directionH, directionV):
        Animal.__init__(self, name, age, x, y, directionH)
        if not isinstance(directionV, int):
            raise InvalidInputException
        if directionV != 0 and directionV != 1:
            raise InvalidInputException

        self.directionV = directionV
        self.directionH = directionH

    def __str__(self):
        pass

    def get_animal(self):
        pass

    def move(self):
        if self.directionH == 0:
            if self.directionV == 0:
                self.x -= 1
                self.y += 1
            else:
                self.x -= 1
                self.y -= 1
        else:
            if self.directionV == 0:
                self.x += 1
                self.y += 1
            else:
                self.x += 1
                self.y -= 1

    def get_directionV(self):
        return self.directionV

    def set_directionV(self, directionV):
        self.directionV = directionV
