import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWxHome:

    def setup(self):
        # option = Options()
        # option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/')
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # cookies = self.driver.get_cookies()
        db = shelve.open('cookies')
        # db['cookies']=cookies

        cookies_local = db['cookies']
        db.close()
        for cookie in cookies_local:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
    # def teardown(self):
    #     self.driver.quit()


    # def test_cookies_get(self):
    #     self.driver.get('https://work.weixin.qq.com/')
    #     # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
    #     # cookies = self.driver.get_cookies()
    #     db = shelve.open('cookies')
    #     # db['cookies']=cookies
    #
    #     cookies_local=db['cookies']
    #     db.close()
    #     for cookie in cookies_local:
    #         if 'expiry' in cookie.keys():
    #             cookie.pop('expiry')
    #         self.driver.add_cookie(cookie)
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
    def test_addcontact(self):
        self.driver.find_element(By.CSS_SELECTOR,'#menu_contacts').click()
        sleep(3)
        before=self.driver.find_element(By.CSS_SELECTOR,'.js_unactive_count_span').text
        self.driver.find_element_by_link_text('添加成员').click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#username').send_keys('username')
        self.driver.find_element(By.CSS_SELECTOR,'#memberAdd_acctid').send_keys('123123')
        self.driver.find_element(By.CSS_SELECTOR,'#memberAdd_phone').send_keys('15314577998')
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'.member_colRight_operationBar:nth-child(3) > .ww_btn_Blue').click()
        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=-10000")
        self.driver.find_element(By.CSS_SELECTOR,'#menu_contacts').click()
        sleep(3)
        result = self.driver.find_element(By.CSS_SELECTOR,'.js_unactive_count_span').text
        assert int(result) == int(before)+1
        print(f'目前已有联系人{result}')


