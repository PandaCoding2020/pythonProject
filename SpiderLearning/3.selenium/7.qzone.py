"""
@Time : 2021/1/31 18:04 
@Author : Steven Chen
@File : 7.qzone.py 
@Software: PyCharm
"""
# 目标：
# 方法：
from selenium import webdriver

url = 'https://qzone.qq.com'

driver = webdriver.Chrome()

driver.get(url)

driver.switch_to_frame('login_frame')

driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('527729740')
driver.find_element_by_id('p').send_keys('pandacode828168')
driver.find_element_by_id('login_button').click()

