""" 
获取 URL：resp.url
获取 响应状态码：resp.status_code
获取 Cookie：resp.cookies
获取 响应头：resp.headers
获取 响应体：
文本格式：resp.text
json格式：resp.json()
"""

import unittest
import requests

# 定义测试类
class TestLogin(unittest.TestCase):
    # 添加测试方法
    def test01_login_ok(self):
        # print(1)
        # 发送 post 登录请求，指定 url、请求头、请求体，获取响应结果
        resp = requests.post(url="http://localhost:3333/api/login",
        data={"username": "admin", "password": "123456"})
        # 打印响应结果
        print(resp.json())
        # 断言- 响应状态码为 200
        self.assertEqual(200, resp.json().get('code'))
        self.assertEqual('登录成功', resp.json().get("message"))


if __name__=='__main__':
    # unittest.main()

    # 创建 TestSuite 对象
    suite = unittest.TestSuite()

    # 将要运行的测试方法添加到 TestSuite 中
    suite.addTest(TestLogin('test01_login_ok'))

    # 创建 TextTestRunner 对象并运行测试
    unittest.TextTestRunner().run(suite)
