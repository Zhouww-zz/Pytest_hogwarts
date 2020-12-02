
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:

    def setup(self):
        #初始化一个驱动
        self.driver = webdriver.Chrome()
        #窗口最大化
        self.driver.maximize_window()
        #隐式等待
        self.driver.implicitly_wait(5)
    def teardown(self):
        #关闭浏览器
        self.driver.quit()

    def test_hogwarts(self):
        #打开浏览器
        self.driver.get("https://www.v2ex.com/")
        #找到元素交易，并点击，一开始可以借助selenium的IDE来定位元素
        self.driver.find_element_by_link_text("交易").click()
        #在显示等待前需要传入的函数必须要带一个参数，虽然用不到，但必须带
        def wait(x):
            return len(self.driver.find_elements(By.XPATH,'//*[class="box"]')) >= 1
        #并不是每个都用到WebDriverWait，有内置函数,作用跟def wait(x)一样，例如：
        expected_conditions.element_to_be_clickable(By.XPATH,'//*[class="box"]')
        #可以直接将这一行放入until的括号中去
        # python中传函数时候不用加括号，加括号是调用，不是传参
        WebDriverWait(self.driver, 10).until(wait)
        #找到元素“。。。”并点击
        self.driver.find_element_by_link_text("现在就打开浏览器开始游戏吧").click()