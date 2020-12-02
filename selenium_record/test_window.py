from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium_record.base import Base


class TestForm(Base):

    def test_form(self):
        #获取url
        self.driver.get('http://www.baidu.com')
        #登录
        self.driver.find_element_by_link_text('登录').click()
        #注册
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        #实例化一个window变量，获取当前所有窗口的句柄，他是一个列表形式
        window = self.driver.window_handles
        #在注册界面输入用户名
        #切换到倒数第一个窗口，也就是最后打开的窗口，如果不切换，默认的是第一个窗口
        self.driver.switch_to_window(window[-1])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("username")
        sleep(3)
        #切换回第一个窗口
        self.driver.switch_to_window(window[0])
        sleep(5)
        #点击微信登陆按钮
        self.driver.find_element_by_xpath('//*[@id="pass_phoenix_btn"]/ul/li[3]/a').click()
        sleep(5)