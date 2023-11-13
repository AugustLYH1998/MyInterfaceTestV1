import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import assert_util
from common.db_util import DBUtil
from common.read_json_util import read_json_data
from config import TEL

from parameterized import parameterized


class TestEmpAddParams(unittest.TestCase):
    def setUp(self) -> None:
        # 删除手机号
        delete_sql = f"delete from bs_user where mobile = '{TEL}'"
        DBUtil.uid_db(delete_sql)

    def tearDown(self) -> None:
        # 删除手机号
        delete_sql = f"delete from bs_user where mobile = '{TEL}'"
        DBUtil.uid_db(delete_sql)

    # 通用测试方法 - 实现参数化
    @parameterized.expand(read_json_data())
    def test_add_emp(self, desc, json_data, stauts_code, success, code, message):
        # 准备数据
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer b040daed-39c1-4302-8777-f950770c8a26"}

        # 调用自己封装的 接口
        resp = IhrmEmpCURD.add_emp(header, json_data)
        print(desc, "：", resp.json())

        # 断言
        assert_util(self, resp, stauts_code, success, code, message)