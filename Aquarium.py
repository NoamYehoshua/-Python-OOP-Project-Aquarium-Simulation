from Exceptions import *
from Scalar import Scalar
from Molly import Molly
from Ocypode import Ocypode
from Shrimp import Shrimp
import copy

class Aquarium():
    def __init__(self, aqua_width, aqua_height):
        if not isinstance(aqua_width, int):
            raise InvalidInputException
        if aqua_width < 40:
            raise TooSmallAquariumSize
        if not isinstance(aqua_height, int):
            raise InvalidInputException
        if aqua_height < 25:
            raise TooSmallAquariumSize
        self.aqua_width = aqua_width
        self.aqua_height = aqua_height
        self.step = 0
        self.animals = []
        board_list = []
        for i in range(self.aqua_height):
            small_list = []
            for index in range(self.aqua_width):
                if i == 2:
                    if index == 0:
                        small_list.append("|")
                    elif index == (self.aqua_width-1):
                        small_list.append("|")
                        board_list.append(small_list)
                    else:
                        small_list.append("~")
                elif i ==(self.aqua_height-1):
                    if index == 0:
                        small_list.append("\\")
                    elif index == (self.aqua_width-1):
                        small_list.append("/")
                        board_list.append(small_list)
                    else:
                        small_list.append("_")
                else:
                    if index == 0:
                        small_list.append("|")
                    elif index == (self.aqua_width-1):
                        small_list.append("|")
                        board_list.append(small_list)
                    else:
                        small_list.append(" ")
        self.board = board_list

    def __str__(self):
        animals_str = ""
        if len(self.animals)>0:
            for i in range(0 ,len(self.animals)):
                if i == (len(self.animals)-1):
                    animal = self.animals[i]
                    animals_str += animal.__str__()
                    return f"The aquarium, sized {self.aqua_height}/{self.aqua_width} and currently in step {self.step}, contains the following animals:\n{animals_str}\n"
                else:
                    animal = self.animals[i]
                    animals_str += animal.__str__() + "\n"
        return f"The aquarium, sized {self.aqua_height}/{self.aqua_width} and currently in step {self.step}, contains the following animals:\n"

    def __repr__(self):
        no_punctuation = ""
        board_lst = self.board
        for i in range(0,len(board_lst)):
            for index in range(0,len(board_lst[0])):
                if index != (len(board_lst[0])-1):
                    no_punctuation += board_lst[i][index] + " "
                else:
                    if i == (len(board_lst)-1):
                        no_punctuation += board_lst[i][index] + "\n"
                    else:
                        no_punctuation += board_lst[i][index] + "\n"
        return no_punctuation

    def feed_all(self):
        animals_list = self.animals
        for animal in animals_list:
            animal.add_food(10)


    def __insert_animal_to_board (self, animal):
        y_location = animal.y
        get_ani = animal.get_animal()
        board_list = self.board
        for i in range(0,len(get_ani)):
            x_location = animal.x
            if i!=0:
                y_location += 1
            for index in range(0,len(get_ani[0])):
                if x_location + 1 == (animal.x + len(get_ani[0])):
                    if board_list[y_location][x_location] != "*":
                        board_list[y_location][x_location] = get_ani[i][index]
                else:
                    if board_list[y_location][x_location] != "*":
                        board_list[y_location][x_location] = get_ani[i][index]
                    x_location += 1
        self.board = board_list

    def __delete_animal_from_board(self, animal):
        y_location = animal.y
        get_ani = animal.get_animal()
        board_list = self.board
        for i in range(0,len(get_ani)):
            x_location = animal.x
            if i!=0:
                y_location += 1
            for index in range(0,len(get_ani[0])):
                if x_location + 1 == (animal.x + len(get_ani[0])):
                    board_list[y_location][x_location] = " "
                else:
                    board_list[y_location][x_location] = " "
                    x_location += 1
        self.board = board_list

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if not isinstance(animaltype, str):
            raise InvalidInputException
        if animaltype not in ["ocypode", "molly", "scalar", "shrimp"]:
            raise InvalidAnimalType(animaltype)
        if x <= 0:
            x = 1
        if y <= 2:
            y = 3
        if animaltype == "molly":
            new_animal = Molly(name, age, x, y, directionH, directionV)
        elif animaltype == "scalar":
            new_animal = Scalar(name, age, x, y, directionH, directionV)
        elif animaltype == "ocypode":
            new_animal = Ocypode(name, age, x, y, directionH)
        else:
            new_animal = Shrimp(name, age, x, y, directionH)
        get_animal_list = new_animal.get_animal()
        if new_animal.x > (self.aqua_width-1-1-len(get_animal_list[0])+1):
            new_animal.x = (self.aqua_width-1-1-len(get_animal_list[0])+1)
        if animaltype == "scalar" or animaltype == "molly":
            if new_animal.y > (self.aqua_height-5-1-len(get_animal_list)+1):
                new_animal.y = (self.aqua_height-5-1-len(get_animal_list)+1)
        else:
            if new_animal.y != (self.aqua_height-1-len(get_animal_list)):
                new_animal.y = (self.aqua_height-1-len(get_animal_list))
        min_y = new_animal.y
        max_y = new_animal.y+len(get_animal_list)-1
        min_x = new_animal.x
        max_x = new_animal.x+len(get_animal_list[0])-1
        for ani in self.animals:
            if ani is not new_animal:
                ani_list = ani.get_animal()
                ani_min_y = ani.y
                ani_max_y = ani.y+len(ani_list)-1
                ani_min_x = ani.x
                ani_max_x = ani.x+len(ani_list[0])-1
                if (min_y <= ani_min_y <= max_y) or (min_y <= ani_max_y <= max_y):
                    if (min_x <= ani_min_x <= max_x) or (min_x <= ani_max_x <= max_x):
                        raise NotAvailablePlace
        self.animals.append(new_animal)
        self.__insert_animal_to_board(new_animal)

    def __kill_animal(self,animal):
        if animal.starvation() or animal.die():
            self.__delete_animal_from_board(animal)
            self.animals.remove(animal)

    def next_step(self):
        self.step += 1
        animals_list = copy.copy(self.animals)
        for animal in animals_list:
            self.__kill_animal(animal)
        for animal in animals_list:
            self.__delete_animal_from_board(animal)
        animals_list = copy.copy(self.animals)
        for animal in animals_list:
            animal_lst = animal.get_animal()
            if animal.x == 1 and animal.directionH == 0:
                animal.directionH = 1
            elif (animal.x+len(animal_lst[0])-1) == (self.aqua_width-2) and animal.directionH == 1:
                animal.directionH = 0
        for animal in animals_list:
             animal_lst = animal.get_animal()
             if isinstance(animal,Molly) or isinstance(animal,Scalar):
                 if animal.y == 3 and animal.directionV == 1:
                     animal.directionV = 0
                 elif ((animal.y+len(animal_lst)-1) == (self.aqua_height-1-5)) and animal.directionV == 0:
                    animal.directionV = 1
        for animal in animals_list:
            if isinstance(animal, Ocypode) or isinstance(animal, Shrimp):
                animal_lst = animal.get_animal()
                for ani in animals_list:
                    if isinstance(ani, Ocypode) or isinstance(ani, Shrimp) and ani is not animal:
                        ani_list = ani.get_animal()
                        if (ani.x+len(ani_list[0])-1 == animal.x-1) or (ani.x+len(ani_list[0])-1 == animal.x-2):
                            if ani.directionH == 1 and animal.directionH == 0:
                                ani.directionH = 0
                                animal.directionH = 1
                        elif ((animal.x+len(animal_lst[0])-1) == ani.x-1) or ((animal.x+len(animal_lst[0])-1) == ani.x-2):
                            if ani.directionH == 0 and animal.directionH == 1:
                                ani.directionH = 1
                                animal.directionH = 0
        for animal in animals_list:
            animal.move()
        if self.step % 10 == 0:
            for animal in animals_list:
                animal.dec_food()
                animal.inc_age()
        for animal in animals_list:
            self.__insert_animal_to_board(animal)

    def several_steps(self, steps):
        for i in range(0,steps):
            self.next_step()
