# MyPython

pylance python autopep8

=============================================
# requests库
pip install requests
=============================================

pytest库
- 模块名必须用test开头或者_test结尾
- 类名必须以Test开头，不能有init方法
- 用例方法必须以test开头

插件：
```
pytest
pytest-html 简单的html报告
pytest-xdist 多线程执行
pytest-ordering 控制用例的执行顺序
pytest-rerunfailures 失败用例重跑
pytest-base-url 设置基础路径
allure-pytest 生成allure报告

pip install -r requirement.txt
-r 指定一个文本文件
```
运行方式
## 命令行执行:
```
pytest

pytest -vs  命令行显式输出
-v详细输出  -s输出调试信息

```
## pytest的主入口
根路径创建run.py
```python
# pytest的主入口
import pytest

if __name__ == '__main__':
    pytest.main()
```

## pytest配置文件ini
根路径创建pytest.ini

```
[pytest]
addopts = -vs
# addopts = -vs --html=./test-reports/reports.html --reruns 2
# addopts = -vs -m smoke

# target path
testpaths = ./02TestPytest

# default model rules
#python_files = xxx_*.py
#python_classes = xxx*
#python_function = xxx*

# baseurl
base_url = http://localhost:3333/api

# mark
markers = 
    smoke:冒烟测试用例

# 生成报告 失败两次rerun
addopts = -vs --html=./test-reports/reports.html --reruns 2
```
```python
# 冒烟测试用例
    @pytest.mark.smoke
    def testmark(self):
        print('hello smoke')
```

## @pytest.fixture()
@pytest.fixture是Python中pytest测试框架的一个功能，它可以让你定义一些设置代码，这些代码可以被多个测试用例共享。

- scope：控制fixture的生命周期。可选的值有"function"（默认值，每个测试函数都会调用一次fixture），"class"（每个测试类调用一次fixture），"module"（每个模块调用一次fixture），"session"（整个测试会话只调用一次fixture）。
- params：一个可迭代的对象，它的元素会依次传递给fixture函数的参数。每次传递一个参数，都会运行一次fixture函数，然后运行一次测试函数。
- autouse：如果设置为True，那么所有的测试函数都会自动使用这个fixture，即使测试函数没有明确地接收这个fixture作为参数。
- ids：参数别名；一个可迭代的对象，用于给params参数提供的每个值指定一个ID。这些ID会出现在测试报告中。
- name：fixture的名字。默认情况下，fixture的名字就是函数的名字，但你可以通过这个参数改变它。

```python
import pytest

@pytest.fixture(scope="module", params=[0, 1], autouse=True, ids=['zero_data1', 'one_data2'], name="my_fixture")
def example_data(request):
    return request.param
    # 参数request和request.param是固定写法

def test_example(my_fixture):
    print(my_fixture)
    assert my_fixture in [0, 1]
```
在这个例子中，test_example会运行两次，第一次my_fixture的值是0，第二次my_fixture的值是1。

## conftest.py
fixture的scope ='class' 时，如果要不同的class都起作用，要使用conftest.py
在根目录创建一个 conftest.py，放入装饰器

```python
# conftest使所有文件的scope对应的内容查询都生效
import pytest
# 装饰器
@pytest.fixture(scope='class', autouse=True)
def exe_sql():
    print('请求查询数据库')
```
=============================================

# 接口自动化框架封装：通过文件保存中间变量
项目根目录创建extract.yaml，用来存储变量
创建一个yaml工具类进行读写操作
```python
import os
import yaml

filePath = os.path.join(os.path.dirname(__file__), '..', 'extract.yaml')
# 写入
# 将data写入yaml文件
def write_yaml(data):
    with open(filePath, encoding="utf-8", mode="a+") as f:
        # yaml.dump将python对象转换为yaml字符串
        print('data:',data)
        yaml.dump(data, stream=f, allow_unicode=True)
        f.close()

# 读取
def read_yaml(key):
    with open(filePath, encoding="utf-8", mode="r") as f:
        # yaml.dump将python对象转换为yaml字符串
        result =  yaml.load(f,yaml.FullLoader)
        return result[key]
        # yaml.load() 函数用于将 YAML 数据从文件或字符串中加载为 Python 对象。它接受两个参数
        # yaml.FullLoader：是一个加载器类，用于指定加载 YAML 数据时的解析器

# 清空yaml
def clear_yaml():
    with open(filePath, encoding="utf-8", mode="w") as f:
        f.truncate()

```

```python
# 请求测试
import requests
from yaml_utils import write_yaml, read_yaml

class TestApi:
    # 将变量保存到 yaml中
    def test_get_token(self):
        url = 'http://localhost:3333/api/access_token'
        data = {
            'grant_type': '1',
            'secret': '1',
            'appid': '1'
        }
        response = requests.get(url, params=data)
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
```
避免每次请求造成数据重复积累到文件中，需要清空
配置一个session的 fixture,在请求前使用
```python
import pytest
from TestPackage03.yaml_utils import clear_yaml

@pytest.fixture(scope='session', autouse=True)
# request参数名固定
def exe_clearYAML():
    # 请求前清空
    clear_yaml()
    yield
    # 请求后清空
    # clear_yaml()
```

