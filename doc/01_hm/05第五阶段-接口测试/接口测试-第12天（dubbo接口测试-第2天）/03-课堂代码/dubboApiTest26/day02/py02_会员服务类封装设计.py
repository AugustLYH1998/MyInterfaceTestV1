"""
类名：MemberService，继承于 BaseService
实例属性：
    服务名称：service_name，赋值为 'MemberService'
实例方法：
    def __init__(self)：
        # 先调父类__init__()，再添加实例属性 service_name

    def find_by_telephone(self, telephone):
        # 功能：根据手机号查询会员信息
        # :param telephone: 手机号
        # :return: 1. 会员存在，返回会员信息 2. 会员不存在，返回None

    def find_member_count_by_months(self, data_list):
        # 功能：根据日期统计会员数
        # :param date_list: 日期列表，格式如：["2021.7"]
        # :return: 返回列表，列表元素为对应月份的会员数，如：[10]

    def add(self, info): 添加会员
        # 功能：添加会员
        # :param info: 会员信息的字典格式数据，参考接口文档填入字段数据，手机号需要唯一
        #              如：{"fileNumber":"D0001", "name":"李白", "phoneNumber":"13020210002"}
        # :return: 添加成功返回True,  添加失败返回False
验证结果：
        # 1. 实例化对象
        # 2. 通过实例对象调用实例方法
        # 2.1 根据手机号查询会员信息
        # 2.2 根据日期统计会员数
        # 2.3 添加会员
"""
import json

from day02.base_service import BaseService


# 将 会员服务 封装成 会员服务类
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


if __name__ == '__main__':
    ms = MemberService()
    resp = ms.find_by_telephone("13020210001")
    print("响应结果 =", resp)
    print("type(resp) =", type(resp))

    print("=" * 66)

    months = ["2021-6"]
    ms = MemberService()
    resp = ms.find_member_count_by_months(months)
    print("响应结果 =", resp)
    print("type(resp) =", type(resp))

    print("&" * 66)

    # 准备 add 方法，所需要的数据
    info = {"id": 911, "name": "杜甫", "phoneNumber": "13048379041"}
    ms = MemberService()
    resp = ms.add(info)
    print("响应结果 =", resp)
    print("type(resp) =", type(resp))