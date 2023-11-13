import requests

# 发送 post 请求，指定url、请求头、请求体， 获取响应结果
resp = requests.post(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
                     # headers={"Content-Type": "application/x-www-form-urlencoded"},
                     data={"username": "13012345678", "password": "1234567", "verify_code": "8888"})

# 打印响应结果 - 文本
print(resp.text)
# 打印响应结果 - json
print(resp.json())
