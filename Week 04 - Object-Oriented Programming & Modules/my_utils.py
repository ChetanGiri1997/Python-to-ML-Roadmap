
PI_APPROX = 3.14159

def circle_area(r):
    return PI_APPROX * r * r

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return circle_area(self.radius)

    def __repr__(self):
        return f"Circle(radius={self.radius})"
