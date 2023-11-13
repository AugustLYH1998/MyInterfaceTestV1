import requests

# 创建 session 实例
session = requests.Session()

# 使用实例，调用get 发送获取验证码请求
session.get(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.21519623710645064")

# 使用实例，调用post 发送登录请求
resp = session.post(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
                    data={"username": "13012345678", "password": "123456", "verify_code": "8888"})

print("响应结果 =", resp.json())

