from selenium_live.selenium_homework.company_simple.po_page.main import MainPage


class TestRegister:
    def setup(self):
        self.main=MainPage()
    def test_register(self):
        # result = self.main.goto_login().goto_signup().signup()
        # assert result
        result=self.main.goto_signup().signup()
        assert result