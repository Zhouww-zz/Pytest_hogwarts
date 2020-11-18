import allure
import pytest
import allure_pytest
class TestLink():

    TEST_CASE_LINK = "http://www.baidu.com"
    @allure.testcase(TEST_CASE_LINK,"链接用例")
    def test_link(self):
        print("这是添加了连接的测试用例")
        pass
# --allure-link-pattern=issue:http://.../issue/{bug的id值}，在执行的时候添加在执行语句中
    @allure.issue('140',"这是一个issue")
    def test_link1(self):
        print("这是一个issue")
        pass