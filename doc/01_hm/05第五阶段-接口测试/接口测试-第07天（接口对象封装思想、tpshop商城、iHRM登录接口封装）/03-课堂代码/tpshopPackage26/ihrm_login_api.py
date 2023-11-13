# 接口对象层
import requests


class IhrmLoginApi(object):
    @classmethod
    def login(cls, json_data):
        resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json=json_data)
        return resp