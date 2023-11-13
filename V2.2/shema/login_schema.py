schema = {
    # type 待校验元素类型
    "type": "object",
    # 定义待校验的JSON对象中，各个key-value对中value的限制条件
    "properties": {
        "code": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        },
        "token":{
            "type":"string"
        }
        # const:JSON元素必须等于指定的内容，固定值
        # "data": {"const": None},
        # pattern:使用正则表达式约束字符串类型数据
        # "number": {"pattern": "[0-9]{11}"}

    },
    # 定义待校验的JSON对象中，必须存在的key
    "required": ["code", "message"]
}