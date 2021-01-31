"""
@Time : 2021/1/31 14:49 
@Author : Steven Chen
@File : 3.driver_atti.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import time
from selenium import webdriver

url = 'https://www.baidu.com/'

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 访问指定的url
driver.get(url)

# 显示源码
print(driver.page_source)

# 显示对应的url
print(driver.current_url)
print(driver.title)

time.sleep(2)
driver.get('http://www.douban.com')

time.sleep(2)
driver.back()

time.sleep(2)
driver.forward()

time.sleep(2)
# driver.close()
# quit()也可以实现退出
driver.quit()

#
driver.save_screenshot('baidu.png')