import requests

resp = requests.get(url="http://www.baidu.com")

print(resp.text)