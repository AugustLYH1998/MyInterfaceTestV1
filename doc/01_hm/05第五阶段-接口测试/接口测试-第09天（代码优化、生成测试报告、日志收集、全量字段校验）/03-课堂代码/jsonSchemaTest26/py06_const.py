import jsonschema

# 测试数据
data = {
    "success": True,
    "code": 10000,
    "message": "操作成功",
    "data": None,
}

# 校验规则
schema = {
    "type": "object",
    "properties": {
        "success": {"const": True},
        "code": {"const": 10000},
        "message": {"const": "操作成功"},
        "data": {"const": None}
    },
    "required": ["success", "code", "message", "data"]
}

# 调用方法校验
res = jsonschema.validate(instance=data, schema=schema)
print(res)
