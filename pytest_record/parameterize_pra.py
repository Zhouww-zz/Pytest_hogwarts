import pytest
import yaml


class TestData:
    #要参数化的变量有三个值，可以是string，list，tuple
    #tuple在python中的定义是不可修改的，而list是可以修改的
    @pytest.mark.parametrize(["a","b"],yaml.safe_load(open("./data.yaml")))
    def test_para(self,a,b):
        print(a+b)