# 将参数封装到yaml中
import os
import requests
from yaml_utils import write_yaml, read_yaml, read_testcase
import pytest

class TestApi:
    
    # 配置的yaml config文件
    yaml_path = os.path.join(os.path.dirname(__file__), '.', 'test_get_token.yaml')

    @pytest.mark.packagetest
    @pytest.mark.parametrize('yaml_conf', read_testcase(yaml_path))
    def test_get_token(self, yaml_conf):
        # 读取数据
        data = yaml_conf['request']['params']
        url = yaml_conf['request']['url']

        response = requests.get(url, params=data)
        token = response.json()
        result = {"access_token": token["access_token"]}
        # 写入
        write_yaml(result)

        """ 
        TestPackage03/test_api3_yaml_pack.py::TestApi::test_get_token[yaml_conf0] {'model': '模块1', 'interface': '接口1', 'title': '获取access_token', 'request': {'method': 'get', 'url': 'http://localhost:3333/api/access_token', 'params': {'grant_type': 1, 'secret': 1, 'appid': 1}}, 'validate': None}
        {'model': '模块1', 'interface': '接口1', 'title': '获取access_token', 'request': {'method': 'get', 'url': 'http://localhost:3333/api/access_token', 'params': {'grant_type': 1, 'secret': 1, 'appid': 1}}, 'validate': None}
        data: {'access_token': 'nGXkO48YRbpFm1Eutpb7'}
        PASSED
        
        TestPackage03/test_api3_yaml_pack.py::TestApi::test_get_token[yaml_conf1] {'model': '模块2', 'interface': '接口1', 'title': '获取access_token', 'request': {'method': 'get', 'url': 'http://localhost:3333/api/access_token', 'params': {'grant_type': 1, 'secret': 1, 'appid': 1}}, 'validate': None}
        {'model': '模块2', 'interface': '接口1', 'title': '获取access_token', 'request': {'method': 'get', 'url': 'http://localhost:3333/api/access_token', 'params': {'grant_type': 1, 'secret': 1, 'appid': 1}}, 'validate': None}
        data: {'access_token': 'vZYG1J8LphIfSrH0NhNn'}
        PASSED
        """

    # yaml处理python函数
    yaml_path2 = os.path.join(os.path.dirname(__file__), '.', 'test_get_token_1.yaml')
    @pytest.mark.packagetest
    @pytest.mark.parametrize('yaml_conf', read_testcase(yaml_path2))
    def test_get(self,yaml_conf):
        url = yaml_conf['request']['url']

        # 读出
        datas = yaml_conf['request']['params']
        for k,v in datas.items():
            datas[k] = read_yaml(k)
            datas[v] = read_yaml(v)
        print(datas)

        response = requests.get(url, params=datas)
        print('response:',response.text)

    # 文件上传
    yaml_path3 = os.path.join(os.path.dirname(__file__), '.', 'test_uploadfiles.yaml')

    @pytest.mark.packagetest
    @pytest.mark.parametrize('yaml_conf', read_testcase(yaml_path3))
    def test_file(self, yaml_conf):
        url = yaml_conf['request']['url']

        # open('E:\\test\\MyPython\\demo01\\1.txt', 'rb')
        datas = yaml_conf['request']['files']
        for k,v in datas.items():
            datas[k] = open(datas['media'], 'rb')

        response = requests.post(url, files=datas)
        print(response.text)