from selenium.webdriver.common.by import By

from selenium_live.selenium_homework.company_simple.po_page.base import Base
from selenium_live.selenium_homework.company_simple.po_page.signup import SignupPage


class LoginPage(Base):
    def scan(self):
        pass
    def goto_signup(self):
        self.find(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return SignupPage(self.driver)