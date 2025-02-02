from math import sqrt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates:", self.x, self.y)
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self,otherpoint):
        distance = sqrt(((self.x - otherpoint.x) ** 2) + ((self.y - otherpoint.y) ** 2))
        print(f"Distance between ({self.x}, {self.y}) and ({otherpoint.x}, {otherpoint.y}): {distance}")

coordinates1 = Point(3,4)
coordinates1.show()
coordinates1.move(1,3)
coordinates1.show()

coordinates2 = Point(3,4)
coordinates2.dist(coordinates1)