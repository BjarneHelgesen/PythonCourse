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

def vector_str(vec):
    return "x=" + str(vec.x) + " y=" + str(vec.y)


a = Vector(1,4)
b = Vector(-2, 5)

a_plus_b = add(a,b)
print("a:", vector_str(a))
print("b:", vector_str(b))
print("a + b:", vector_str(a_plus_b))

negated = negate(a_plus_b)
print("Negated:", vector_str(negated))
