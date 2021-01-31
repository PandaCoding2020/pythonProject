"""
@Time : 2021/1/31 15:48 
@Author : Steven Chen
@File : 4.selenium_locate_multi.py 
@Software: PyCharm
"""
# 目标：
# 方法：
from selenium import webdriver

url = 'https://bj.58.com/changping/chuzu/?PGTID=0d3090a7-0047-e45d-c967-40ee52d9df06&ClickID=3'
# 1.创建浏览器对象
driver = webdriver.Chrome()

# 2.操作浏览器对象
driver.get(url)

el_list = driver.find_elements_by_xpath('/html/body/div[7]/div[2]/ul/li/div[2]/h2/a')

for el in el_list:
    print(el.text)