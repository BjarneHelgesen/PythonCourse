class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def add(vec1, vec2):
    x = vec1.x + vec2.x
    y = vec1.y + vec2.y   
    return Vector(x,y) 

def negate(vec):
    return Vector(-vec.x, -vec.y)

a = Vector(1,4)
b = Vector(-2, 5)
a_and_b = add(a,b)
print(a_and_b.x, a_and_b.y)
