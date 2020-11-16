import sys
import time

class Student():

    __slots__ = ('name','age','Height')  # 返回值是一个元组  在这里面的内容才能被使用修改  也意味着不能再加内容

    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.Height = height

    def Run(self):
        print(self.name,'is runing')

    def Eat(self):
        print(self.name,'is eating')

    def __del__(self):
        # 当对象销毁时自动调用这个额方法
        print(self.name + '调用了del方法')

    # 当print（对象）的时候默认调用这个方法  默认打印对象类型及内存地址<__main__.Student object at 0x02ED1FB8>
    # 和str方法相同  两个都有的时候 默认调用str
    def __repr__(self):
        return '我是repr方法 我被'+self.name+'调用了'
    def __str__(self):
        return "heoldasokdiajsdajsldauijsdjauis"

    # 这个方法可以使类中的对象可以被调用  且调用的时候又返回值
    def __call__(self, *args, **kwargs):
        print('我是call 我被' + self.name + '调用了')

s1 = Student('小明',18,1.72)
s1.Eat()
del s1
s2 = Student('小红',25,2.35)
print(s2)  # 默认打印对象类型及内存地址<__main__.Student object at 0x02ED1FB8>
s2.Run()
s2()  # 调用对象的_call_方法   ==>

time.sleep(5)