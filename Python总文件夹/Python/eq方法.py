

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age



p1 = Person('JACK',18)
p2 = Person('VN',23)
print(id(p1))
print(id(p2))

# print(p1 is p2)

nums1 = [1,2,3]
nums2 = [1,2,3]

#  is 比较内存地址  == 比较值的大小（并不是值  调用的是eq方法 本质是nums1._eq_(nums2)）
print(nums1 is nums2)
print(nums1 == nums2)