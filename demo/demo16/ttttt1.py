# import requests
#
# url = 'http://192.168.7.111/aes.exe'
# res = requests.get(url)
# exe = 'aes.exe'
# with open(exe, 'wb') as f:
#     f.write(res.content)


import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
print(desktop_path)

# from selenium import webdriver
# from time import sleep
# # 创建一个chrome浏览器实例
# browser = webdriver.Chrome()
# #访问百度首页
# browser.get('https://www.baidu.com/')
# sleep(5)
# browser.quit()