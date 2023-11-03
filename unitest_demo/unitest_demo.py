""" 
unittest 测试框架代码所处文件要求： 遵守 标识符命名规范：
1. 只能使用 字母、数字、下划线
2. 数字不能开头
3. 避免使用 关键字、已知函数名
类：首字母必须大写。建议以 Test 开头
方法：必须 test 开头，建议 编号
"""

import unittest

# 待测试方法
def add(x, y):
    return x + y

# 封装 测试类，从 unittest.TestCase 类继承
class TestAdd(unittest.TestCase):

    # fixture
    # 1、方法级别的 setUp(self) tearDown(self) 每个普通方法执行 之前/之后 自动运行
    def setUp(self) -> None:
        print("-----setUp------")

    def tearDown(self) -> None:
        print("-----tearDown------")

    # 2、类级别的 setUpClass(cls) tearDownClass(cls) 在类内所有方法直 之前/之后 运行一次。
    @classmethod
    def setUpClass(cls) -> None:
        print("====setUpClass=====")

    @classmethod
    def tearDownClass(cls) -> None:
        print("====tearDownClass=====")


    """ 
    assertEqual(参1，参2) ：
    参1：预期结果。 参2：实际结果。
    成功：完全相等。断言通过。不报错！
    失败：报错！
    
    assertIn(参1，参2)：
    参1：预期结果。参2：实际结果。
    成功：实际结果中，包含预期结果。断言通过。不报错！
    失败：报错！
    """

    # 自定义的测试方法
    def test01_add(self):
        print("测试方法1")
        ret = add(10, 20)
        # 断言响应结果
        self.assertEqual(30, ret)

    def test02_add(self):
        print("测试方法2")
        ret = add(100, 200)
        # 断言
        # self.assertEqual(400, ret)
        self.assertEqual(300, ret)


if __name__ == '__main__':
    unittest.main()
