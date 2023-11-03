import pytest


# 装饰器
@pytest.fixture(scope='class', autouse=True)
def exe_sql():
    print('请求查询数据库')
# 前后置
# @pytest.mark.controller
class TestController:
    def test_setup(self):
        print('用例请求前')

    # exe_sql用例会被执行
    # def test_fixture(self, exe_sql):
    #     print('test_fixture')


    def test_end(self):
        print('用例请求后')
