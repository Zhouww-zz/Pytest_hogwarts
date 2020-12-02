from time import sleep

from selenium_record.base import Base

#Base是将很多py文件都用到的代码归到统一的文件中，直接调用，提高复用率，使代码简洁
class TestFrame(Base):
    def test_frame(self):
        #打开frame测试平台
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        #由于想要获取的文本是在一个iframe中，所以要定位到该iframe，switch_to.frame中的参数是iframe的id
        self.driver.switch_to.frame('iframeResult')
        #获取他的文本信息
        print(self.driver.find_element_by_id('draggable').text)
        sleep(3)
        #由于运行按钮不在iframe中，所以要先回到默认的frame或者父类frame
        self.driver.switch_to.parent_frame()
        #获取运行按钮中的文本信息
        print(self.driver.find_element_by_id('submitBTN').text)
        sleep(3)