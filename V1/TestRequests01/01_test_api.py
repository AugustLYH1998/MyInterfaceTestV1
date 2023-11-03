import requests

""" 
# def get(url, params=None, **kwargs)
requests.get()

# def post(url, data=None, json=None, **kwargs)
requests.post()
data跟json取决于body是什么类型
文件上传用files

# def put(url, data=None, **kwargs)
requests.put() 

# def delete(url, **kwargs)
requests.delete()

# 前 4个方法都是return调用requests.request()
# def request(method, url, **kwargs)
requests.request()
#  return session.request(method=method, url=url, **kwargs)

# 生成session对象
requests.session() 
"""

""" 
获取 URL：resp.url
获取 响应状态码：resp.status_code
获取 Cookie：resp.cookies
获取 响应头：resp.headers
获取 响应体：
文本格式：resp.text
json格式：resp.json()
"""

res = requests.get('http://localhost:3333/api')
print('res:',res) #返回的响应
print(res.text) # 返回的文本
print(res.json) # 返回的json
print(res.content) # 返回的字节内容
print(res.status_code) # 返回的状态码
print(res.cookies) # 返回的cookie
print(res.encoding) # 返回的编码格式
print(res.headers) #返回的请求头
print(res.request.url) # 返回的请求数据
print(res.request.body) # 返回的请求数据