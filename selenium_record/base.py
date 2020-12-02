import os

from selenium import webdriver


class Base():
    def setup(self):
        #这一段是根据测试需求用来测试在不同浏览器中的兼容性时检测用户是在哪个浏览器中进行测试的：
        # browser = os.getenv("browser")
        #如果指定是火狐，那么就启动火狐浏览器
        # if browser == 'firfox':
        #     self.driver = webdriver.Firefox()
        # elif browser == 'headless':
        #     self.driver = webdriver.PhantomJS()
        #都不是就启动chrome浏览器
        # else:
        #     self.driver = webdriver.Chrome()
        # 实例化一个driver
        self.driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()
        # 隐式等待5秒
        self.driver.implicitly_wait(5)


    def teardown(self):
        # 关闭浏览器
        self.driver.quit()