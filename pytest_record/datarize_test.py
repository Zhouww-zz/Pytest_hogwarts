import pytest
import yaml


class Test_Demo:
    #参数化
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            #这里打印出来是只有key值，后面的value被省略，是因为参数化的函数不支持字典类型，解决办法是在env文件中加横杠
            print("测试环境的ip地址是：",env["test"])
        elif "dev" in env:
            print("这是开发环境")
    def test_demo1(self):
        print(yaml.safe_load(open("./env.yml")))
