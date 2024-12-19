class Shape:
    def __init__(self):
        self.area = 0
        self.perimeter = 0
    def compute_area(self):
        pass
    def compute_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def compute_area(self):
        self.area = self.width * self.height
        return self.area

    def compute_perimeter(self):
        self.perimeter = 2*(self.width + self.height)
        return self.perimeter

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side  

    def compute_area(self):
        self.area = self.side * self.side
        return self.area

    def compute_perimeter(self):
        self.perimeter = 4 * self.side
        return self.perimeter