from selenium_live.selenium_homework.homework_addcontact.page.main import MainPage


class TestRegister:
    def setup(self):
        self.main=MainPage()
    def test_register(self):
        #这个是通过登陆页面里的注册进入到注册页面
        # result = self.main.goto_login().goto_signup().signup()
        # assert result
        #这个是直接从主页面上进入注册页面
        result=self.main.goto_signup().signup()
        assert result
    #测试添加联系人
    def test_add(self):
        #从主页面跳转到添加联系人页面，调用添加联系人页面里的添加联系人函数进行添加联系人
        result=self.main.goto_addcontact().addcontact()
        assert result
    def test_get_member(self):
        #添加联系人需要的参数
        name='username'
        count='userid'
        number='15314577998'
        #将添加联系人页面保存下来
        addmemberpage=self.main.goto_addcontact()
        #在这个页面添加联系人，
        addmemberpage.addcontact(name,count,number)
        #再在这个页面上获取联系人列表，赋值给result
        result=addmemberpage.get_member(name)
        #断言新添加的联系人在获取的联系人列表中
        assert result
