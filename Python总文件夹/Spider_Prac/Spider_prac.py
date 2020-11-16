import requests
from fake_useragent import UserAgent


def spider_para():
    url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList"
    headers = {
        "User-Agent": UserAgent().Chrome
    }
    ID = []  # 存储企业的id
    for page in range(1,6):
        page = str(page)
        para = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':''
        }


        response = requests.post(url,headers=headers,data=para).json()
        # print(response['list'])

        for i in response['list']:
            ID.append(i['ID'])

    return ID



def twice():

    ID = spider_para()
    headers = {
        "User-Agent": UserAgent().Chrome
    }
    base_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in ID:
        data ={'id':id}
        response = requests.post(url=base_url,headers=headers,data=data).json()
        print(response)
        with open('all.txt','a',encoding='utf8',newline='\n') as f:
            f.write(str(response))



def main():

    twice()





if __name__ == '__main__':
    main()
