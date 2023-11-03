# 请求封装;统一发送请求
import requests
import os
from utils.yaml_utils import read_yaml

req = requests.session()

# 请求行为
def all_req(**args):
    return req.request(**args)

# 获取yaml路径
def get_yaml_path(path):
    return os.path.join(os.path.dirname(__file__), '..\\yaml_conf', path)

# 获取yaml配置项
def get_conf(yaml_conf):
    conf = {
        'url': yaml_conf['request']['url'],
        'method': yaml_conf['request']['method'],
        'need_write': yaml_conf['request']['need_write'],
        'interface': yaml_conf['interface']
    }
    if yaml_conf['request']['files']:
        conf['files'] = yaml_conf['request']['files']
    if yaml_conf['request']['need_read']:
        par = yaml_conf['request']['params']
        print(par)
        for k, v in par.items():
            par[k] = read_yaml(k)
            par[v] = read_yaml(v)
        conf['params'] = par
        return conf
    elif not yaml_conf['request']['need_read']:
        conf['params'] = yaml_conf['request']['params']
        return conf
    elif yaml_conf['request']['files']:
        conf['params'] = yaml_conf['request']['files']
        return conf

# 获取所有yaml文件路径
def get_all_yaml_path():
    # 获取所有yaml配置文件的文件名
    folder_path = os.path.join(os.path.dirname(__file__), '..\\yaml_conf')
    # print(folder_path)

    file_list = []

    # 遍历文件夹，获取每个文件的全路径，添加到 file_list
    for f in os.listdir(folder_path):
        # print(f)
        file_list.append(get_yaml_path(f"{f}"))
    # print(file_list)

    return file_list


