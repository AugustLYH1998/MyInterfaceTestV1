# 请求测试
import requests
from yaml_utils import read_yaml

class TestApi:
    def test_get(self):
        url = 'http://localhost:3333/api/any'
        datas = read_yaml('access_token')
        print(datas)
        response = requests.get(url, params=datas)
        print('test2222--response:', list(response.json().keys())[0])