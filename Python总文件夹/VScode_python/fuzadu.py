"""
自己写的max函数 
"""




def thereom(u):

    

    # print(max(u))
    if len(u) != 0:

        y = []

        for i in range(len(u)-1):
            if u[i] < u[i+1]:
                
                y.append(u[i+1])

        print(y)
        thereom(y)
    


if __name__ == "__main__":
    x = [1,3,58,8,79,3,105]
    thereom(x)