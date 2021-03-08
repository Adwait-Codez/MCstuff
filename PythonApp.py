import math

class Vec3:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        return Vec3(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        return Vec3(self.x-other.x,self.y-other.y,self.z-other.z)
    def __mul__(self,other):
        return Vec3(self.x*other,self.y*other,self.z*other)
    def __truediv__(self,other):
        return Vec3(self.x/other,self.y/other,self.z/other)
    def length(self):
        return math.sqrt((self.x**2)+(self.y**2)+(self.z**2))