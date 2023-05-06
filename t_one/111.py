from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
d = webdriver.Chrome()

d.get('https://www.baidu.com')
sleep(3)
d.quit()