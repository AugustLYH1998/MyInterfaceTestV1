"""
类名：UserService，继承于BaseService
实例属性：
    服务名称：service_name，赋值为'UserService'
实例方法：
    def __init__(self)：
        # 先调父类__init__()，再添加实例属性 service_name

    def find_by_username(self, username):
        # 功能：根据用户名查询用户信息
        # :param username: 用户名
        # :return: 1. 如果用户存在，返回用户信息 2. 如果不存在，返回 None

验证结果：
        # 1. 实例化对象
        # 2. 通过实例对象调用实例方法
"""
import json

from day02.base_service import BaseService


# 封装 用户服务类
class UserService(BaseService):
    def __init__(self):
        super().__init__()

    def find_by_user_name(self, name):
        # 3. 调用 invoke 传 服务名、方法名、实参。得响应结果
        resp = self.dubbo_client.invoke("UserService", "findByUsername", name)
        if resp == "null":
            return None
        else:
            return json.loads(resp)


if __name__ == '__main__':
    # 管理员用户名
    name = "李白"
    us = UserService()
    resp = us.find_by_user_name(name)
    print("响应结果 =", resp)
    print("type(resp) =", type(resp))
