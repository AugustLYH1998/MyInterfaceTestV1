
# 封装 用户服务类
import json

from api.base_service import BaseService


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
