from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAttribute:
    def setup_method(self,method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    def teardown_method(self,method):
        self.driver.quit()
    def test_attribute(self):
        self.driver.get('https://ceshiren.com/latest')
        self.driver.find_element(By.LINK_TEXT,'所有分类').click()
        sleep(5)
        result_element = self.driver.find_element(By.LINK_TEXT,'所有分类').get_attribute('class')
        assert result_element == 'active'