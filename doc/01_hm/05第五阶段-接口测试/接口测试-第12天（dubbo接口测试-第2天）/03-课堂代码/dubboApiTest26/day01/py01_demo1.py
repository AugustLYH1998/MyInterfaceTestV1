"""
1. 导包 from dubboclient import DubboClient
2. 创建 DubboClient类实例，指定 IP 和 port (int类型)
3. 使用 实例调用 invoke() 方法。 传入：服务名、方法名、实参(方法使用)。获取响应结果
4. 打印响应结果
"""

# 1. 导包 from dubboclient import DubboClient
from dubboclient import DubboClient

# 2. 创建 DubboClient类实例，指定 IP 和 port
dubboclt = DubboClient("211.103.136.244", 6502)

# 3. 使用 实例调用 invoke() 方法。 传入 ：服务名、方法名、实参(方法使用)。获取响应结果
resp = dubboclt.invoke("MemberService", "findByTelephone", "13020210001")

# 4. 打印响应结果
print("响应结果 =", resp)
print("type(resp) =", type(resp))