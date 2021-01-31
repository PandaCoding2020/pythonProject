"""
@Time : 2021/1/31 14:35 
@Author : Steven Chen
@File : 2.selenium_baidu.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import time
from selenium import webdriver
# selenium 1.0  selenium
# selenium 2.0  webdriver + seleniu
# selneium 3.0  webdriver

# 1.创建浏览器对象
driver = webdriver.Chrome()

# 2.操作浏览器对象
driver.get('https://www.baidu.com')
time.sleep(3)

# 2.定位元素
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
driver.find_element_by_xpath('//*[@id="su"]').click()

time.sleep(6)
# 退出浏览器
driver.quit()