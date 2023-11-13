# 1. 导包
from dubboclient import DubboClient

# 2. 创建 dubboclient 实例
dubboclt = DubboClient("211.103.136.244", 6502)

# 管理用户名
name = "admin789"

# 3. 调用 invoke 传 服务名、方法名、实参。得响应结果
resp = dubboclt.invoke("UserService", "findByUsername", name)

# 4. 打印
print("响应结果 =", resp)
print("type(resp) =", type(resp))
