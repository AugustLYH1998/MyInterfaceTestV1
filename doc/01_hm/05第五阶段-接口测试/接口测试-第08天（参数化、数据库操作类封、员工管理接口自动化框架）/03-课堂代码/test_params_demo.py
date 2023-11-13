import json
import unittest
from parameterized import parameterized


# 待 测试方法
def add(x, y):
    return x + y


# data = [
#     {"x": 10, "y": 20, "except": 30},
#     {"x": 100, "y": 200, "except": 300},
#     {"x": 1000, "y": 20, "except": 1020},
#     {"x": 4, "y": 18, "except": 23}
# ]


# [{},{},{}] ---> [(),(),()]
def read_json_data():
    list_data = []
    # 从 .json 文件中，读取 [{},{},{}] 数据
    with open("./params_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

        for item in data:
            tmp = tuple(item.values())
            list_data.append(tmp)

    return list_data


"""
参数实现步骤：
1. 导包 from parameterized import parameterized
2. 在通用测试方法上一行，添加 @parameterized.expand()
3. 给 expand() 传入 [(),(),()] 格式数据。（ 调用 read_json_data() ）
4. 修改 通用测试方法形参，按 数据中的 key 设计 参数。
5. 在 通用测试方法 内，使用形参
"""


class TestAdd(unittest.TestCase):
    # 通用测试方法（实现参数化）
    @parameterized.expand(read_json_data())
    def test_add(self, x, y, except_data):
        res = add(x, y)
        self.assertEqual(except_data, res)

    # def test01_add(self):
    #     res = add(10, 20)
    #     self.assertEqual(30, res)
    #
    # def test02_add(self):
    #     res = add(100, 200)
    #     self.assertEqual(300, res)
    #
    # def test03_add(self):
    #     res = add(1000, 20)
    #     self.assertEqual(1020, res)