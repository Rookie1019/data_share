import math

class point(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y

class circle(object):

    def __init__(self,cp:point,r):

        self.r = r
        self.cp = cp

    def get_area(self):
        return math.pi*(self.r)**2

p = point(1,2)
c = circle(p,3)

print(c.get_area())


