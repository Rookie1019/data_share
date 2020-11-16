


def listsum(z):
    if len(z) == 1:
        return z[0]
    else:
        return z[0] + listsum(z[1:])
    # r = z.pop()
    # print(r + qiuhe(z)) 
    






if __name__ == "__main__":
    a = listsum([1])
    print(a)