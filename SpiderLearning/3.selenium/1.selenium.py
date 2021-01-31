"""
@Time : 2021/1/31 10:23 
@Author : Steven Chen
@File : 1.selenium.py 
@Software: PyCharm
"""
# 目标：
# 方法：
from selenium import webdriver

# 指定driver的绝对路径
driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()

# 向一个url发起请求
driver.get("http://www.itcast.cn/")

# 把网页保存为图片
driver.save_screenshot("itcast.png")

# 退出模拟浏览器
driver.quit() # 一定要退出！不退出会有残留进程！


# response = requests.get(url)