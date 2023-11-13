import json

from api.base_service import BaseService


class MemberService(BaseService):
    def __init__(self):
        super().__init__()  # 调用父类 init 方法
        self.service_name = "MemberService"

    def find_by_telephone(self, tel):
        resp = self.dubbo_client.invoke(self.service_name, "findByTelephone", tel)
        if resp == "null":
            return None
        else:
            # 作用：将 string类型的 数据，还原回成 字典 或 列表 数据。
            return json.loads(resp)

    def find_member_count_by_months(self, months):
        resp = self.dubbo_client.invoke(self.service_name, "findMemberCountByMonths", months)
        # 作用：将 string类型的 数据，还原回成 字典 或 列表 数据。
        return json.loads(resp)

    def add(self, info):
        """
        :param info: 代表 用户 传入的 测试数据，没有 class 元素
        :return:
        """
        # 如果 class 已经存在，覆盖原有class值; 如果不存在 class，新增一组 元素到 字典中。
        info["class"] = "com.itheima.pojo.Member"

        # 3. 调用 invoke 传 服务名、方法名、实参。得响应结果
        resp = self.dubbo_client.invoke(self.service_name, "add", info)
        if resp == "null":
            return True
        else:
            return False