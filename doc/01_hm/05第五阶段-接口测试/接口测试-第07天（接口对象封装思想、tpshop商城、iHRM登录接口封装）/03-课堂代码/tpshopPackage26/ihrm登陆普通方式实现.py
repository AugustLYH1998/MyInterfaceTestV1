import unittest
import requests


class TestIhrmLogin(unittest.TestCase):
    # 登陆成功
    def test01_login_success(self):
        resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json={"mobile": "13800000002", "password": "123456"})
        print(resp.json())
        # 断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(True, resp.json().get("success"))
        self.assertEqual(10000, resp.json().get("code"))
        self.assertIn("操作成功", resp.json().get("message"))
