import requests

# 发送 post 登录请求，指定 url、请求头、请求体，获取响应结果
resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                     # headers={"Content-Type": "application/json"},
                     json={"mobile": "13800000002", "password": "123456"})

# 打印响应结果
print(resp.json())
