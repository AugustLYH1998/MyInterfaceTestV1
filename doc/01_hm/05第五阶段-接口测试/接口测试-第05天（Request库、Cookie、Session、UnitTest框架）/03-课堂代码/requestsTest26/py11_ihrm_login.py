import unittest
import requests


# 定义测试类
class TestIhrmLogin(unittest.TestCase):
    # 添加测试方法-登录成功
    def test01_login_ok(self):
        # 发送 post 登录请求，指定 url、请求头、请求体，获取响应结果
        resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json={"mobile": "13800000002", "password": "123456"})
        # 打印响应结果
        print(resp.json())

        # 断言- 响应状态码为 200
        self.assertEqual(200, resp.status_code)
        # 断言 success 的值为 true
        self.assertEqual(True, resp.json().get("success"))
        # 断言 code 的值为 10000
        self.assertEqual(10000, resp.json().get("code"))
        # 断言 message 的值为 操作成功！
        self.assertIn("操作成功", resp.json().get("message"))

    # 添加测试方法-手机号不存在
    def test02_tel_not_exists(self):
        # 发送 post 登录请求，指定 url、请求头、请求体，获取响应结果
        resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json={"mobile": "13808437002", "password": "123456"})
        # 打印响应结果
        print(resp.json())

        # 断言- 响应状态码为 200
        self.assertEqual(200, resp.status_code)
        # 断言 success 的值为 true
        self.assertEqual(False, resp.json().get("success"))
        # 断言 code 的值为 10000
        self.assertEqual(20001, resp.json().get("code"))
        # 断言 message 的值为 操作成功！
        self.assertIn("用户名或密码错误", resp.json().get("message"))

    # 添加测试方法-密码错误
    def test03_pwd_err(self):
        # 发送 post 登录请求，指定 url、请求头、请求体，获取响应结果
        resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json={"mobile": "13800000002", "password": "123456789"})
        # 打印响应结果
        print(resp.json())

        # 断言- 响应状态码为 200
        self.assertEqual(200, resp.status_code)
        # 断言 success 的值为 true
        self.assertEqual(False, resp.json().get("success"))
        # 断言 code 的值为 10000
        self.assertEqual(20001, resp.json().get("code"))
        # 断言 message 的值为 操作成功！
        self.assertIn("用户名或密码错误", resp.json().get("message"))