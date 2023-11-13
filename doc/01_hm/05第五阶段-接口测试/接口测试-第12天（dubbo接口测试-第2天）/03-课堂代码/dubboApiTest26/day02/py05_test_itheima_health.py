"""
# 1. 导入unittest包
# 2. 自定义测试类
# 3. 自定义测试方法
# 注意: 必须以 test 开头(字母必须全小写, 别拼错单词, 例如: text)
"""
import unittest
from day02.py02_会员服务类封装设计 import MemberService
from parameterized import parameterized


# 借助 unittest 框架，封装测试类，从 TestCase 继承
class TestMemberService(unittest.TestCase):
    ms = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.ms = MemberService()  # 创建MemberService实例

    # 通用测试方法（参数化）
    @parameterized.expand([("13020210001", "13020210001"),
                           ("13020218973", None),
                           ("1302021abc#", None)])
    def test_findByTelephone(self, tel, except_data):
        # print("tel =", tel, "except_data =", except_data)
        resp = self.ms.find_by_telephone(tel)
        if resp is None:
            self.assertEqual(None, resp)
        else:
            self.assertEqual(except_data, resp.get("phoneNumber"))

    @parameterized.expand([(["2021.5"], [3]),
                           (["2017.4"], [0])])
    def test_findMemberCountByMonths(self, month, except_data):
        resp = self.ms.find_member_count_by_months(month)
        print("============ resp =============", resp)
        self.assertEqual(except_data, resp)

    # def test01_tel_exists(self):
    #     tel = "13020210001"
    #     resp = self.ms.find_by_telephone(tel)
    #     print("手机号存在 =", resp)
    #
    #     self.assertEqual("13020210001", resp.get("phoneNumber"))
    #
    # def test02_tel_not_exists(self):
    #     tel = "13020218973"
    #     resp = self.ms.find_by_telephone(tel)
    #     print("手机号不存在 =", resp)
    #
    #     self.assertEqual(None, resp)
    #
    # def test03_tel_has_special_char(self):
    #     tel = "1302021abc#"
    #     resp = self.ms.find_by_telephone(tel)
    #     print("手机号含有字母特殊字符 =", resp)
    #
    #     self.assertEqual(None, resp)
