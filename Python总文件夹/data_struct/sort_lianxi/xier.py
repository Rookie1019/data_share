import time



def shell_short(nums):
    start = time.time()

    gap = len(nums)
    lenth = len(nums)

    while gap > 0:
        for i in range(gap, lenth):
            for j in range(i, gap-1, -gap):
                if nums[j-gap] > nums[j]:
                    nums[j], nums[j - gap] = nums[j - gap], nums[j]

        if gap == 2:
            gap = 1
        else:
            gap = gap // 2
    t = time.time() - start     
            
    return len(nums), t

# 4006695518


if __name__ == "__main__":
    x , t = shell_short([1,3,5,7,9,2,8,4,6])
    print(x)
    print('t',t)


    4008895518

