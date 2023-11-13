import unittest
import requests

from tpshop_login_api import TpshopLoginApi
from parameterized import parameterized


# 封装 通用 的 断言函数
def common_assert(self, resp, status_code, status, msg):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(status, resp.json().get("status"))
    self.assertIn(msg, resp.json().get("msg"))


json_data = [
    {
        "req_body": {"username": "13012345678", "password": "123456", "verify_code": "8888"},
        "status_code": 200,
        "status": 1,
        "msg": "登陆成功"
    },
    {
        "req_body": {"username": "13048392845", "password": "123456", "verify_code": "8888"},
        "status_code": 200,
        "status": -1,
        "msg": "账号不存在"
    },
    {
        "req_body": {"username": "13012345678", "password": "123456890", "verify_code": "8888"},
        "status_code": 200,
        "status": -2,
        "msg": "密码错误"
    },
    {
        "req_body": {"username": None, "password": "123456", "verify_code": "8888"},
        "status_code": 200,
        "status": -2,
        "msg": "密码错误"
    },
    {
        "req_body": {"username": "13012345678", "password": None, "verify_code": "8888"},
        "status_code": 200,
        "status": -2,
        "msg": "密码错误"
    }
]


# 定义函数，读取 [{},{},{}] --> [(),(),()]
def read_json_data():
    list_data = []
    for item in json_data:
        tmp = tuple(item.values())
        list_data.append(tmp)

    # 循环结束后，将 list_data 为 [(),(),()] 数据， 返回
    return list_data

class TestTpshopLogin(unittest.TestCase):
    # 添加类属性
    session = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()

    def setUp(self) -> None:
        # 调用 自己封装的接口，获取验证码
        TpshopLoginApi.get_verify(self.session)

    # 测试 tpshop 登录
    @parameterized.expand(read_json_data())
    def test_tpshop_login(self, req_body, status_code, status, msg):
        resp = TpshopLoginApi.login(self.session, req_body)
        common_assert(self, resp, status_code, status, msg)

    # def test01_login_ok(self):
    #     data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
    #     resp = TpshopLoginApi.login(self.session, data)
    #     common_assert(self, resp, 200, 1, "登陆成功")
    #
    # # 测试 手机号不存在
    # def test02_tel_not_exists(self):
    #     data = {"username": "13048392845", "password": "123456", "verify_code": "8888"}
    #     resp = TpshopLoginApi.login(self.session, data)
    #     common_assert(self, resp, 200, -1, "账号不存在")
    #
    # # 测试 密码错误
    # def test03_pwd_err(self):
    #     data = {"username": "13012345678", "password": "123456890", "verify_code": "8888"}
    #     resp = TpshopLoginApi.login(self.session, data)
    #     common_assert(self, resp, 200, -2, "密码错误")
