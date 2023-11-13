"""
类名：BaseService
实例属性：
    dubbo客户端对象：dubbo_client，创建DubboClient()后给dubbo_client赋值
实例方法：
    def __init__(self)：
        # 添加实例属性 dubbo_client

会员服务类：继承于BaseService
    def __init__(self)：
        # 先调父类__init__()，再添加实例属性 service_name
"""
from dubboclient import DubboClient


class BaseService(object):
    def __init__(self):
        self.dubbo_client = DubboClient("211.103.136.244", 6502)


class MemberService(BaseService):
    def __init__(self):
        super().__init__()
        self.service_name = "MemberService"


if __name__ == '__main__':
    ms = MemberService()
    print(ms.dubbo_client)
