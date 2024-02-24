import multiprocessing
from Program1 import Square, Shape
from Program2 import swap_variables


def program1():
    aSquare = Square(16)
    print(f" Output of aSquare.area() == {aSquare.area()}")

    aShape = Shape()
    print(f" Output of aShape.area() == {aShape.area()}")


def program2():
    x, y = 50, 60
    print(f" Before Swapping: x: {x}  y: {y}")
    swap_variables(x, y)


if __name__ == "__main__":
    t1 = multiprocessing.Process(target=program1)
    t2 = multiprocessing.Process(target=program2)

    t1.start()
    t2.start()
