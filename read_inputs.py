# get inputs for each program
import json

from Program1 import Square, Shape
from Program2 import swap_variables

path_to_file = './input_data/input_file.json'
with open(path_to_file, 'r') as rfile:
    data = json.load(rfile)

print(data)

# Input for Program1
length = data['program1']
aSquare = Square(length)
print(f" Output of aSquare.area() == {aSquare.area()}")

# Input for Program2
x, y = data['program2']['x'], data['program2']['y']
print(f" Before Swapping: x: {x}  y: {y}")
swap_variables(x, y)
