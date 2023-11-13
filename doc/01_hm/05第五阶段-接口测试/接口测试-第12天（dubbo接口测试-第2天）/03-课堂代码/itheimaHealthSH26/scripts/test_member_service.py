# 借助 unittest 框架，封装测试类，从 TestCase 继承
import unittest

from parameterized import parameterized

from api.member_service import MemberService


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