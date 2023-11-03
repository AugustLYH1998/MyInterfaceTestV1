from utils.test_Myrequest import TestCommen
import pytest
import requests

# 测试baseurl
# @pytest.mark.slow_manager
# def test_demo(base_url):
#     print(base_url)

# @pytest.mark.smoke
class TestReq:

    def testGet(self, exe_sql):
        print(exe_sql)
        url = 'http://localhost:3333/api/any'
        datas = {
            'test': exe_sql
        }
        res = TestCommen().api_req(url=url, method='get', params=datas)
        print(res.json())

    # 测试失败用例重跑
    def testfailed(self):
        print('hello')
        # assert 1==2

    # 冒烟测试用例
    def testmark(self):
        print('hello smoke')
