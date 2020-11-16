

class Point(object):

    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y



class Rectangle(object):

    def __init__(self,Top_left:Point,Bottom_right:Point):
        self.Top_left = Top_left
        self.Bottom_right = Bottom_right

    def area(self):
        print('面积是  ',( self.Top_left.y - self.Bottom_right.y ) * (self.Bottom_right.x
                                                            - self.Top_left.x))
        # return ( self.Top_left.y - self.Bottom_right.y ) * (self.Bottom_right.x
                                                            #- self.Top_left.x)
    def inside(self,p):
        if (self.Top_left.x<p.x<self.Bottom_right.x) and (
                self.Top_left.y<p.y<self.Bottom_right.y):
            print('在矩形内部')
        else:
            print('不在内部')



p1 = Point(1,30)
p2 = Point(40,20)
R3 = Rectangle(p1, p2)

R3.area()

dsa = Point(30,15)
R3.inside(dsa)  # 这里注意  是R调用此函数  然后传递的参数是点  不是点调用