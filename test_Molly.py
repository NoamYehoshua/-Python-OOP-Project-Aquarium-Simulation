from unittest import TestCase
from Animal import Animal
from Fish import Fish
from Molly import Molly
from Exceptions import *

class test_Molly(TestCase):
    def test_init(self):
        with self.assertRaises(InvalidInputException):
            Fish(55, 5, 1, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish([], 5, 1, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish({}, 5, 1, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", -2, 1, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 170, 1, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 120, 1, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 0, 1, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", "ddg", 1, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, 0, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, -1, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, "df", 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, 1.1, 1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, 1, 0, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, 1, -1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, 1, "df", 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, 1, 1.1, 0,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, 1, 1, 5,1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, 1, 1, "gf",1)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, 1, 1, 0, 5)
        with self.assertRaises(InvalidInputException):
            Fish("molly", 5, 1, 1, 0,"gf")
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.assertEqual("molly1",self.molly.name,msg = 'Error in init - name')
        self.assertEqual(12, self.molly.age, msg='Error in init - age')
        self.assertEqual(10, self.molly.x, msg='Error in init - x')
        self.assertEqual(10, self.molly.y, msg='Error in init - y')
        self.assertEqual(1, self.molly.directionH, msg='Error in init - directionH')
        self.assertEqual(0, self.molly.directionV, msg='Error in init - directionV')
        self.assertEqual(10, self.molly.food, msg='Error in init - food')
        self.assertEqual(3, self.molly.height, msg='Error in init - height')
        self.assertEqual(8, self.molly.width, msg='Error in init - width')

    def test_str(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.assertEqual(f"The molly {self.molly.name} is {self.molly.age} years old and has {self.molly.food} food.", self.molly.__str__(), msg='Error in str')

    def test_get_animal(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly1 = Molly("molly2", 30, 2, 2, 0, 0)
        self.assertEqual([["*", " ", " ", "*", "*", "*", "*", " "],
               ["*", "*", "*", "*", "*", "*", "*", "*"],
               ["*", " ", " ", "*", "*", "*", "*", " "]], self.molly.get_animal(), msg='Error in get_animal')
        self.assertEqual([[" ", "*", "*", "*", "*", " ", " ", "*"],
              ["*", "*", "*", "*", "*", "*", "*", "*"],
              [" ", "*", "*", "*", "*", " ", " ", "*"]], self.molly1.get_animal(), msg='Error in get_animal')

    def test_move(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly1 = Molly("molly2", 30, 4, 4, 0, 0)
        self.molly2 = Molly("molly3", 30, 4, 4, 0, 1)
        self.molly3 = Molly("molly4", 30, 4, 4, 1, 1)
        self.molly.move()
        self.molly1.move()
        self.molly2.move()
        self.molly3.move()
        self.assertEqual((11,11), self.molly.get_position(), msg='Error in move')
        self.assertEqual((3, 5), self.molly1.get_position(), msg='Error in move')
        self.assertEqual((3, 3), self.molly2.get_position(), msg='Error in move')
        self.assertEqual((5, 3), self.molly3.get_position(), msg='Error in move')

    def test_get_directionV(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.assertEqual(0, self.molly.get_directionV(), msg='Error in get_directionV')



    def test_set_directionV(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly.set_directionV(0)
        self.molly1 = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly1.set_directionV(1)
        self.assertEqual(0, self.molly.get_directionV(), msg='Error in set_directionV')
        self.assertEqual(1, self.molly1.get_directionV(), msg='Error in set_directionV')


    def test_get_position(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.assertEqual((10,10), self.molly.get_position(), msg='Error in get_positinion')

    def test_get_directionH(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.assertEqual(1, self.molly.get_directionH(), msg='Error in get_directionH')

    def test_get_size(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.assertEqual((8,3), self.molly.get_size(), msg='Error in get_sizeV')

    def test_dec_food(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly.dec_food()
        self.assertEqual(9, self.molly.food, msg='Error in dec_food')

    def test_add_food(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly1 = Molly("molly2", 12, 10, 10, 1, 0)
        self.molly.add_food(10)
        self.molly1.add_food(0)
        self.assertEqual(20, self.molly.food, msg='Error in add_food')
        self.assertEqual(10, self.molly1.food, msg='Error in add_food')

    def test_inc_age(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly.inc_age()
        self.assertEqual(13, self.molly.age, msg='Error in inc_age')


    def test_set_directionH(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly.set_directionH(0)
        self.molly1 = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly1.set_directionH(1)
        self.assertEqual(0, self.molly.get_directionH(), msg='Error in set_directionH')
        self.assertEqual(1, self.molly1.get_directionH(), msg='Error in set_directionH')

    def test_starvation(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly1 = Molly("molly1", 12, 10, 10, 1, 0)
        self.molly.food = 0
        self.assertTrue(self.molly.starvation(), msg='Error in starvation')
        self.assertFalse(self.molly1.starvation(), msg='Error in starvation')

    def test_die(self):
        self.molly = Molly("molly1", 119, 10, 10, 1, 0)
        self.molly.inc_age()
        self.molly1 = Molly("molly1", 12, 10, 10, 1, 0)
        self.assertTrue(self.molly.die(), msg='Error in die')
        self.assertFalse(self.molly1.die(), msg='Error in die')

    def test_repr(self):
        self.molly = Molly("molly1", 12, 10, 10, 1, 0)
        self.assertEqual("*     * * * *  \n* * * * * * * *\n*     * * * *  ", self.molly.__repr__(), msg='Error in repr')
