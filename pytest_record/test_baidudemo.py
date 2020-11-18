import allure
import pytest
from selenium import webdriver
import time
@allure.testcase("http://www.baidu.com","这是一个测试用例连接的测试用例管理平台地址")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo(test_data1):

    with allure.step("打开百度网页"):
        driver = webdriver.Chrome("D:\pychrm\Pytest_hogwarts")
        driver.get("http://www.baidu.com")
        driver.maximize_window()
    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("kw").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./photo/2.png")
        allure.attach.file("./photo/2.png",name="这是保存的图片",attachment_type=allure.attachment_type.PNG)

    with allure.step("退出浏览器"):
        driver.quit()