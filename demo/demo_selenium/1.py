# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument('--disable-gpu')
# option.add_argument("window-size=1024,768")
option.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=option)
driver.get("https://www.baidu.com/")
cookies = driver.title
print(cookies)
