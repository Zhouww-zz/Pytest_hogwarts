import allure
import pytest

# @allure.severity(allure.severity_level.NORMAL)
# def test_login_success1(self):
#     print("这是严重性级别为normal的测试用例")
#     pass
# @allure.severity(allure.severity_level.CRITICAL)
# def test_login_success6(self):
#     print("这是严重性级别为critical的测试用例")
#     pass

@allure.feature("登录模块")
@allure.severity(allure.severity_level.NORMAL)
class TestLogin(object):

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_success2(self):
        print("这是严重性级别为normal的测试用例")
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success3(self):
        print("这是严重性级别为critical的测试用例")
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success4(self):
        print("这是严重性级别为critical的测试用例")
        pass

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_login_success6(self):
        print("这是严重性级别为trivial的测试用例")
        pass
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_success5(self):
        print("这是严重性级别为blocker的测试用例")
        pass
if __name__ == '__main__':
    pytest.main()