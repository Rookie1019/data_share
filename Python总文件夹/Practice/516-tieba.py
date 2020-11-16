from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode
import os


def get_html(url):
    print(url)
    headers = {
        "User-Agent":UserAgent().chrome
    }
    requents = Request(url,headers = headers)
    response = urlopen(requents)
    # print(response.read().decode())
    return response.read()



def save_html(x,y):
    with open(x,'wb') as f:
        f.write(y)


def main():
    base_url = "https://tieba.baidu.com/f?ie=utf-8&{}"
    content = input('请输入要下载文件名  ')
    i = int(input('请输入要下载的页数  '))
    for num in range(i):
        args = {
            "kw":content,
            "pn":num * 50
        }

        args = urlencode(args)
        # print(args)
        print('第'+str(num+1)+'页正在下载')
        filename = '第'+str(num+1)+'页.html'
        html_bytes = get_html(base_url.format(args))
        # print(type(html_bytes))
        save_html(filename,html_bytes)




if __name__ == '__main__':
    main()