## 补充os读写文件
```python
在Python的open()函数中，mode参数用于指定文件打开的模式。下面是一些常见的mode值及其含义：

"r"：只读模式（默认）。打开文件以供读取，如果文件不存在则会引发错误。
"w"：写入模式。打开文件以进行写入，如果文件存在，则会截断文件内容；如果文件不存在，则会创建一个新文件。
"x"：独占创建模式。创建一个新文件，如果文件已经存在，则会引发错误。
"a"：追加模式。打开文件以进行写入，在文件末尾追加内容，如果文件不存在，则会创建一个新文件。
"b"：二进制模式。以二进制格式打开文件。
"t"：文本模式（默认）。以文本格式打开文件。
"+"：读写模式。同时支持读取和写入操作。
这些模式可以组合使用，例如"rb"表示以二进制模式打开文件进行只读操作，"w+"表示以读写模式打开文件。
```

# 数据业务分离
## yaml是一种数据类型，比如json
python中使用yaml，引用的是pyYAML库
```yml
# 配置文件示例
# map对象
database:
  host: localhost
  port: 3306
  username: myuser
  password: mypassword

server:
  port: 8080
  debug: true

# list对象
- name1: test111
- name2: test222
- name3: test333
```

## pytest数据驱动的装饰器
@pytest.mark.parametrize() 是一个装饰器，用于在pytest测试中传递参数化测试数据。
它允许你通过多个参数组合来运行同一个测试函数，从而减少重复代码和提高测试效率。
```python
@pytest.mark.parametrize() 的参数包括：
参数名称：是一个字符串，表示将要传递的参数名称。
参数值：是一个列表或元组，其中包含一个或多个参数值组合。每个参数值组合都应该是一个单独的元组或列表，其中包含要传递给测试函数的参数值。
选项：是一个可选字典，用于指定参数化测试的一些选项，如ids（为每个测试生成自定义标识符）。
```

### 封装参数
test_get_token.yaml
```yaml
# yaml 模拟一个用例
# 自定义名称
# -
#   model: 模块
#   interface: 接口
#   title: 用例标题
#   request: 
#     method: 请求方式
#     url: 请求路径
#     params: 参数
#     # data: 
#     # json: 
#     # header
#   # validate: null 断言
#   validate: null 断言
-
  model: 模块1
  interface: 接口1
  title: 获取access_token
  request: 
    method: get
    url: http://localhost:3333/api/access_token
    params: 
            grant_type: 1
            secret: 1
            appid: 1
    # data: 
    # json: 
    # header
  # validate: null 断言
  validate: null

# 每个都是一个用例
-
  model: 模块2
  interface: 接口1
  title: 获取access_token
  request: 
    method: get
    url: http://localhost:3333/api/access_token
    params: 
            grant_type: 1
            secret: 1
            appid: 1
    # data: 
    # json: 
    # header
  # validate: null 断言
  validate: null
```

py
```python
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
        print(yaml_conf)
        data = yaml_conf['request']['params']
        print(yaml_conf)
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

    # @pytest.mark.packagetest
    # @pytest.mark.parametrize('yaml_conf', read_testcase(yaml_path))
    # def test_get(self,yaml_conf):
    #     url = yaml_conf['request']['url']+'/any'
    #     # 读出
    #     datas = read_yaml('access_token')
    #     response = requests.get(url, params=datas)
    #     print(list(response.json())[0])
```

yaml_utils.py
```python
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
```

## yaml处理python函数
```python
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
```

```yaml
# 读取用例
-
  model: 模块1
  interface: 接口1
  title: 打印access_token
  request: 
    method: get
    url: http://localhost:3333/api/any
    params: 
      access_token: access_token
  validate: null
```
utils
```python
import os
import yaml

filePath = os.path.join(os.path.dirname(__file__), '..', 'extract.yaml')

# 读取
def read_yaml(key):
    with open(filePath, encoding="utf-8", mode="r") as f:
        # yaml.dump将python对象转换为yaml字符串
        result = yaml.load(f, yaml.FullLoader)
        return result[key]

```

## 文件上传
py
```python
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
```

test_uploadfiles.yaml
```python
-
  model: 模块1
  interface: 接口1
  title: 文件上传
  request: 
    method: post
    url: http://localhost:3333/api/upload
    params: null
    files:
      media: 'E:\test\Interface\TestRequests01\1.txt'
  validate: null

```

# allure报告
1、安装allure
2、执行ini
[pytest]
addopts = -vs -m packagetest --alluredir=./result --clean-alluredir
3、生成html报告
```python
# pytest的主入口
import os
import time
import pytest

if __name__ == '__main__':
    pytest.main()

    time.sleep(3)
    os.system('allure generate ./result -o ./test-reports --clean')
```
4、浏览器打开
```shell
allure open test-reports/
```