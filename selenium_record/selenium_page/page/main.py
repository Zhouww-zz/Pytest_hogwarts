from selenium.webdriver.common.by import By

from selenium_record.selenium_page.page.base import Base
from selenium_record.selenium_page.page.login import LoginPage
from selenium_record.selenium_page.page.register import RegisterPage


class MainPage(Base):
    base_url = "https://work.weixin.qq.com/"
    def goto_login(self):
        self.find(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return LoginPage(self._driver)
    def goto_register(self):
        self.find(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return RegisterPage(self._driver)