# conftest使所有文件的scope对应的内容查询都生效
import pytest

# 装饰器
@pytest.fixture(scope='function', autouse=False, params=[['pyhton','javascript'],['hello,world']])
# request参数名固定
def exe_sql(request):
    print('请求查询数据库')
    yield request.param
    print('请求完毕')