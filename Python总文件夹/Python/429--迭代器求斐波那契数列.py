# from collections.abc import Iterable

class fb(object):

    def __init__(self,n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 0


    def __iter__(self):

        return self

    def __next__(self):

        if self.count < self.n:

            self.count += 1
            x = self.num1
            self.num1,self.num2 = self.num2,self.num1+self.num2
            return x

        else:
            raise StopIteration




# fb(300000)    # 占时间不占空间
# list[1,2,3,4,5,6,7,8,9,11,2,45,48,15,56,87,51,51,84,8,5,15,454] # 占空间不占时间

x = fb(12)
for a in x:
    print(a)