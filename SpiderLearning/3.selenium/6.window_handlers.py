"""
@Time : 2021/1/31 17:40 
@Author : Steven Chen
@File : 6.window_handlers.py 
@Software: PyCharm
"""
# 目标：
# 方法：
from selenium import webdriver

url = 'https://jn.58.com/'
driver = webdriver.Chrome()

driver.get(url)

# 点击租房按钮
el = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')
el.click()

print(driver.current_url)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[-1])

el_list = driver.find_elements_by_xpath('/html/body/div[7]/div[2]/ul/li/div[2]/h2/a')
print(len(el_list))