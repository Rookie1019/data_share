import requests
from fake_useragent import UserAgent
from lxml import etree
import re




url = "https://www.qiushibaike.com/text/page/3/"

headers = {
    "User-Agent":UserAgent().random
}

response = requests.get(url,headers=headers)
# print(response.text)

e = etree.HTML(response.text)
print(type(e))
# content_s = e.xpath('//div[@class="content"]/span.text()')
# content_s = e.xpath('//[@class="author"]/a[1]/text()')
content_s = e.xpath('//a[@class="article block untagged mb15 typs_long"]/a/href/span/@content')


# 这是正则表达式
# infos = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>',response.text)

print(content_s)
