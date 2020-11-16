import new


# def factorial(n):
#     if n==1:
#         return n #跳出
#     elif n>1:
#         return n*factorial(n-1) #规律公式
#
#
# print(factorial(4))
#
# # 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
# # 跳出点==> 第一个字符和最后一个字符不是空格
# def my_trim(input_str):
#     if input_str[0] != " " and input_str[-1] != " ":
#         return input_str
#     elif input_str[0]==" ":
#         return my_trim(input_str[1:])#从第二个到最后一个字符
#     elif input_str[-1]==" ":
#         return my_trim(input_str[:-1])#从第一个到倒数第二个(end_index取不到)
#
# print(my_trim(input("")))
#
#
#
# def tell_story(a,b,c,d,v,g):
#     """
#     函数用来将返回值相加的卡拉圣诞节啊麦克雷萨满考虑到那就怒看了上面的的卡兰尼克的撒开了家里的扣篮发可见度撒奥克兰的考虑
#     阿斯顿马丁卡
#     丹江口ndj
#     点卡
#     疯狂的麻烦
#     放孔明灯囧囧
#     能飞多久哦既然人类
#     mfkdmkfjri
#
#     :param a:
#     :param b:
#     :param c:
#     :param d:
#     :param v:
#     :param g:
#     :return:
#     """
#     print('dasdasdasfgsdfsd')
#
#
# def ad(n,m):
#     x = 0
#     for i in range(n,m):
#         x += i
#
#     return x
# print(ad(1,101))

def fac(n:int):
    if n == 1:
        return n
    elif n > 1:
        return n * fac(n-1)


print(fac(5))
new.nddd()