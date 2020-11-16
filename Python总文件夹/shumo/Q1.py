import pandas as pd
import numpy as np

def main():
    origin_data = pd.read_excel(r'C:\Users\Rookie\Desktop\2020年中国研究生数学建模竞赛赛题\2020年B题\2020年B题--汽油辛烷值建模\数模题\285号和313号样本原始数据chuli.xlsx',sheet_name='操作变量')
    origin_data = origin_data.drop(columns=['时间'])
    # print(origin_data)

    df285 = origin_data.iloc[:40, :].copy()
    print(df285)
    df313 = origin_data.iloc[:40, :].copy()
    # print('df313:\n',df313)

    Theta_285 = ((np.square(df285).sum()-np.square(df285.sum())/df285.count())/(df285.count()-1))**0.5
    print(Theta_285)
    bool_np = (df285 - df285.mean()).abs() - 3 * Theta_285 < 0
    # print(bool_np)

if __name__ == '__main__':
    main()

