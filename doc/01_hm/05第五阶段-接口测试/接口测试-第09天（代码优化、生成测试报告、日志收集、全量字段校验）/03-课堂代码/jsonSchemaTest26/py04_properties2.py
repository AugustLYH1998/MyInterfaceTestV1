import jsonschema

# 准备校验规则
schema = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "code": {"type:": "integer"},
        "message": {"type": "string"},
        "money": {"type": "number"},
        "address": {"type": "null"},
        "data": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "height": {"type": "number"}
            }
        },
        "luckyNumber": {"type": "array"}
    }
}

# 准备测试数据
data = {
    "success": True,
    "code": 10000,
    "message": "操作成功",
    "money": 6.66,
    "address": None,
    "data": {
        "name": "tom",
        "age": 18,
        "height": 1.78
    },
    "luckyNumber": [6, 8, 9]
}

# 调用方法进行校验
res = jsonschema.validate(instance=data, schema=schema)
print(res)
