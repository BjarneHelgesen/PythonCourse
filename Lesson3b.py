class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"(x:{self.x}, y:{self.y})"


a = Vector(100,200)
b = Vector(1, 2)
print(a+b)
