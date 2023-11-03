import unittest
import requests
from parameterized import parameterized
from api.login_api import LoginApi
from common.read_json_util import read_json_data

list = read_json_data('login.json')
class TestApi(unittest.TestCase):

    session = None
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

    @parameterized.expand(list)
    def test_login(self, data1, data2):
        # print(data1)
        # print(data2)
        res = LoginApi.login(self.session, data1)
        print(res.text)
        self.assertEquals(data2, res.json()['code'])
