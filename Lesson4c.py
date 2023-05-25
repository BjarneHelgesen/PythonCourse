import math

class Angle:
    def __init__(self, degrees=None, radians=None):
        if degrees != None:
            assert radians == None
            self.degrees = degrees
            return
        assert radians != None
        self.radians = radians

    @property
    def radians(self):
        return self.degrees * 2*math.pi / 360
    
    @radians.setter
    def radians(self, r):
        self.degrees = r*360/(2*math.pi)

a = Angle(radians=1.8)
print(a.degrees)
a.degrees = 17
print(a.degrees) 
print(a.radians)
a.radians = math.pi
print(a.degrees)