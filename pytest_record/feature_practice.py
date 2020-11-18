import allure
import allure_pytest
import pytest
#对测试模块进行标记
#例如下面的这个整个类是登录模块，将他标记为登录模块，用allure.feature
@allure.feature("登录模块")
class TestLogin():
    #下面这些方法为整个登录模块的子模块，将其标记为子模块，用allure.story
    @allure.story("登陆成功")
    def test_login_success(self):
        print("这是登陆：测试用例，登陆成功")
        pass

    @allure.story("登陆失败")
    def test_login_fail(self):
        print("这是登陆：测试用例，登陆失败")
        pass

    @allure.story("用户名缺失")
    def test_login_namemiss(self):
        print("这是登陆：测试用例，用户名缺失")
        pass

    @allure.story("密码缺失")
    def test_login_passmiss(self):
        #标记每个登陆步骤，用with allure.step()标记，这样可以在测试报告里看到详细的测试情况
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登陆之后登录失败"):
            assert '1' == 1
            print("登陆失败")
        pass

    TEST_CASE_LINK = ""
    @allure.testcase(TEST_CASE_LINK,"链接用例")
    def test_link(self):
        print("这是添加了连接的测试用例")
        pass
   # --allure-link-pattern=issue:http://.../issue{bug的id值}，在执行的时候添加在执行语句中
    @allure.issue('140',"这是一个issue")
    def test_link(self):
        print("这是一个issue")
        pass
if __name__=="__main__":
    pytest.main()