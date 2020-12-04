from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_live.selenium_homework.homework_addcontact.page.addcontact import AddContact
from selenium_live.selenium_homework.homework_addcontact.page.base import Base
from selenium_live.selenium_homework.homework_addcontact.page.login import LoginPage
from selenium_live.selenium_homework.homework_addcontact.page.signup import SignupPage


class MainPage(Base):
    #注册按钮，跳转到注册页面
    def goto_signup(self):
        self.driver.get('https://work.weixin.qq.com/')
        self.find(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return SignupPage(self.driver)
    #登录按钮，跳转到登录页面
    def goto_login(self):
        self.driver.get('https://work.weixin.qq.com/')
        self.find(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return LoginPage(self.driver)
    #跳转到通讯录页面
    def goto_addcontact(self):
        self.find(By.CSS_SELECTOR,'#menu_contacts').click()
        return AddContact(self.driver)

