from Program1 import Square, Shape
from Program2 import swap_variables

aSquare = Square(16)

print(f" Output of aSquare.area() == {aSquare.area()}")

aShape = Shape()
print(f" Output of aShape.area() == {aShape.area()}")

x, y = 50, 60
print(f" Before Swapping: x: {x}  y: {y}")
swap_variables(x, y)
