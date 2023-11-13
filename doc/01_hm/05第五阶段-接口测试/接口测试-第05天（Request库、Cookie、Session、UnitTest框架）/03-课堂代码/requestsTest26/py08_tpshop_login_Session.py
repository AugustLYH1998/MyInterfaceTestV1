import requests

# 1. 创建一个 Session 实例。
session = requests.Session()

# 2. 使用 Session 实例，调 get方法，发送 获取验证码请求。（不需要获取cookie）
resp_v = session.get(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.21519623710645064")

# 3. 使用 同一个 Session 实例，调用 post方法，发送 登录请求。(不需要携带 cookie)
resp = session.post(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
                    data={"username": "13012345678", "password": "12345678", "verify_code": "8888"})
print(resp.json())

# 4. 使用 同一个 Session 实例，调用 get 方法，发送 查看我的订单请求。(不需要携带 cookie)
resp_o = session.get(url="http://tpshop-test.itheima.net/Home/Order/order_list.html")
print(resp_o.text)
