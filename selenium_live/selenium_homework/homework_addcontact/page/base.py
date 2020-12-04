from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    def __init__(self,driver:WebDriver=None):
        base_url=''
        if driver is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver=webdriver.Chrome(options=option)
        else:
            self.driver=driver
        if base_url !='':
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def find(self,by,locator):
        return self.driver.find_element(by,locator)
    def finds(self,by,locator):
        return self.driver.find_elements(by,locator)

