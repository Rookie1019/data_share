class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'h'

p = Person('zhangsna',18)
s = Person('lisi',23)

x = [p,s]
print(x)  # 直接打印列表 会把每个对象打印出来  会调用类中的_repr_方法