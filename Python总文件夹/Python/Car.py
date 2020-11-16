

class Car(object):

    def __init__(self,name,color,weight,speed = 0,tire_nums = 4):

        self.tire_nums = tire_nums
        self.color = color
        self.weight = weight
        self.speed = speed
        self.name = name

    def Accelerate(self,x):

        if self.speed <= 0 and x < 0:
            return
        self.speed += x


        print(self.name,'正在加速')
    def down(self):
        print(self.name,'正在减速')
    def stop(self):
        print(self.name,'已经停车')

class Car_auto(Car):

    def __init__(self,name,color,weight,ac,cd,speed = 0,tire_nums = 4):
        # self.tire_nums = tire_nums
        # self.color = color
        # self.weight = weight
        # self.speed = speed
        # self.name = name

        super(Car_auto,self).__init__(name,color,weight,speed,tire_nums)

        self.ac = ac
        self.cd = cd


c1 = Car('小汽车','红色',1.8)

count = 0
while True:
    c1.Accelerate(2)
    count += 2
    if count > 40:
        break

print(c1.name)
print(c1.speed)








