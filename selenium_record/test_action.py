import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_record.base import Base


class TestAction(Base):

    @pytest.mark.skip
    def test_case_click(self):
        # 获取url
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        #用xpath定位元素双击
        element_dbl_click = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        # 用xpath定位元素单击
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        # 用xpath定位元素右键

        element_right_click = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        #实例化一个action队列
        action = ActionChains(self.driver)
        #往action队列里面添加动作指令
        action.click(element_click)
        action.double_click(element_dbl_click)
        action.context_click(element_right_click)
        sleep(3)
        #开始执行action队列里面的动作指令
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_move(self):
        self.driver.get('http://www.baidu.com')
        #定位到设置元素
        element_setting = self.driver.find_element_by_xpath("//span[@id='s-usersetting-top']")

        action = ActionChains(self.driver)
        #把光标移动到设置上面
        action.move_to_element(element_setting)
        action.perform()
        element_highsetting = self.driver.find_element(By.XPATH, "//*[@id='s-user-setting-menu']/div/a[2]")
        action.click(element_highsetting)
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_drag(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        element_drag = self.driver.find_element_by_id("dragger")
        element_drop = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.click_and_hold(element_drag).release(element_drop).perform()
        action.drag_and_drop(element_drag,element_drop).perform()
    @pytest.mark.skip
    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        element_input = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        element_input.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()


if __name__ == '__main__':
    #也可以直接在终端里面执行这个py文件
    pytest.main('-v' '-s' 'test_action.py')
