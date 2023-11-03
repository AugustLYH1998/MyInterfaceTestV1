""" 
参数化 数据驱动

数据驱动：针对一个接口，只写一个测试方法。用一份测试数据文件，管理各个测试用例的测试数据。

参数化：
1. 导包 from parameterized import parameterized
2. 在 通⽤测试⽅法，上⼀⾏，添加 @parameterized.expand()
3. 给 expand() 传⼊ [(),(),()]（调⽤ 转换 [{},{},{}] --> [(),(),()] 的函数）
4. 修改 通⽤测试⽅法，添加形参，个数、顺序，与 [{},{},{}] 中 { } 内的所有 key 完全⼀⼀对应。
5. 在 通⽤测试⽅法内，使⽤形参。
"""


import unittest
import requests
from parameterized import parameterized
from my_utils import MyUtils

json_data = [
    {
        "req_body": {'url': 'http://localhost:3333/api/login', 'username': 'admin', 'password': '123456'},
        'status_code': 200
    },
]


def get_data():
    mylist = []
    for item in json_data:
        mylist.append(tuple(item.values()))
    print(mylist)
    return mylist


class TestAPi(unittest.TestCase):
    session = None
    token = None

    @classmethod
    def setUpClass(cls) -> None:
        print("====setUpClass=====")
        cls.session = requests.session()

    @classmethod
    def tearDownClass(cls) -> None:
        print("====tearDownClass=====")

    def setUp(self) -> None:
        print("-----setUp------")
        self.token = MyUtils.get_token

    def tearDown(self) -> None:
        print("-----tearDown------")

    @parameterized.expand(get_data())
    def test_example(self, param1, param2):
        res = MyUtils.login(self,param1)
        MyUtils.common_assert(self, param2, res)


if __name__ == '__main__':
    unittest.main()
