import allure
import pytest
from pytest_liveone.core.caculate import Caculate

#参数中调用calc_init,注意不加括号
def test_calc_demo1(calc_init):
    assert calc_init.mul(1,2) == 2

def test_calc_demo2(calc_init):
    assert calc_init.mul(1,3) == 3

if __name__ == "__main__":
    pytest.main()