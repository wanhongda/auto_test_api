"""
1.命名规则
所有的单测文件名都需要满足test_*.py格式或*_test.py格式。
在单测文件中，测试类以Test开头，并且不能带有 init 方法(注意：定义class时，需要以T开头，不然pytest是不会去运行该class的)
在单测类中，可以包含一个或多个test_开头的函数。
此时，在执行pytest命令时，会自动从当前目录及子目录中寻找符合上述约束的测试函数来执行。
原文链接：https://blog.csdn.net/lovedingd/article/details/98952868
pytest的运行方式https://www.cnblogs.com/chenkh512/p/11231435.html

2.运行code规则
Exit code 0 所有用例执行完毕，全部通过
Exit code 1 所有用例执行完毕，存在Failed的测试用例
Exit code 2 用户中断了测试的执行
Exit code 3 测试执行过程发生了内部错误
Exit code 4 pytest 命令行使用错误
Exit code 5 未采集到可用测试用例文件

3.参数化
方便测试函数对测试属于的获取。
 方法：
     parametrize(argnames, argvalues, indirect=False, ids=None, scope=None)
 常用参数：
     argnames：参数名
     argvalues：参数对应值，类型必须为list
                 当参数为一个时格式：[value]
                 当参数个数大于一个时，格式为:[(param_value1,param_value2.....),(param_value1,param_value2.....)]
 使用方法:
     @pytest.mark.parametrize(argnames,argvalues)
     ️ 参数值为N个，测试方法就会运行N次
"""
import pytest
import time

class Test_study:

    # @pytest.mark.parametrize("a",[1,2])
    # def test_print_a(self,a):
    #     print("start {} run".format(a))
    #
    # @pytest.mark.parametrize("a,b",[(1,2),(999,1000)])
    # def test_print_ab(self,a,b):
    #     print("start {} + {} run".format(a,b))
    #
    # def setup(self):
    #     print("setup mothod running......")
    #
    # def teardown(self):
    #     print("teardown running......")
    #
    # @pytest.mark.skipif(condition=2>1,reason="跳过")
    # def test001_pytest(self):
    #     print("test001 running......")
    #     assert 1
    #
    # @pytest.mark.skipif(condition=2>1,reason="跳过")
    # def test002_pytest(self):
    #     print("test002 running......")
    #     assert 0
    #

    @pytest.fixture()
    def before(self):
        print("before running......")

    def test_fixture1(self,before):
        print("study hahaha...")

    def test_fixture2(self,before):
        print("study hahaha...")

    def test_fixture3(self,before):
        print("study hahaha...")


if __name__ == '__main__':
    now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    pytest.main(["test001_study.py","-s","--html=../reports/report{}.html".format(now)])#