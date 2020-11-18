#由于要对Caculate进行初始化，所以要先import这个内容
import allure
import pytest
from pytest_liveone.core.caculate import Caculate

#对Caculate进行初始化
#初始化放在方法外面是只初始化一次，初始化但不复用会造成资源浪费，成本很高，所以最好放在模块里面
class TestCalc:

    #在执行整个类之前执行
    def setup_class(self):
        #初始化一次
        self.calc = Caculate()

    #在执行类中的每个方法之前都执行一次
    def setup(self):
        pass

    #测试用例中要测试的东西分类开，例如预期正确执行的，预期报同一种异常的，要测试的类型分一种
    #测试方法的命名规则要记住
    #要将default runner改成pytest
    @pytest.mark.parametrize('a,b,c',[
        [2, 1, 2],
        [3.6, 2, 1.8],
        [10, 2.5, 4],
        [10.0, 2.5, 4.0]
    ])
    #写在类中的方法参数一定不要忘记self
    def test_div_success(self,a,b,c):
        #调用Caculate中的乘法函数，运用断言判断对错
        assert self.calc.div(a,b) == c


    @pytest.mark.parametrize('a,b', [
        [2, 0],
        [0,2],
        [0.2, 0],
    ])
    def test_div_success(self, a, b):
        print("0期望异常")
        #这是预期的异常，返回预期的异常，参数是预期的异常类型
        #参数里面可以写多个异常，如果期望是异常，但不知道异常的具体类型，可以直接写Exception
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    #流程测试例子，在一些比较复杂的场景下，接口的调用顺序很重要，会影响值的覆盖等等，因此流程的测试也需要
    def test_process(self):
        print("流程测试")
        r1=self.calc.mul(1,2)
        r2=self.calc.div(2,1)
        assert r1==2
        assert r2==2
    #这个方法是测试
    @pytest.mark.parametrize('a,b,c',[
        (1.2,1.0,1.2),
        (1.25,1.25,1.5625),
        (0.55,0.79,0.4345)
    ])
    def test_float(self,a,b,c):
        print(f'预期值是：{c},实际值是{a*b}')
        assert self.calc.mul(a,b)==c

if __name__=='__main__':
    pytest.main()
