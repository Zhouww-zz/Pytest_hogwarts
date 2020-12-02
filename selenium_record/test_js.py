from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.remote import switch_to

from selenium_record.base import Base


class Test_JS(Base):
    def test_js(self):
        self.driver.get('http://www.baidu.com')
        #在输入框中输入selenium测试：
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        sleep(3)
        #在selenium中执行JavaScript代码块来执行一些操作，例如获取id是su的元素，返回并赋值给element_search
        element_search = self.driver.execute_script('return document.getElementById("su")')
        sleep(3)
        #点击搜索按钮
        element_search.click()
        #使用执行JavaScript脚本将页面下滑10000个像素
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)
        #使用JavaScript获取一些数据，可以将这些数据取出来进行分析
        for code in ['return document.title','return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))
        #还可以放在一起执行
        # self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)')
    def test_timedate(self):
        self.driver.get('https://www.12306.cn/index/')
        #首先通过JavaScript根据id获取到时间输入框中的元素，由于该元素是readonly属性，只读属性，所以要修改时间必须先移除readonly属性，
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        #再把新的时间赋值给a.value
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        #打印一下修改后的value
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(3)
    def test_file_upload(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id('stfile').send_keys('D:\pychrm\Pytest_hogwarts\photo\s.jpg')
        sleep(3)
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        #由于要拖拽的内容在frame中，所以首先要先切换到目的frame中
        self.driver.switch_to.frame('iframeResult')
        #定位两个拖拽的起始和终点位置，拖拽要使用ActionChains
        element_drag = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        element_drop = self.driver.find_element_by_xpath('//*[@id="droppable"]')
        action = ActionChains(self.driver)
        action.drag_and_drop(element_drag,element_drop).perform()
        sleep(3)
        #直接定位是无法定位到弹框中的，所以首先要先定位到弹框中，才能对弹框进行操作，定位，点击确定即accept
        self.driver.switch_to.alert.accept()
        #要将拖拽的元素复位，点击开始运行，由于开始运行不在frame中，所以要先从frame中退出到父类frame或者默认的frame中
        self.driver.switch_to.parent_frame()
        #点击开始运行
        self.driver.find_element_by_id('submitBTN').click()
        sleep(3)

