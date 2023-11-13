# 1. 导包
import jsonschema

# 2. 创建 校验规则
schema = {
    # type 待校验元素类型
    "type": "object",
    # 定义待校验的JSON对象中，各个key-value对中value的限制条件
    "properties": {
        "success": {
            "type": "boolean"
        },
        "code": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        },
        # const:JSON元素必须等于指定的内容，固定值
        "data": {"const": None},
        # pattern:使用正则表达式约束字符串类型数据
        "number": {"pattern": "[0-9]{11}"}

    },
    # 定义待校验的JSON对象中，必须存在的key
    "required": ["success", "code", "message"]
}

# 准备待校验数据
data = {
    "success": True,
    "code": 200,
    "message": "操作成功",
    "data": None,
    "number":18161111111
}

# 3. 调用 validate 方法，实现校验
# jsonschema.validate(instance="json数据", schema="jsonshema规则")
result = jsonschema.validate(instance=data, schema=schema)
print("result =", result)

""" 
# None: 代表校验通过
# ValidationError：数据 与 校验规则不符
# SchemaError： 校验规则 语法有误
"""

""" 
integer —— 整数
string —— 字符串
object —— 对象
array —— 数组 --> python：list 列表
number —— 整数/⼩数
null —— 空值 --> python：None
boolean —— 布尔值
语法：
{
"type": "数据类型"
}
"""

""" 
基础正则举例：
1 包含字符串：hello
2 以字符串开头 ^: ^hello 如：hello,world
3 以字符串结尾 $: hello$ 如：中国,hello
4 匹配[]内任意1个字符[]: [0-9]匹配任意⼀个数字 [a-z]匹任意一个小写字母 [cjfew9823]匹配任意一个
5 匹配指定次数{}: [0-9]{11}匹配11位数字。
匹配 手机号：^[0-9]{11}$
"""
