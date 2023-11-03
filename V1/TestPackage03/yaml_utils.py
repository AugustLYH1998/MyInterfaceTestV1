import os
import yaml

filePath = os.path.join(os.path.dirname(__file__), '..', 'extract.yaml')
# 写入
# 将data写入yaml文件
def write_yaml(data):
    with open(filePath, encoding="utf-8", mode="a+") as f:
        # yaml.dump将python对象转换为yaml字符串
        print('data:', data)
        yaml.dump(data, stream=f, allow_unicode=True)
        f.close()

# 读取
def read_yaml(key):
    with open(filePath, encoding="utf-8", mode="r") as f:
        # yaml.dump将python对象转换为yaml字符串
        result = yaml.load(f, yaml.FullLoader)
        return result[key]

# 清空yaml
def clear_yaml():
    with open(filePath, encoding="utf-8", mode="w") as f:
        f.truncate()


# 读取测试用例
yaml_path = os.path.join(os.path.dirname(__file__), '.', 'test_get_token.yaml')
def read_testcase(path):
    with open(path, encoding="utf-8", mode='r') as f:
        return yaml.load(f, yaml.FullLoader)


if __name__ == '__main__':
    print(read_testcase(yaml_path))
