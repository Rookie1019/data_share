# from urllib.request import Request,urlopen
from fake_useragent import UserAgent
import requests


base_url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start={}&genres=%E5%89%A7%E6%83%85"

for i in range(100000):
    headers = {
        "User-Agent":UserAgent().random
    }
    url = base_url.format(i*20)


    # request = Request(url,headers = headers)
    # response = urlopen(request)
    #
    # print(response.read().decode())
    response = requests.get(url,headers=headers)
    print(response.text)