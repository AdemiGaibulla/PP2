class Shape():
    def __init__(self):
        pass
    def area(self):
        print("Area of the shape:",0)

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        print("Area of the square:",self.length**2)

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self):
        print("Area of the rectangle:",self.width*self.length)

rectangle = Rectangle(2,3)
rectangle.area()