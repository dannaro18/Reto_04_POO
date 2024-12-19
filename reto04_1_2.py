import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.compute_length()

    def compute_length(self):
        return self.start_point.compute_distance(self.end_point)

class Shape:
    def __init__(self):
        self.vertices = []  
        self.edges = []     
        self.inner_angles = []  
        self.is_regular = False

    def compute_area(self):
        pass
    def compute_perimeter(self):
        pass
    def compute_inner_angles(self):
        pass

class Triangle(Shape):
    def __init__(self, point1, point2, point3):
        super().__init__()
        self.vertices = [point1, point2, point3]
        self.edges = [Line(point1, point2), Line(point2, point3), Line(point3, point1)]
    
    def compute_area(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        s = (a+b+c)/2  
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area

    def compute_perimeter(self):
        return sum(edge.length for edge in self.edges)

    def compute_inner_angles(self):
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        angles = [
            math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c))),
            math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))),
            math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        ]
        return angles

class Isosceles(Triangle):
    def __init__(self, point1, point2, point3):
        super().__init__(point1, point2, point3)
        if self.edges[0].length == self.edges[1].length or self.edges[1].length == self.edges[2].length or self.edges[2].length == self.edges[0].length:
            self.is_regular = True

class Equilateral(Triangle):
    def __init__(self, point1, point2, point3):
        super().__init__(point1, point2, point3)
        if self.edges[0].length == self.edges[1].length == self.edges[2].length:
            self.is_regular = True

class Scalene(Triangle):
    def __init__(self, point1, point2, point3):
        super().__init__(point1, point2, point3)
        if self.edges[0].length != self.edges[1].length and self.edges[1].length != self.edges[2].length and self.edges[2].length != self.edges[0].length:
            self.is_regular = False

class TriRectangle(Triangle):
    def __init__(self, point1, point2, point3):
        super().__init__(point1, point2, point3)
        angles = self.compute_inner_angles()
        if any(abs(angle - 90) < 1e-6 for angle in angles):
            self.is_regular = True

class Rectangle(Shape):
    def __init__(self, point1, point2, point3, point4):
        super().__init__()
        self.vertices = [point1, point2, point3, point4]
        self.edges = [Line(point1, point2), Line(point2, point3), Line(point3, point4), Line(point4, point1)]
    
    def compute_area(self):
        base = self.edges[0].length
        height = self.edges[1].length
        return base * height

    def compute_perimeter(self):
        return sum(edge.length for edge in self.edges)

    def compute_inner_angles(self):
        return [90, 90, 90, 90]  

class Square(Rectangle):
    def __init__(self, point1, point2, point3, point4):
        super().__init__(point1, point2, point3, point4)
        if self.edges[0].length == self.edges[1].length == self.edges[2].length == self.edges[3].length:
            self.is_regular = True

