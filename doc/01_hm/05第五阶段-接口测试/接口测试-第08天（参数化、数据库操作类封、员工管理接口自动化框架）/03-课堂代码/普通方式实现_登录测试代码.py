import unittest
import requests


class TestIhrmLogin(unittest.TestCase):
    # 测试方法1，登录成功
    def test01_login_success(self):
        # 组织url
        url = "http://ihrm-test.itheima.net/api/sys/login"
        header = {"Content-Type": "application/json"}
        json_data = {"mobile": "13800000002", "password": "123456"}
        resp = requests.post(url=url, headers=header, json=json_data)
        print("登录成功：", resp.json())
        # 断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(True, resp.json().get("success"))
        self.assertEqual(10000, resp.json().get("code"))
        self.assertIn("操作成功", resp.json().get("message"))

    # 测试方法2，密码错误
    def test02_pwd_err(self):
        # 组织url
        url = "http://ihrm-test.itheima.net/api/sys/login"
        header = {"Content-Type": "application/json"}
        json_data = {"mobile": "13800000002", "password": "123456789"}
        resp = requests.post(url=url, headers=header, json=json_data)
        print("密码错误：", resp.json())
        # 断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(False, resp.json().get("success"))
        self.assertEqual(20001, resp.json().get("code"))
        self.assertIn("用户名或密码错误", resp.json().get("message"))
