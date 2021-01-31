"""
@Time : 2021/1/31 15:48 
@Author : Steven Chen
@File : 4.selenium_locate_multi.py 
@Software: PyCharm
"""
# 目标：
# 方法：
from selenium import webdriver


# 1.创建浏览器对象
driver = webdriver.Chrome()

# 2.操作浏览器对象
driver.get('https://www.baidu.com')

# 2.定位元素
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_name('wd').send_keys('python')
# 通过class属性值进行元素定位
driver.find_element_by_class_name('s_ipt').send_keys('python')
# driver.find_element_by_css_selector('#kw').send_keys('python')

driver.find_element_by_xpath('//*[@id="su"]').click()


print(driver.find_element_by_tag_name('title'))

# 通过含有链接的完整文本内容进行元素定位   链接文本(链接和文本在同一个标签中)
# driver.find_element_by_link_text('hao12').click()
driver.find_element_by_partial_link_text('hao123').click()