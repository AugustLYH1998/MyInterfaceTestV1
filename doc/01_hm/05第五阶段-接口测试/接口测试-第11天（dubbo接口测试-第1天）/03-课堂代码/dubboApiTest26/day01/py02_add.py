# 1. 导包
from dubboclient import DubboClient

# 2. 创建 dubboclient 实例
dubboclt = DubboClient("211.103.136.244", 6502)

# 准备 add 方法，所需要的数据
info = {"id": 911, "name": "杜甫", "phoneNumber": "13048379884"}

# 如果 class 已经存在，覆盖原有class值; 如果不存在 class，新增一组 元素到 字典中。
info["class"] = "com.itheima.pojo.Member"

# 3. 调用 invoke 传 服务名、方法名、实参。得响应结果
resp = dubboclt.invoke("MemberService", "add", info)

# 4. 打印
print("响应结果 =", resp)
print("type(resp) =", type(resp))
