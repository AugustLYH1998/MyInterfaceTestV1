import unittest

from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import assert_util


class TestIhrmLogin(unittest.TestCase):
    # 登录成功
    def test01_login_success(self):
        # 组织请求数据
        json_data = {"mobile": "13800000002", "password": "123456"}
        # 调用自己封装的接口
        resp = IhrmLoginApi.login(json_data)
        print("登录成功：", resp.json())

        # 断言
        assert_util(self, resp, 200, True, 10000, "操作成功")

    # 手机号为空
    def test02_mobile_none(self):
        # 组织请求数据
        json_data = {"mobile": None, "password": "123456"}
        # 调用自己封装的接口
        resp = IhrmLoginApi.login(json_data)
        print("手机号为空：", resp.json())

        # 断言
        assert_util(self, resp, 200, False, 20001, "用户名或密码错误")

    # 密码错误
    def test03_pwd_err(self):
        # 组织请求数据
        json_data = {"mobile": "13800000002", "password": "123456890"}
        # 调用自己封装的接口
        resp = IhrmLoginApi.login(json_data)
        print("密码错误：", resp.json())
        # 断言
        assert_util(self, resp, 200, False, 20001, "用户名或密码错误")
