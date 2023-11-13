import requests

resp = requests.get(url="http://www.baidu.com")

# - 获取 URL：resp.url
print("url =", resp.url)

# - 获取 响应状态码：resp.status_code
print("status_code =", resp.status_code)

# - 获取 Cookie：resp.cookies
print("cookies =", resp.cookies)

# - 获取 响应头：resp.headers
print("headers =", resp.headers)

# - 获取 响应体：
#   - 文本格式：resp.text
print("body_text =", resp.text)

#   - json格式：resp.json()  当显示 JSONDecodeError 错误时，说明 resp 不能转换为 json格式数据。
print("body_json =", resp.json())
