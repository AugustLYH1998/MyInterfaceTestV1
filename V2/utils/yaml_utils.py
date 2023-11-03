import os
import yaml

""" ==============yaml相关的方法============== """
# 存放变量的路径
filePath = os.path.join(os.path.dirname(__file__),'..\\yaml_conf\\', 'extract.yaml')

# 写入变量
# 将data写入yaml文件
def write_yaml(data):
    with open(filePath, encoding="utf-8", mode="a+") as f:
        # yaml.dump将python对象转换为yaml字符串
        print('yaml写入成功：:', data)
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

# 读取测试用例
def read_testcase(path):
    with open(path, encoding="utf-8", mode='r') as f:
        return yaml.load(f, yaml.FullLoader)