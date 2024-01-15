# '# import random
#
#
# for i in range(100):
#     a = random.randint(1000000000,9999999999)
#     print('ca-app-pub-3940256099942544~' + str(a))
#

import get_chrome_version
import requests
import re
url = 'https://googlechromelabs.github.io/chrome-for-testing/'
heads = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
res = requests.get(url=url, headers=heads)
# print(res.text)
res.encoding = res.apparent_encoding


parr = r"<tr class=status-ok><th><code>chromedriver</code><th><code>win64</code><td><code>(https.*?)</code><td><code>200</code>"


image = re.findall(parr,res.text)
# print(image)

for i in image:
    if get_chrome_version.get_chrome_version() in i:
        print("四段版本号："+ get_chrome_version.get_chrome_version() + i)
    if get_chrome_version.three() in i:
        print("三段版本号："+ get_chrome_version.three() + i)


# import time
#
# from selenium import webdriver
#
# # url地址
# url = 'http://www.baidu.com'
#
# # 定义chrome驱动去地址
#
# # 创建浏览器操作对象
# browser = webdriver.Chrome("E:\enstrRes2\chromedriver.exe")
#
# # 这里我们给哥time等待，假设我们在这段时间内进行的操作
# browser.get(url)
# # 获取前端页面
# time.sleep(5)
# # 输出前端代码中的title字段内容
# print(browser.title)
# browser.quit()'