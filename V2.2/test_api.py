import logging
import os
import pytest
import jsonschema

from utils.yaml_utils import read_testcase, get_yaml_config, write_yaml, clear_yaml, read_yaml
from shema.login_schema import schema


class TestApi:

    # login
    # @pytest.mark.mytest
    @pytest.mark.parametrize('yaml_conf', read_testcase('test_login'))
    def test_login(self, yaml_conf):
        datas = get_yaml_config(yaml_conf)
        res = self.session(
            url=datas['url'], method=datas['method'], json=datas['params'])
        logging.debug(f'res:{res} ----- {res.json()}')
        result = jsonschema.validate(instance=res.json(), schema=schema)
        logging.debug(f'===schema_result:{result}]===')

    # crud
    # @pytest.mark.mycrud
    @pytest.mark.usefixtures("delete_test")
    @pytest.mark.parametrize('yaml_conf', read_testcase('test_createUser'))
    def test_crud(self, yaml_conf):
        datas = get_yaml_config(yaml_conf)
        res = self.session(
            url=datas['url'], method=datas['method'], params=datas['params'])
        logging.debug(f'res:{res} ----- {res.json()}')

    # 存储登录返回变量token
    @pytest.mark.mytest
    @pytest.mark.parametrize('yaml_conf', read_testcase('test_login_token'))
    def test_login_token(self, yaml_conf):
        datas = get_yaml_config(yaml_conf)
        res = self.session(
            url=datas['url'], method=datas['method'], json=datas['params'])
        logging.debug(f'res:{res} ----- {res.json()}')
        result = jsonschema.validate(instance=res.json(), schema=schema)
        logging.debug(f'===schema_result:{result}]===')

        rs = {'token': res.json()['token']}

        clear_yaml()
        write_yaml(rs)

    # 读取变量
    @pytest.mark.mytest
    @pytest.mark.parametrize('yaml_conf', read_testcase('test_login_token_read'))
    def test_login_token_read(self, yaml_conf):
        datas = get_yaml_config(yaml_conf)
        params = read_yaml('token')
        res = self.session(
            url=datas['url'], method=datas['method'], params={'token':params})
        logging.debug(f'res:{res} ----- {res.json()}')
