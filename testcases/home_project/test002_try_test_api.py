"""
author:wanhongda
time:2022.02.17
function:
    tongits star 公告接口测试
"""
import pytest
import time
import os
import requests
from assertpy import assert_that
import allure
import sys
sys.path.append(r"C:\ProgramData\Jenkins\.jenkins\workspace\tongits_star_auto_test_api")
from utils import *



# from utils import *


# from utils import yaml_control
# from utils import pre_build_data
# from utils import ByteTracker
# from utils import GameTestUtils
# from utils import SignarureUtils
@allure.feature("Tongits Star登录接口")
class Test_study:
    # 接口yaml所在路径，后面可做成配置文件，依据文件目录、命名来设定yaml所在地址与名称
    file_name_cases = "../../data/home_project/cases/test002_try_test_api.yaml"
    # file_name_apis = "../../data/home_project/apis/test002_try_test_api.yaml"
    # 处理用例数据
    data = yaml_control.get_yaml_data(file_name_cases)
    # url = yaml_control.get_one_yaml_data(file_name_apis)
    print("-----------------------------", data, "*****************************")
    """
    data:
    [('https://itest.tongitsstar.com/data/handleMsg.do', 8201, 0), ('https://itest.tongitsstar.com/data/handleMsg.do', '-0x1001 -0 -"" -auth_register_test', 0)]
    """

    # 参数化处理测试用例，发送请求
    @allure.story("测试用例")
    @allure.title("测试用例001")
    @allure.description("尝试用allure生成美观的测试报告")
    @pytest.mark.parametrize("url,params,status", data)
    def test_run_simple(self, url, params, status):
        #加个判断 判断是否有数组、字典
        # 预处理用例信息
        print("--------------url-----------------", url)
        print("--------------params-----------------", params)
        print("--------------status-----------------", status)
        body = pre_build_data.pre_build(params)
        print("--------------------------------", body)
        res = requests.get(url=url, params=body)
        response_tracker = ByteTracker.ByteTracker("little")
        # 读取响应数据
        # print("res.text2",res.text)
        response_tracker.load(res.text)
        # print("响应内容解析后为：",response_tracker.load(res.text))
        # 获取响应的status
        response_status = response_tracker.get_int()
        print("登录请求的response_status:", response_status)
        assert_that(response_status).is_equal_to(status)
        if response_status == status:
            print("登录请求响应成功！")


if __name__ == '__main__':
    # now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    # print(os.path.abspath(__file__))
    # print(os.path.dirname((os.path.dirname(os.path.dirname(__file__)))))
    reportName = os.path.dirname((os.path.dirname(os.path.dirname(__file__))))
    pytest.main(["test002_try_test_api.py", "-s", '--alluredir', '{}/reports/result/'.format(reportName),
                 '--clean-alluredir'])  #
    print(reportName)
    os.system("allure generate {}/reports/result/ -o {}/reports/report/ --clean".format(reportName, reportName))
    os.system("allure open -h 127.0.0.1 -p 8883 {}/reports/report/".format(reportName))
    print("***执行完成，输出报告***")
