import pytest
from pytest_liveone.core.caculate import Caculate

#conftest文件中默认包含了很多fixture,其他文件执行时，不需要引用，直接去寻找conftest中的fixture引用

#这部分可以被别的模块使用，写在类里面只能是该类里面使用，而这个地方是公用的

#对Caculate进行初始化

#初始化放在方法外面是只初始化一次，初始化但不复用会造成资源浪费，成本很高，所以最好放在模块里面
@pytest.fixture(scope='module')
def calc_init():
    print("setup_class")
    return Caculate()