from selenium_record.selenium_page.page.main import MainPage
import pytest

class TestRegister:
    def setup(self):
        self.main = MainPage()
    def test_register(self):
        assert self.main.goto_login().goto_register().register()