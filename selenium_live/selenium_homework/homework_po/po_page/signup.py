from time import sleep

from selenium.webdriver.common.by import By

from selenium_live.selenium_homework.company_simple.po_page.base import Base


class SignupPage(Base):
    def signup(self):
        sleep(3)
        self.find(By.ID,'corp_name').send_keys('companyname')
        sleep(3)
        self.find(By.ID,'register_tel').send_keys('15314577998')
        sleep(3)
        self.find(By.ID,'iagree').click()
        sleep(3)
        self.find(By.ID,'submit_btn').click()
        sleep(3)
        return True