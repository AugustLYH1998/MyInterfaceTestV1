# 1. 导包
from dubboclient import DubboClient

# 2. 创建 dubboclient 实例
dubboclt = DubboClient("211.103.136.244", 6502)

# 日期 和 设置数据
date = {"orderDate": "2021-06-15 16:99:77", "number": 120}
date["class"] = "com.itheima.pojo.OrderSetting"

# 3. 调用 invoke 传 服务名、方法名、实参。得响应结果
resp = dubboclt.invoke("OrderSettingService", "editNumberByDate", date)

# 4. 打印
print("响应结果 =", resp)
print("type(resp) =", type(resp))
