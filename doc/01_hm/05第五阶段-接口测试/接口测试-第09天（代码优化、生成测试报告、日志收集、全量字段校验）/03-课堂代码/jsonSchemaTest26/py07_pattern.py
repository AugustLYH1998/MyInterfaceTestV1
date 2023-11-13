import jsonschema

# 测试数据
data = {
    "message": "!jeklff37294操作成功43289hke",
    "mobile": "15900000002"
}

# 校验规则
schema = {
    "type": "object",
    "properties": {
        "message": {"pattern": "操作成功"},
        "mobile": {"pattern": "^[0-9]{11}$"}
    }
}

# 调用方法校验
res = jsonschema.validate(instance=data, schema=schema)
print(res)
