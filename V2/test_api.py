
import pytest
import os
from utils.yaml_utils import write_yaml, read_yaml, read_testcase
from utils.request_utils import get_yaml_path, all_req, get_conf, get_all_yaml_path

class TestApi:

    @pytest.mark.packagetest
    # 测试所有的用例
    def testALL(self):
        list = get_all_yaml_path()
        list.pop(0)
        for path in list:
            yaml_conf = read_testcase(path)
            for item in yaml_conf:
                conf = get_conf(item)
                interface = conf['interface']
                url = conf['url']
                method = conf['method']
                params = conf['params']
                need_write = conf['need_write']
                print(f'==========={interface}==========')
                print('url',url)
                print('method',method)
                print('params',params)
                # 如果不携带参数
                if not params:
                    files = conf['files']
                    path = os.path.join(os.path.dirname(
                        __file__), files['media'])
                    files['media'] = open(path, 'rb')
                    response = all_req(url=url, method=method, files=files)
                else:
                    response = all_req(url=url, method=method, params=params)
                # 如果需要写入文件
                if need_write:
                    datas = {
                        'access_token': response.json()['access_token']
                    }
                    write_yaml(datas)
                print(response.text)


                # datas = {
                #     'access_token': response.json()['access_token']
                # }
                # write_yaml(datas)

    # ==============获取token==============
    yaml_path = get_yaml_path('test_get_token.yaml')
    # @pytest.mark.packagetest
    @pytest.mark.parametrize('yaml_conf', read_testcase(yaml_path))
    def test_gettoken(self, yaml_conf):
        url = get_conf(yaml_conf)['url']
        method = get_conf(yaml_conf)['method']
        params = get_conf(yaml_conf)['params']

        response = all_req(url=url, method=method, params=params)
        print(response.text)

        datas = {
            'access_token': response.json()['access_token']
        }
        write_yaml(datas)

    # ==============读取token==============
    yaml_path2 = get_yaml_path('test_read_token.yaml')
    # @pytest.mark.packagetest
    @pytest.mark.parametrize('yaml_conf', read_testcase(yaml_path2))
    def test_get(self, yaml_conf):

        url = get_conf(yaml_conf)['url']
        method = get_conf(yaml_conf)['method']
        params = get_conf(yaml_conf)['params']

        for k, v in params.items():
            params[k] = read_yaml(k)
            params[v] = read_yaml(v)
        print(params)
        response = all_req(url=url, method=method, params=params)
        print('response:', response.text)

    # ==============文件上传==============
    yaml_path3 = get_yaml_path('test_uploadfiles.yaml')
    # @pytest.mark.packagetest
    @pytest.mark.parametrize('yaml_conf', read_testcase(yaml_path3))
    def test_file(self, yaml_conf):

        url = get_conf(yaml_conf)['url']
        method = get_conf(yaml_conf)['method']
        params = get_conf(yaml_conf)['params']
        for k, v in params.items():
            params[k] = open(params['media'], 'rb')

        response = all_req(url=url, method=method, files=params)
        print(response.text)


