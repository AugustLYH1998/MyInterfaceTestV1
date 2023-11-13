import logging
import os
import unittest
import requests

from parameterized import parameterized
from api.login_api import LoginApi
from common.read_json_util import read_json_data
from common.logging_use import init_log_config

class TestApi(unittest.TestCase):
    session = None
    list = read_json_data('login.json')

    @classmethod
    def setUpClass(cls) -> None:
        print("====setUpClass=====")
        cls.session = requests.Session()

    @classmethod
    def tearDownClass(cls) -> None:
        print("====tearDownClass=====")

    def setUp(self) -> None:
        print("-----setUp------")

    def tearDown(self) -> None:
        print("-----tearDown------")

    # 初始化
    init_log_config(os.path.dirname(__file__)+'/test.log')

    @parameterized.expand(list)
    def test_login(self, datas, expected_status_code):
        logging.debug(f'data1:{datas}')
        logging.debug(f'data2:{expected_status_code}')
        # res = LoginApi.login(self.session, data1)
        # logging.debug(f'res.text:{res.text}')
        # self.assertEquals(data2, res.json()['code'])



if __name__ == '__main__':
    unittest.main()