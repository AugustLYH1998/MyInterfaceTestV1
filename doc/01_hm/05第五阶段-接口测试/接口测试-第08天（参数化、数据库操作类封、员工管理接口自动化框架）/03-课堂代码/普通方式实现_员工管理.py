import requests

# 添加员工
url = "http://ihrm-test.itheima.net/api/sys/user"
header = {"Content-Type": "application/json", "Authorization": "Bearer b040daed-39c1-4302-8777-f950770c8a26"}
json_data = {
    "username": "业务猪001",
    "mobile": "13978734783",
    "workNumber": "9527"
}
resp = requests.post(url=url, headers=header, json=json_data)
print("添加员工：", resp.json())

# 查询员工
url_query = "http://ihrm-test.itheima.net/api/sys/user/1469566449784717312"
header_query = {"Content-Type": "application/json",
                "Authorization": "Bearer b040daed-39c1-4302-8777-f950770c8a26"}
resp_query = requests.get(url=url_query, headers=header_query)
print("查询员工：", resp_query.json())

# 修改员工
url_modify = "http://ihrm-test.itheima.net/api/sys/user/1469566449784717312"
header_modify = {"Content-Type": "application/json",
                 "Authorization": "Bearer b040daed-39c1-4302-8777-f950770c8a26"}

modify_data = {"username": "齐天大圣"}
resp_modify = requests.put(url=url_modify, headers=header_modify, json=modify_data)
print("修改员工：", resp_modify.json())

# 删除员工
url_del = "http://ihrm-test.itheima.net/api/sys/user/1469566449784717312"
header_del = {"Content-Type": "application/json",
              "Authorization": "Bearer b040daed-39c1-4302-8777-f950770c8a26"}
resp_del = requests.delete(url=url_del, headers=header_del)
print("删除员工：", resp_del.json())
