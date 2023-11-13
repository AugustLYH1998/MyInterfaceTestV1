import requests

resp = requests.put(url="http://ihrm-test.itheima.net/api/sys/user/1467780995754229760",
                    headers={"Authorization": "Bearer 4c51c601-c3f7-4d1a-a738-7848f2439f45"},
                    json={"username": "齐天大圣"})

print(resp.json())
