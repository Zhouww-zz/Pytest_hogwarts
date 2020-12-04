from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_live.selenium_homework.company_simple.po_page.base import Base
from selenium_live.selenium_homework.company_simple.po_page.login import LoginPage
from selenium_live.selenium_homework.company_simple.po_page.signup import SignupPage


class MainPage(Base):
    base_url = 'https://work.weixin.qq.com/'
    def goto_signup(self):
        self.find(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return SignupPage(self.driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return LoginPage(self.driver)
