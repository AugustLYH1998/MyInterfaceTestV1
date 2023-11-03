# 请求测试
import requests
from yaml_utils import write_yaml, read_yaml

class TestApi:
    # 将变量保存到 yaml中
    def test_get_token(self, base_url):
        # print(base_url)
        # url = 'http://localhost:3333/api/access_token'
        data = {
            'grant_type': '1',
            'secret': '1',
            'appid': '1'
        }
        response = requests.get(base_url+'/access_token', params=data)
        token = response.json()
        result = {"access_token": token["access_token"]}
        # 写入
        write_yaml(result)

    def test_get(self):
        url = 'http://localhost:3333/api/any'
        # 读出
        datas = read_yaml('access_token')
        print(datas)
        response = requests.get(url, params=datas)
        print('test111111--response:', list(response.json().keys())[0])