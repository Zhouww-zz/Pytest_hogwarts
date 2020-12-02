from selenium.webdriver.common.by import By

from selenium_record.selenium_page.page.base import Base
from selenium_record.selenium_page.page.register import RegisterPage


class LoginPage(Base):
    def scan(self):
        pass
    def goto_register(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return RegisterPage(self._driver)