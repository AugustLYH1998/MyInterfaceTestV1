import unittest
from common.DBUtils import DBUtils
from config import TEL
from api.crud_api import MyCRUD
import requests
from common.assert_utils import my_assert


class TestAdd(unittest.TestCase):
    # 测试用户添加
    # 每次执行前删除对应手机号码
    # 每次执行后也删除对应手机号码
    session = None

    @classmethod
    def setUpClass(cls) -> None:
        print("====setUpClass=====")
        cls.session = requests.session()

    @classmethod
    def tearDownClass(cls) -> None:
        print("====tearDownClass=====")

    def setUp(self) -> None:
        print("-----setUp------")
        DBUtils.my_crud(f'delete from `c` where `phonenumber`={TEL}')

    def tearDown(self) -> None:
        print("-----tearDown------")
        DBUtils.my_crud(f'delete from `c` where `phonenumber`={TEL}')

    def test01_add(self):
        datas = {
            'id': 1,
            'phonenumber': TEL
        }

        rs = MyCRUD.add_user(self.session, datas)
        my_assert(self, rs, 200, 200)
