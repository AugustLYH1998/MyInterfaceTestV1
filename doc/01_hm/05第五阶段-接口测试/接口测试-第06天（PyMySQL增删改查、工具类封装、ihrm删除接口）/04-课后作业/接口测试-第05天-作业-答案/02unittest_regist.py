# 导包
import unittest
import requests


class TestTsphopRegist(unittest.TestCase):

    def setUp(self):
        # 实例化session
        self.session = requests.Session()
        self.url = "http://tpshop-test.itheima.net/Home/User/reg.html"
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def tearDown(self):
        # 关闭Session
        self.session.close()

    # 将session实现注册的代码拷贝到框架中
    def test01_regist(self):
        # 使用session发送获取验证码的请求
        resp_verify = self.session.get(
            url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&type=user_reg")
            
        # 断言响应头中包含 image
        self.assertIn('image', resp_verify.headers.get('Content-Type'))

        # 使用session发送注册的请求
        response = self.session.post(url=self.url, headers=self.headers,
                                     data={"scene": "1",
                                           "username": "13822138017",
                                           "verify_code": "8888",
                                           "password": "123456",
                                           "password2": "123456",
                                           "invite": ""})
        # 断言 响应状态码 200
        self.assertEqual(200, response.status_code)
        # 断言 响应体 status 1
        self.assertEqual(1, response.json().get('status'))
        # 断言 响应体 msg 登录成功
        self.assertEqual('注册成功', response.json().get('msg'))

        # 打印注册的结果
        print("注册的结果为：", response.json())
