import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouch():

    def setup(self):
        #如果不加下面两句会有报错，提示不符合w3c标准
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        #实例化一个driver
        self.driver = webdriver.Chrome(options=option)
        #窗口最大化
        self.driver.maximize_window()
        #隐式等待5秒
        self.driver.implicitly_wait(5)

    # def teardown(self):
    #     #关闭浏览器
    #     self.driver.quit()
    def test_TouchAction(self):
        self.driver.get('http://www.baidu.com')
        element_input = self.driver.find_element_by_id("kw")
        element_search = self.driver.find_element_by_id("su")
        action = TouchActions(self.driver)
        element_input.send_keys("selenium测试")
        action.tap(element_search)
        action.perform()
        #将页面向下滚动，需要三个参数，
        action.scroll_from_element(element_input, 0, 10000).perform()

if __name__ == '__main__':
    pytest.main('-v' '-s' 'test_touch.py')