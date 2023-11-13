# 导包
import requests

# 实例化session
session = requests.Session()

# 使用session发送获取验证码的请求
session.get(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&type=user_reg")

# 使用session发送注册的请求
response = session.post(url="http://tpshop-test.itheima.net/Home/User/reg.html",
                         headers={"Content-Type":"application/x-www-form-urlencoded"},
                         data={"scene":"1",
                               "username":"13822138012",
                               "verify_code":"8888",
                               "password":"123456",
                               "password2":"123456",
                               "invite":""})
# 打印注册的结果
print("注册的结果为：", response.json())