from selenium.webdriver.common.by import By

from selenium_live.selenium_homework.homework_addcontact.page.base import Base
from selenium_live.selenium_homework.homework_addcontact.page.signup import SignupPage


class LoginPage(Base):
    #扫描二维码
    def scan(self):
        pass
    #去注册，点击注册按钮，跳转到注册页面
    def goto_signup(self):
        self.find(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return SignupPage(self.driver)