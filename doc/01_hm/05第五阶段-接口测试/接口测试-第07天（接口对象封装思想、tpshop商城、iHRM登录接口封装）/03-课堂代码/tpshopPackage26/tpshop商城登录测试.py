import unittest
import requests


class TestTpshopLogin(unittest.TestCase):
    # 测试 登录成功
    def test01_login_ok(self):
        # 创建 session 实例
        session = requests.Session()

        # 使用实例，调用get 发送获取验证码请求
        session.get(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.21519623710645064")

        # 使用实例，调用post 发送登录请求
        resp = session.post(
            url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
            data={"username": "13012345678", "password": "123456", "verify_code": "8888"})

        print("响应结果 =", resp.json())

        # 断言：
        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, resp.json().get("status"))
        self.assertEqual("登陆成功", resp.json().get("msg"))

    # 测试 手机号不存在
    def test02_tel_not_exists(self):
        # 创建 session 实例
        session = requests.Session()

        # 使用实例，调用get 发送获取验证码请求
        session.get(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.21519623710645064")

        # 使用实例，调用post 发送登录请求
        resp = session.post(
            url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
            data={"username": "13847834701", "password": "123456", "verify_code": "8888"})


        print("响应结果 =", resp.json())

        # 断言：
        self.assertEqual(200, resp.status_code)
        self.assertEqual(-1, resp.json().get("status"))
        self.assertEqual("账号不存在!", resp.json().get("msg"))

    # 测试 密码错误
    def test03_pwd_err(self):
        # 创建 session 实例
        session = requests.Session()

        # 使用实例，调用get 发送获取验证码请求
        session.get(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.21519623710645064")

        # 使用实例，调用post 发送登录请求
        resp = session.post(
            url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
            data={"username": "13012345678", "password": "123456890", "verify_code": "8888"})

        print("响应结果 =", resp.json())

        # 断言：
        self.assertEqual(200, resp.status_code)
        self.assertEqual(-2, resp.json().get("status"))
        self.assertEqual("密码错误!", resp.json().get("msg"))
