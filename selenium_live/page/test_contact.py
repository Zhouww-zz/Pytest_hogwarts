import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWx:
    def setup(self):
        # 复用浏览器，debugger模式，复用浏览器的时候cmd不能关，关了就相当于进程结束了，
        # 复用浏览器的时候要提前打开所要打开的页面，
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        #如果需要复用浏览器，则需要在括号中加入：options=option，如果不复用就不用加
        self.driver = webdriver.Chrome()

    def test_contact(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def test_cookies(self):
        #获取当前页面的cookie，是一个列表
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.qq.com', 'expiry': 1606915968, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688849974530901'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'w-H5ANYmcr6kKsAaKfNovh8E0pYw4b8a1B7MGwpjeU34h4O7gWlBwkbaom1JuXLAKDR5IW6doR_-8ctbIyFKbFlekK1ycbLs3ImrUutf6nYy91mzI7Ez90x1FzHW-LtNzrPFp43zmixiGaO0DfGkUIOxw3WWrJ_5Hpw88NF6Lg-hwnw-9krkotUm_Q2irJyRSegzMop9Qz518m4J-45oz9BFCryZM8pioCC46Uc5Iy5Mfs1U-1mSrgTc7TxlhstmctBG7dtLlVuB6mfoFkSozA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688849974530901'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325096204077'}, {'domain': '.work.weixin.qq.com', 'expiry': 1638449658, 'httpOnly': False,
                                            'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
                                            'secure': False, 'value': '1606884814,1606884877,1606884884,1606913658'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a4946326'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '76588872352543'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'XmomNbX2GL8qWt4ZMHtMncQKZwdcnrZFEQRoR6JxOhNhTzTgK6VFy1b3JHFQBNDr'},
            {'domain': '.qq.com', 'expiry': 1669987908, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1201134821.1606884799'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1638419566, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1609507912, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1606947334, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '5n0o1m7'},
            {'domain': '.qq.com', 'expiry': 1607002308, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.85143717.1606884799'}]

        #要先进入到正确的环境里，确保cookies的domain可用，才能有效的利用cookie，否则打开空白页面，cookie不可用
        self.driver.get("https://work.weixin.qq.com")
        #或者是：self.driver.get("https://work.weixin.qq.com/wework_admin/frame")然后获取完cookie后刷新：self.driver.refresh()
        #将cookie添加到driver里，一个个遍历
        for cookie in cookies:
            # 'expiry': 1606947334是一个过期时间戳，不支持时间戳是浮点类型，一般来说这个参数是没有用的，但是如果是浮点类型，就会报错
            #所以可以将这个属性删掉
            if 'expiry' in cookie.keys():
                #删掉这个key
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        #拥有了cookie就可以打开相应的页面了
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #shelve,python自带的对象持久化存储
    #相当于一个小型的数据库
    #运行完这个测试用例，就会生成三个文件来保存数据的key和value，相当于永久保存下来了，就可以把代码里的cookie数据删除掉，
    # 用的时候直接调用小型数据库
    def test_database(self):
        #先打开这个名为cookies的数据库，把他赋值给本地创建的一个cookies变量
        db = shelve.open('cookies')
        cookies = db['cookie']
        #用完要记得关闭
        db.close()
        self.driver.get("https://work.weixin.qq.com")
        #还是依然要先把cookie一个个加入到driver中，才可以打开对应的页面
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #点击导入联系人，这里的语法是在检查元素里面console中获取这个元素，由于这个元素的
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.CLASS_NAME,'ww_fileImporter_fileContainer_uploadInputMask').send_keys("D:\pychrm\Pytest_hogwarts\photo\pytest.xls")
        result = self.driver.find_element(By.CSS_SELECTOR,'.ww_fileImporter_fileContainer_fileNames').text
        assert result == 'pytest.xls'
        sleep(5)