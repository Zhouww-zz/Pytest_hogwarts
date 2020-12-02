#由于要对Caculate进行初始化，所以要先import这个内容


import allure
import pytest
import yaml

from pytest_liveone.core.caculate import Caculate


def data_load(path='test_calc_data.yml'):
    with open(path) as f:
        data = yaml.safe_load(f)
        keys=",".join(data[0].keys())
        values=[list(d.values()) for d in data]
        data={'keys':keys,'values':values}
        return data

@allure.feature("计算器模块")
class TestCalc:

    #在执行整个类之前执行
    # def setup_class(self):
    #     #初始化一次
    #     self.calc = Caculate()
    #下面的classmethod跟上面的setup_class作用是一样的，一般情况下上面一种情况更简洁，
    # 两者同时存在时下面一种优先执行，会把上面覆盖掉
    @classmethod
    #写在类里面的，同类外面的calc_init
    def setup_class(cls):
        print("setup_class classmethod")
        cls.calc=Caculate()


    data=data_load()

    #记录参数显示在测试报告中
    @allure.step
    def simple_step(self,step_param1,step_param2=None):
        pass
    #在执行类中的每个方法之前都执行一次
    def setup(self):
        pass

    #测试用例中要测试的东西分类开，例如预期正确执行的，预期报同一种异常的，要测试的类型分一种
    #测试方法的命名规则要记住:模块名全部小写，且以test开头，类名Tset开头，驼峰式，方法名小写，以test_开头
    #要将default runner改成pytest
    @pytest.mark.parametrize('a,b,c',[
        [2, 1, 2],
        [3.6, 2, 1.8],
        [10, 2.5, 4],
        [10.0, 2.5, 4.0]
    ])
    #写在类中的方法参数一定不要忘记self
    @allure.story("使用了story")
    def test_div_success1(self,a,b,c):
        #添加一个截图，图片的地址使用的复制绝对路径，参数分别是：图片路径，添加的备注，添加的文件类型
        allure.attach.file(
            'D:\pychrm\Pytest_hogwarts\photo\s.jpg',
            "小恐龙",
            attachment_type=allure.attachment_type.JPG
        )
        #调用这个函数，用来记录参数和返回值，方便在测试报告中查看
        self.simple_step(f"{a} {b} {c}")
        # 调用Caculate中的乘法函数，运用断言判断对错
        assert self.calc.div(a,b) == c


    @pytest.mark.parametrize(data['keys'],data['values'])
    def test_div_success(self, a, b):
        # 这是预期的异常，返回预期的异常，参数是预期的异常类型
        # 参数里面可以写多个异常，如果期望是异常，但不知道异常的具体类型，可以直接写Exception
        with allure.step("0期望异常"):
            with pytest.raises(Exception):
                assert self.calc.div(a, b)

    #流程测试例子，在一些比较复杂的场景下，接口的调用顺序很重要，会影响值的覆盖等等，因此流程的测试也需要
    @allure.story("流程测试")
    def test_process(self):
        with allure.step("先乘后除"):
            r1=self.calc.mul(1,2)
            r2=self.calc.div(2,1)
            assert r1==2
            assert r2==2
    #这个方法是测试
    @allure.story("浮点数相乘")
    @pytest.mark.parametrize('a,b,c',[
        (1.2,1.0,1.2),
        (1.25,1.25,1.5625),
        (0.55,0.79,0.4345)
    ])
    def test_float(self,a,b,c):
       with allure.step(f'预期值是：{c},实际值是{a*b}'):
            assert self.calc.mul(a,b)==c

if __name__=='__main__':
    pytest.main()
