class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print("Point:", (self.x, self.y))


point = Point(5, 10)
point.display()
