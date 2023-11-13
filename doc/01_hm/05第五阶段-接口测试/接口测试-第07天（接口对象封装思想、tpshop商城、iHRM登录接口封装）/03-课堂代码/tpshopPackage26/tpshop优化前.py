import unittest
import requests

from tpshop_login_api import TpshopLoginApi


class TestTpshopLogin(unittest.TestCase):

    # 测试 登录成功
    def test01_login_ok(self):
        # 创建 session实例
        s = requests.Session()

        # 用实例，调用自己封装的 获取验证码 接口
        TpshopLoginApi.get_verify(s)
        # 调用 自己封装的接口，登录
        abc = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
        resp = TpshopLoginApi.login(s, abc)
        print(resp.json())

        # 断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json().get("status"))
        self.assertEqual("登陆成功", resp.json().get("msg"))

    # 测试 手机号不存在
    def test02_tel_not_exists(self):
        # 创建 session实例
        s = requests.Session()

        # 用实例，调用自己封装的 获取验证码 接口
        TpshopLoginApi.get_verify(s)

        # 调用 自己封装的接口，登录
        abc = {"username": "13048932745", "password": "123456", "verify_code": "8888"}
        resp = TpshopLoginApi.login(s, abc)
        print(resp.json())

        # 断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(-1, resp.json().get("status"))
        self.assertIn("账号不存在", resp.json().get("msg"))

    # 测试 密码错误
    def test03_pwd_err(self):
        # 创建 session实例
        s = requests.Session()

        # 用实例，调用自己封装的 获取验证码 接口
        TpshopLoginApi.get_verify(s)

        # 调用 自己封装的接口，登录
        abc = {"username": "13012345678", "password": "123456789", "verify_code": "8888"}
        resp = TpshopLoginApi.login(s, abc)
        print(resp.json())

        # 断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(-2, resp.json().get("status"))
        self.assertIn("密码错误", resp.json().get("msg"))
