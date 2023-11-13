import logging
import os
import yaml

# 读取yaml文件位置
def read_yaml_path(filename):
    return os.path.dirname(__file__)+f'\\..\\datas\\{filename}'

# 读取测试用例
def read_testcase(filename):
    with open(read_yaml_path(filename+'.yaml'), encoding="utf-8", mode='r') as f:
        return yaml.load(f, yaml.FullLoader)

# 参数化数据解构
def get_yaml_config(config):
    # url = config['request']['url']
    # data = config['request']['params']
    # method = config['request']['method']
    rs = {}
    dict_keys = config['request'].keys()
    for item in dict_keys:
        rs[item] = config['request'][item]
    return rs


# 存放变量的路径
filePath = os.path.join(os.path.dirname(__file__),'..\\datas\\', 'extract.yaml')

# 写入变量
# 将data写入yaml文件
def write_yaml(data):
    with open(filePath, encoding="utf-8", mode="a+") as f:
        # yaml.dump将python对象转换为yaml字符串
        logging.debug(f'yaml写入成功：{data}')
        yaml.dump(data, stream=f, allow_unicode=True)
        f.close()

# 读取变量
def read_yaml(key):
    with open(filePath, encoding="utf-8", mode="r") as f:
        # yaml.dump将python对象转换为yaml字符串
        result = yaml.load(f, yaml.FullLoader)
        return result[key]

# 清空yaml变量文件
def clear_yaml():
    with open(filePath, encoding="utf-8", mode="w") as f:
        f.truncate()
