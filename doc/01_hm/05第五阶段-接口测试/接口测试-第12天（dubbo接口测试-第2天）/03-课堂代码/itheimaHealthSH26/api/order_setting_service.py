import json

from api.base_service import BaseService


class OrderSettingService(BaseService):
    def __init__(self):
        super().__init__()
        self.service_name = "OrderSettingService"

    def add(self, date_list):
        # 功能：添加预约设置
        # :param date_list:
        #     1. 日期列表，如：[{"orderDate":"2021-09-20 16:45:12","number":20}]
        #     2. 日期格式为："2021-09-20 16:45:12"，必须包括时分秒
        # :return: 设置成功返回 True,  设置失败返回 False
        resp = self.dubbo_client.invoke(self.service_name, "add", date_list)
        if resp == "Failed":
            return False
        else:
            return True

    def get_order_setting_by_month(self, month):
        # 功能：按月统计预约设置信息
        # :param months: 日期，如："2021-08"
        # :return: 列表，指定月份的预约信息
        resp = self.dubbo_client.invoke(self.service_name, "getOrderSettingByMonth", month)
        if resp == "Failed":
            return None
        else:
            return json.loads(resp)

    def edit_number_by_date(self, date):
        # 功能：根据日期修改预约设置数量
        # :param info:
        #     1. 预约设置的字典格式数据，参考接口文档填入字段数据
        #     2. 如：{"orderDate":"2021-09-19 17:45:12","number":15}
        #     3. 日期格式为："2021-09-19 17:45:12"，必须包括时分秒
        #     4. 添加 "class":"com.itheima.pojo.OrderSetting"
        # :return: 修改成功返回 True,  修改失败返回 False
        date["class"] = "com.itheima.pojo.OrderSetting"

        # 3. 调用 invoke 传 服务名、方法名、实参。得响应结果
        resp = self.dubbo_client.invoke(self.service_name, "editNumberByDate", date)
        if resp == "Failed":
            return False
        else:
            return True
