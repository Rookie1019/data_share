import math
from typing import List
import numpy as np
import pandas as pd
import logging
from gensim.models import Word2Vec
import wordcloud
from pandas.core.tools import numeric

 

def hunwenshu(x):

    y = str(x)
    
    if y[0] == '-':
        
        return False
    else:
        if y == y[::-1]:
            print(y)
            return True
        return False


# def longestCommonPrefix(x):

#     for i in x:
        
#     return 

def MagicIndex(nums:list):

    a = []
    for i in range(len(nums)):
        if i == nums[i]:
            a.append(i)
    if len(a) == 0:
        return -1
    return min(a)
# 更好的方法
# def m(nums):
#     for i in range(len(nums)):
#         if nums[i] == i:
#             return i
#     return -1



def multiply(A,B):

    # z = 0 
    # # if x == 0 or y == 0:
    # #     return z
    # for i in range(y):
    #     z += x
    # return z
    if B == 0:
        return 0
    return A + multiply(A,B-1)
    


def func(s:str):
    s = list(s)
    
    b = 0
    if len(s) <= 50000:
        for i in range(len(s)):
            if a[i] == a[i+1]:
                b = b + 1
    else:
        return None


    pass


def find_consecutive_ones(s):
    local = maximum = 0
    for i in s:
        local = local + 1 if i == 1 else 0
        maximum = max(maximum, local)
        
    return maximum

def last_twice(nums):
    maximum = idx = second = 0
    for i in range(len(nums)):
        if maximum < nums[i]:
            second = maximum
            maximum = nums[i]
            idx = i
        elif second < nums[i]:
            second = nums[i]
    return idx if (maximum >= second * 2) else -1

def jiecheng(n):
    if n == 0:
        return 1
    return n * jiecheng(n-1)

def print_ruler(n):
    assert(n>0)
    if n == 1:
        return '1'
    t = print_ruler(n-1)
    return t + ' ' + str(n) + ' ' + t

def myPow(x: float, n: int) -> float:
    if n < 0:
        x = 1/x
        n = -n
    if n == 0:
        return 1
    
    if n % 2 == 0:
        cal = myPow(x, n/2)
        return cal * cal
    else:
        cal = myPow(x, (n-1)/2)
        return cal * cal * x

def maxSubArray(nums):
    for i in range(1,len(nums)):
        nums[i] = nums[i] + max(nums[i-1], 0)

    return max(nums)

def majorityElement(nums):
    # if len(nums) == 1:
    #     return nums[0]   int(0.5)是0 所以不用做这个边界判断 
    nums.sort()
    return nums[int(len(nums)/2)]


def longestPalindrome(s):
    # stack = []
    # s = list(s)
    # stack.append(s[0])
    # for i in range(1,len(s)):
    #     if s[i] != s[]
    


    return 

def minDistance(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    count = 0
    x, y = len(word1), len(word2)
    if x == 0 or y == 0:
        return max(x, y)
    elif x == y:
        for i in range(x):
            if word1[i] == word2[i]:
                continue
            count += 1
        return count
    elif x < y:
        for i in range(x):
            if word1[i] == word2[i]:
                continue
            count += 1

        return y - x + count
    else:
        for i in range(y):
            if word1[i] == word2[i]:
                continue
            count += 1

        return x - y + count - 1

def rob(nums):
        sum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                sum += nums[i]
        return sum


def benry_search():
    x = np.random.random((3,2,10))
    # x = x.astype(np.int)
    # for i in range(100):
    


    return x

def transpose(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
    #         # x = A[i][j]
    #         # A[j][i] = x
    #         # x = 
            A[i][j], A[j][i] = A[j][i], A[i][j]
    #         # print(len(A))


    return A
def findMedianSortedArrays(nums1, nums2):
    # if len(nums1) != 0 and len(nums2) != 0:
    #     if 
    for i in nums2:
        nums1.append(i)
    nums1 = sorted(nums1)
    x,y = divmod(len(nums1), 2)
    if y == 1:
        return nums1[x]
    else:
        return (nums1[x]+nums1[x-1])/2

        
# def missingNumber(nums):
#     # 二分法找缺失数字
#     a = len(nums)
    
#     if a // 2 == 1:
#         if nums[a-1]/2 == (a-1)/2:
#             new_nums = nums[(a+1)/2:a]
#             missingNumber(new_nums)
#         else:
#             new_nums2 = nums[0:(a+1)/2]
#             missingNumber(new_nums2)
#     else:

def islandPerimeter(grid):
    from keras.preprocessing.sequence import pad_sequences
    a = 0
    m, n = len(grid), len(grid[0])
    # for i in range(m):
    #     grid[i].insert(n, 0)
    #     grid[i].insert(0, 0)
    # grid.insert(m, [0]*(n+2))
    # grid.insert(0, [0]*(n+2))
    # print(grid)
    c = np.array(grid)
    c = np.pad(c, pad_width=1, mode='constant', constant_values=0)
    c = c.toarray()
    for i in range(m):
        for j in range(n):
            a += [grid[i-1][j], grid[i+1,j],grid[i,j-1],grid[i,j+1]].count(0)
    return a


def intersection(nums1, nums2):
    nums = []
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
    for i in nums1:
        if i in nums2:
            nums.append(i)
    return nums

def ccc():
    list = [102, 232, 424]
    count = 0
    d = {}  # Empty dictionary to add values into

    for i in list:
        d[count] = i
        count += 1
    print(d)
    for i in d:
        print(i)


def twoSum(self, nums: List[int], target: int) -> List[int]:
    a = dict()
    d = 0
    for i in range(len(nums)):
        c = target - nums[i]
        if c in nums:
            d = c
            a.append(i)
    for i in range(len(nums)):
        if nums[i] == d:
            a.append(i)
    return a

def longestWord(words: List[str]) -> str:
    words = words.sort()
    # for i,j in enumerate(words):


    return words

if __name__ == "__main__":

    # print(MagicIndex([1,2,3,4,5]))
    # print(m([1,2,2,3,5]))
    # print(multiply(2,10))
    # func('wosdhjia')
    # x = find_consecutive_ones([1,1,1,0,0,0,1,1,1,1,1])
    # x = last_twice([1,2,3,8,3,2,1])
    # x = jiecheng(3)
    # x = print_ruler(5)
    # x = myPow(2.000, 10)
    # x = maxSubArray([-2, 1, -3, 4, 1, 2, 1, -5, 4])
    # x = majorityElement([2,1,2,2,1,2,2,2,1,3])
    # x = longestPalindrome('babad')
    # x = minDistance('a', "ab")
    # x = rob([1,2,3,1])
    # x = benry_search()
    # x = transpose([[1,2,3],[4,5,6],[7,8,9]])
    # x = findMedianSortedArrays([],[1,3,2,4])
    # missingNumber([1,2,3,5,4])
    # islandPerimeter([[0,1,0,0],
    #                 [1,1,1,0],
    #                 [0,1,0,0],
    #                 [1,1,0,0]])
    # x = intersection([4,9,5], [9,4,9,8,4])
    x = longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
    print(x)