import json
import unittest
from parameterized import parameterized
from get_base_dir import BASE_DIR  # 拿到项目目录


# 待测函数
def login(username, password):
    if username == 'admin' and password == '123456':
        return '登录成功'
    else:
        return '登录失败'


# 读取json文件数据
def build_data():
    with open(BASE_DIR + '/data/login_data.json', 'r', encoding='utf8') as f:
        json_data = json.load(f)  # [{}, {}, {}] ---> [(), (), ()]

    new_list = []  # 创建一个空列表
    for data in json_data:  # data 为字典 数据
        a = tuple(data.values())  # 取 字典的 values 部分，组成元组
        new_list.append(a[1:])  # 剔除 desc 这个 key 对应的 value，将剩余内容，存入空列表

    return new_list  # 循环结束，将 装满 元组的列表 [(), (), ()] 返回


class TestLogin(unittest.TestCase):
    @parameterized.expand(build_data())
    def test_login(self, username, pwd, code, expect):
        ret = login(username, pwd)
        self.assertEqual(expect, ret)

    # def test01_username_pwd_right(self):
    #     """正确用户名和密码"""
    #     ret = login('admin', '123456')
    #     self.assertEqual('登录成功', ret)
    #
    # def test02_username_error(self):
    #     """错误用户名"""
    #     ret = login('root', '123456')
    #     self.assertEqual('登录失败', ret)
    #
    # def test03_pwd_error(self):
    #     """错误密码"""
    #     ret = login('admin', '123123')
    #     self.assertEqual('登录失败', ret)
    #
    # def test04_username_pwd_error(self):
    #     """错误用户名和错误密码"""
    #     ret = login('aaa', '1231123')
    #     self.assertEqual('登录失败', ret)
