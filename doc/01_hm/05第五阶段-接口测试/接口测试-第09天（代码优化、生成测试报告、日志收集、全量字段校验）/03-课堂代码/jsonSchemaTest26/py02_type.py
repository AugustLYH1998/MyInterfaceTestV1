import jsonschema

# 准备校验规则
schema = {
    "type": "object"
}

# 准备数据
data = {"a": 1, "b": 2}
# data = {
#     "success": True,
#     "code": 10000,
#     "message": "操作成功",
#     "money": 6.66,
#     "address": None,
#     "data": {
#         "name": "tom"
#     },
#     "luckyNumber": [6, 8, 9]
# }

# 调用函数
res = jsonschema.validate(instance=data, schema=schema)
print(res)
