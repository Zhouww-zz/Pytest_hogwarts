from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    base_url=""
    #括号里面的webdriver没有什么实际作用，只是起到了一个提示作用，提示一些内置函数
    #这个的用法就是在一个变量后加冒号，给他一个类型，就能识别出来它的类型，后续在找内置函数的时候就可以进行提示例如：
    #a:str=""后续在写a.后面就会有string类型的一些内置方法会提示出来
    def __init__(self,driver:WebDriver=None):
        self.driver=''
        if driver is None:
            self.driver=webdriver.Chrome()
        else:
            self.driver=driver
        if self.base_url != '':
            self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def find(self,by,locator):
        return self.driver.find_element(by,locator)

