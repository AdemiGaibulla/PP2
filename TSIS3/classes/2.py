class Shape():
    def __init__(self):
        pass
    def area(self):
        print("Area of the shape:",0)

class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length = length

    def area(self):
        print("Area of the square:",self.length**2)
    
shape = Shape()
shape.area()
square = Square(2)
square.area()
