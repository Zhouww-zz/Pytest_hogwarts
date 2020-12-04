from time import sleep

from selenium.webdriver.common.by import By

from selenium_live.selenium_homework.homework_addcontact.page.base import Base


class AddContact(Base):

    def addcontact(self,name,count,number):
        #添加成员
        self.driver.find_element_by_link_text('添加成员').click()
        self.find(By.CSS_SELECTOR, '#username').send_keys(name)
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(count)
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(number)
        self.find(By.CSS_SELECTOR, '.member_colRight_operationBar:nth-child(3) > .ww_btn_Blue').click()
        sleep(3)
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
    def get_member(self,name):
        names_total=[]
        while True:
            #find_elements返回的是一个列表，因为class为“member_colRight_memberTable_td”的有多个元素，所以返回值不止一个
            elements=self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            #这一句是下面两行的简介表达，lambda表达式
            names=[element.get_attribute('title') for element in elements]
            # for element in elements:
            #     names.append(element.get_attribute('title'))
            #将获取的某一页的names添加到总的names_total中，extend语句：将两个列表合并，和语句
            names_total.extend(names)
            #如果此时要查找的name已经存在names_total中，返回True
            if name in names_total:
                return True
            #获取页码处的当前页面数和总页数
            page:str=self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
            #将“1/4”这个字符串用“/”进行分割一次，得到的是[“1”,"4"],分别赋值给num，total，注意此时都是字符串格式
            num,total=page.split('/',1)
            #将num和total进行比较大小，要注意转换成int类型
            if int(num) == int(total):
                #如果此时当前页面已经是最后一页了，还没有找到name，返回False
                return False
            else:
                #如果不是最后一页，点击翻页按钮
                self.find(By.CSS_SELECTOR,'.ww_commonImg_PageNavArrowRightNormal').click()