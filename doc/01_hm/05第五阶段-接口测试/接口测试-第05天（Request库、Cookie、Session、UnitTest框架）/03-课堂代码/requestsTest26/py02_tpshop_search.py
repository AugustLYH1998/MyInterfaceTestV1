import requests

# 发送 get 请求，指定 url，获取 响应结果
# 方法1：
# resp = requests.get(url="http://tpshop-test.itheima.net/Home/Goods/search.html?q=iPhone")
# 方法2：
resp = requests.get(url="http://tpshop-test.itheima.net/Home/Goods/search.html",
                    params={"q": "iPhone"})

# 查询响应结果
print(resp.text)
