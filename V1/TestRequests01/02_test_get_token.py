# 请求测试
import requests
import jsonpath
# jsonpath 在 JSON 数据中定位和提取特定数据
import re
import json

from commen.TestUntils import RequestUtils

class TestApi:
    # 类变量保存值
    access_token = ''

    def test_get_token(self):
        url = 'http://localhost:3333/api/access_token'
        data = {
            'grant_type': '1',
            'secret': '1',
            'appid': '1'
        }
        response = requests.get(url, params=data)
        token = response.json()

        # 提取access_token
        """ 
        $ 根节点
        . 子节点   $.access_token
        .. 递归取子节点
        [] 下标0开始 取历表中的值
         """
        rs = jsonpath.jsonpath(token, '$.access_token')
        # print(rs[0])
        TestApi.access_token = rs[0]

    # 使用上一个接口的结果作为参数
    def my_test(self):
        url = 'http://localhost:3333/api/any'
        data = {
            'token': TestApi.access_token
        }
        response = requests.get(url, params=data)
        print(response.json())

    # 测试post请求
    def test_post(self):
        url = 'http://localhost:3333/api/post'
        datas = {
            'TestApi.access_token': TestApi.access_token
        }
        response = requests.post(url, json=datas)
        print(response.json())

    # 文件上传
    def test_file(self):
        url = 'http://localhost:3333/api/upload'
        datas = {
            "media": open('E:\\test\\MyPython\\demo01\\1.txt', 'rb')
        }

        response = requests.post(url, files=datas)
        print(response)

    # 正则提取
    def test_search(self):
        url = 'http://localhost:3333/api/menus/build'
        response = requests.get(url)
        # print(response.json())
        # 正则匹配name
        """ 
        re.search()提取一个值，通过下标取值
        re.findall()提取多个值，通过下标取值
        """
        json_str = json.dumps(response.json())

        pattern = r'"name":\s*"(\w*)"'

        re_result = re.findall(pattern, json_str)
        # re中，group(1)是一个方法，用于获取匹配对象中第一个捕获组（capturing group）

        if re_result:
            print(re_result)
        else:
            print('未匹配到name字段')

    #  请求头
    """ 
    header={
    }
    response = requests.post(url, headers=header)
    """

    # 使用requests.session().request()
    def test_session(self):
        url = 'http://localhost:3333/api/'
        res = requests.session().request(method='get',url=url)
        # print(res.text)
        print(res.json())

    # 使用封装请求
    def test_utils(self):
        url = 'http://localhost:3333/api/'
        res = RequestUtils().all_req(method='get', url=url)
        # print(res.text)
        print(res.json())

if __name__ == '__main__':
    TestApi().test_get_token()
    # TestApi().my_test()
    # TestApi().test_post()
    # TestApi().test_file()
    # TestApi().test_search()
    # TestApi().test_session()
    TestApi().test_utils()
