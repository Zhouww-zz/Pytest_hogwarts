from selenium.webdriver.common.by import By

from selenium_record.selenium_page.page.base import Base


class RegisterPage(Base):
    def register(self):
        self.find(By.ID,"corp_name").send_keys("hello")
        self.find(By.ID,"manager_name").send_keys("hello2")
        return True