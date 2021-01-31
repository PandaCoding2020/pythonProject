"""
@Time : 2021/1/31 18:23 
@Author : Steven Chen
@File : 8.selenium_cookies.py 
@Software: PyCharm
"""
# 目标：
# 方法：
from selenium import webdriver

url = 'https://www.baidu.com'

driver = webdriver.Chrome()
driver.get(url)

cookies = {data["name"]: data["value"] for data in driver.get_cookies()}
print(cookies)
