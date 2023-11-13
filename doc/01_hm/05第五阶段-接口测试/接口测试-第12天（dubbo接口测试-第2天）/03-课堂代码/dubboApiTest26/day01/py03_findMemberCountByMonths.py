# 1. 导包
from dubboclient import DubboClient

# 2. 创建 dubboclient 实例
dubboclt = DubboClient("211.103.136.244", 6502)

# 3. 用实例 调用invoke() ，传入 服务名、方法名、实参。 得响应结果
months = ["2021-7"]
resp = dubboclt.invoke("MemberService", "findMemberCountByMonths", [2021.7])

# 4. 查看响应结果
print("响应结果 =", resp)
print("type(resp) =", type(resp))