# 1. 导包
import jsonschema

# 2. 创建 校验规则
schema = {
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "code": {
            "type": "int"
        },
        "message": {
            "type": "string"
        }
    },
    "required": ["success", "code", "message"]
}

# 准备待校验数据
data = {
    "success": True,
    "code": 10000,
    "message": "操作成功"
}

# 3. 调用 validate 方法，实现校验
result = jsonschema.validate(instance=data, schema=schema)
print("result =", result)

# None: 代表校验通过
# ValidationError：数据 与 校验规则不符
# SchemaError： 校验规则 语法有误