"""
@Time : 2021/1/31 20:58 
@Author : Steven Chen
@File : 9.script_excute.py 
@Software: PyCharm
"""
# 目标：
# 方法：
from selenium import webdriver

url = 'https://jn.lianjia.com/'

driver = webdriver.Chrome()

driver.get(url)

# 滚动条的拖动：执行js代码
js = 'scrllTo(0,500)'
driver.execute_script(js)



driver.find_element_by_xpath('')