from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestPosition:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    # def teardown(self):
    #     self.driver.quit()
    def test_pos(self):
        self.driver.find_element(By.ID,'kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, 'su').click()