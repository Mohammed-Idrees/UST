import unittest
from Program1 import Shape, Square
from Program2 import swap_variables


class TestPrograms(unittest.TestCase):

    def test_program1_tc_1(self):
        aSquare = Square(10)
        assert 100 == aSquare.area()

    def test_program1_tc_2(self):
        aShape = Shape()
        assert 0 == aShape.area()

    def test_program1_tc_3(self):
        aSqaure = Square(20)
        assert 400 == aSqaure.area()

    def test_program2_tc_1(self):
        x, y = 100, 200
        print(f" Before Swapping: x: {x}  y: {y}")
        swap_variables(x, y)

    def test_program2_tc_2(self):
        x, y = 40, 50
        print(f" Before Swapping: x: {x}  y: {y}")
        swap_variables(x, y)


if __name__ == '__main__':
    unittest.main()
