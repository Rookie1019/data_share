import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# dates = pd.date_range('20190301',periods=6)
# # print(dates)
# data = pd.DataFrame(np.random.rand(6,4),index = dates,columns = list('ABCD'))
# # print(data)
# # print(data.T)
# DDDD = data.T
# print(data['20190301':'20190303'])

# obj = pd.Series(range(3),index=['a','b','c'])
# print(obj)
# index = obj.index
# print(index)
np.linspace

def dddd():
    pop = {
        'nevada':{2001:2.4,2002:2.9},
        'ohio':{2000:105,2001:1.7,2002:3.6}
    }
    frame = pd.DataFrame(pop)
    print(frame)
    # frame['2000']['ohio'] = 1.5
    print(frame)


def iloc_loc_ix():
    # a = np.arange(12).reshape(3, 4)
    # print("a: \n", a)
    #
    # df = pd.DataFrame(a)
    # print(df.iloc[1])
    # print("df: \n", df)
    #
    # print("df.loc[0]: \n", df.loc[0])
    # print("df.iloc[0]: \n", df.iloc[0])
    #
    # print("df.loc[:,[0,3]]: \n", df.loc[:, [0, 3]])
    # print("df.iloc[:, [0,3]]: \n", df.iloc[:, [0, 3]])
    x = [1, 2, 3, 4, 5, 6]
    y = [2, 4, 6, 8, 10, 12]

    # plt.plot(x,y, label = '2x',color = 'red',linestyle = '--',linewidth = 1,marker = '.' )
    # plt.plot([1,1.5,2],[3,4.5,6],label = '3x')
    plt.plot(x, y, 'r', label='2x')  # 简写版本  r red   ^ 代表三角形标记 -- 代表虚线

    # 第二条线
    x1 = np.arange(0,4.5,0.5)
    print(x1)
    plt.plot(x1[:3], x1[:3] ** 2, label='x^2')
    plt.plot(x1[2:], x1[2:] ** 2, 'b--')

    plt.title('Our First Graph')
    plt.xlabel('X Axis!')
    plt.ylabel('Y Axis!')

    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])  # 横轴显示的东西
    plt.yticks([0, 2, 4, 6, 8, 10, 12, 14, 16])  # 纵轴显示的东西

    plt.legend()  # 可以让标签显示在右上角

    plt.show()

def zhexiantu():

    gas = pd.read_csv(r'+')
    # plt.plot(gas.Year, gas.USA,'.-', label = 'USA')

    # plt.plot(gas.Year, gas.Canada,'.-', label = 'Canada')

    # plt.plot(gas.Year, gas['South Korea'],'.-', label = 'South Korea')

    # print(gas.Year[::3])
    # print(gas.Year)
    plt.figure(figsize=(20, 10), dpi=150)  # 要在画直线之前表达 后面不行

    for country in gas.columns[1:]:
        plt.plot(gas.Year, gas[country], '.-', label=country)  # 这里刚刚犯了一个错误 country只是字符串类型的索引 并不是数据 想拿到数据就gas[country]

    # 这是另外一个方法 比较有意思 而且容易更改出你想要看的几个
    # country_u_wanted = []  # 就可以在这里面添加自己想看的数据
    # for country in gas:
    #     if country in country_u_wanted:
    #         plt.plot(gas.Year, gas[country], '.-', label=country)


    # print(gas.columns[1:])

    plt.xticks(gas.Year[::3])  # 横坐标是以三个三个的跳跃

    plt.xlabel('Year')
    plt.ylabel('Country')
    # plt.figure(figsize = (20,10), dpi = 300)

    plt.legend()
    plt.show()

def kaoshi():
    # z = [1,1,0]
    # x = np.array(z,dtype=np.int32)
    # j = [[-3,0,-1],[0,-1,-1],[2,0,0]]
    # y = np.array(j,dtype=np.int32)
    # print('x',x)
    # print('y',y)
    # vhhh = x.dot(y.dot(y))
    # print(np.linalg.matrix_rank(vhhh))
    # print('vhhh',vhhh)

    j = [[-1,1,0],[-4,3,0],[1,0,2]]
    y = np.array(j)
    zhi, duoxiangshi= np.linalg.eig(y)

    print('特征值：',zhi)
    print('多项式：', duoxiangshi)
    print(y)
    data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
    data.drop_duplicates()
    return None


x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 0
def course(x):
    return x * w


def loss(x, y):
    y_p = course(x)
    return (y_p - y)**2

def cal():
    w_list = []
    MSE_list = []
    for w in np.arange(0.0, 4.0, 0.1):
        print(w)
        l_sum = 0
        for x_val, y_val in zip(x_data, y_data):
            loss_val = loss(x_data, y_data)
            l_sum += loss_val
        w_list.append(w)
        MSE_list.append(l_sum / 3)
cal()

if __name__ == '__main__':
    # iloc_loc_ix()
    # zhexiantu()
    kaoshi()