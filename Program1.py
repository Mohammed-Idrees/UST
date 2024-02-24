class Shape:

    def area(self):
        # Area of Shape is 0 by default
        return 0


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):

        return self.length ** 2
