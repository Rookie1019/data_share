from collections.abc import Iterable

# list temple dict set str range filter map

# 相当于自己写了一个Range函数
class Abc(object):

    def __init__(self,x):
        self.x = x
        self.count = 0

    def __iter__(self): # 在类里面写上这个方法 就成为了可迭代对象

        # pass
        # return Foo()
        return self

    def __next__(self):
        # 每一次for in调用一次next方法 获取返回值
        self.count += 1
        if self.count <= self.x:

            return self.count - 1
        else:
            raise StopIteration  # 让迭代器停止 注意不是(StopAsyncIteration)



class Foo(object):

    def __next__(self):
        return 1




a = int('123')

# for in 循环的本质就是调用_iter_方法，获取到这个方法的返回值
# 返回值是一个迭代器对象，然后再调用这个对象的_next_方法
x = Abc(100) # Abc函数相当于range函数
for m in x:
    print(m)

# isinstance()函数判断一个实例对象是否由指定类创建出来
print(isinstance(a, Iterable))
print(isinstance(x, Iterable))  # 判断是否为可迭代对象

