import pytest
def func(x):
    return x + 1
#参数化，生成多条测试用例
@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1'),
    (3,4),
    (9,10)

])
def test_answer(a,b):
    assert func(a) == b
def test_answer1():
    assert func(4) == 5

#前面加上下面这一行，这个函数变成了装饰器
@pytest.fixture()
def login():
    username="Jerry"
    return username
#类要以Test*开头，类中的方法只会识别test_*开头的方法
class TestDemo:
    #在执行下面一条测试用例时，先执行login函数，并将返回的结果传递给test_a，可以调用
    #假设一种条件是test_a方法调用之前需要先登录
    def test_a(self,login):
        print(f"a    username={login}")

    def test_b(self):
        print("b")

    def test_c(self,login):
        print(f"c   username={login}")
#以python解释器编译时，要有函数入口
if __name__ =="__main__":
    pytest.main(['test_ans.py::test_answer','-v'])
