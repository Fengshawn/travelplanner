"""
@author:ZRM
@file:generatePdf.py
@time:2020/03/28
"""

from selenium import webdriver
import time


def setUp():
    # 创建Chrome浏览器配置对象实例
    chromeOptions = webdriver.ChromeOptions()
    # 如果该目录不存在，将会自动创建
    prefs = {"download.default_directory": "C:\\Users\\ZRM\\Desktop\\travelplanner"}
    # 将自定义设置添加到Chrome配置对象实例中
    chromeOptions.add_experimental_option("prefs", prefs)
    # 启动带有自定义设置的Chrome浏览器
    driver = webdriver.Chrome(executable_path="e:\\chromedriver", \
                              options=chromeOptions)


setUp()
