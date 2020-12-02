from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    base_url = ""

    #__init__在python中会自动调用，初始化
    def __init__(self, driver:WebDriver=None):
        self._driver = ""
        #这是一个初始化函数，参数中传入一个driver，
        # 如果不传入这个driver，则每次调用这个类都需要初始化一次driver，
        # 对于一些大型的复杂的项目，初始化很多次效率低下，所以传入一个driver，
        # 只在第一次调用的时候初始化，剩余就不用调用了，会进行判断
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self.base_url != "":
            self._driver.get(self.base_url)
    def find(self,by,locator):
        return self._driver.find_element(by,locator)

