import unittest

# 定义测试类
from assert_util import common_assert
from ihrm_login_api import IhrmLoginApi


class TestIhrmLogin(unittest.TestCase):
    # 测试方法 - 登录成功
    def test01_login_success(self):
        # 调用 自己封装 login
        login_data = {"mobile": "13800000002", "password": "123456"}
        resp = IhrmLoginApi.login(login_data)
        print("登录成功:", resp.json())
        # 断言
        common_assert(self, resp, 200, True, 10000, "操作成功")
        # self.assertEqual(200, resp.status_code)
        # self.assertEqual(True, resp.json().get("success"))
        # self.assertEqual(10000, resp.json().get("code"))
        # self.assertIn("操作成功", resp.json().get("message"))

    # 测试方法 - 手机号未注册
    def test02_mobile_not_register(self):
        # 调用 自己封装 login
        login_data = {"mobile": "1384780932", "password": "123456"}
        resp = IhrmLoginApi.login(login_data)
        print("手机号未注册:", resp.json())
        # 断言
        common_assert(self, resp, 200, False, 20001, "用户名或密码错误")

    # 测试方法 - 密码错误
    def test03_pwd_error(self):
        # 调用 自己封装 login
        login_data = {"mobile": "13800000002", "password": "890"}
        resp = IhrmLoginApi.login(login_data)
        print("密码错误:", resp.json())
        # 断言
        common_assert(self, resp, 200, False, 20001, "用户名或密码错误")

    # 测试方法 - 手机号为空
    def test04_mobile_is_none(self):
        # 调用 自己封装 login
        login_data = {"mobile": None, "password": "123456"}
        resp = IhrmLoginApi.login(login_data)
        print("手机号为空:", resp.json())
        # 断言
        common_assert(self, resp, 200, False, 20001, "用户名或密码错误")

    # 测试方法 - 多参
    def test12_more_params(self):
        # 调用 自己封装 login
        login_data = {"mobile": "13800000002", "password": "123456", "abc": "123"}
        resp = IhrmLoginApi.login(login_data)
        print("手机号为空:", resp.json())
        # 断言
        common_assert(self, resp, 200, True, 10000, "操作成功")

    # 测试方法 - 无参
    def test14_none_params(self):
        # 调用 自己封装 login
        login_data = None
        resp = IhrmLoginApi.login(login_data)
        print("手机号为空:", resp.json())
        # 断言
        common_assert(self, resp, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")
