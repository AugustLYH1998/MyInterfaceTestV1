import requests

# 发送 获取验证码请求
resp_v = requests.get(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.21519623710645064")

# 从 获取验证码 的响应结果，提取 cookie
my_cookie = resp_v.cookies

# 发送 登录请求 url、请求头、请求体。 携带 cookie。 得响应结果
resp = requests.post(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
                     # headers={"Content-Type": "application/x-www-form-urlencoded"},
                     data={"username": "13012345678", "password": "12345678", "verify_code": "8888"},
                     cookies=my_cookie)
# 打印响应结果
print(resp.json())

# 发送 查看我的订单 请求
resp_o = requests.get(url="http://tpshop-test.itheima.net/Home/Order/order_list.html", cookies=my_cookie)
print(resp_o.text)

