import logging
import os
import pytest
import requests

from utils.DBUtils import DBUtils
from utils.logging_use import init_log_config

# 初始化日志
@pytest.fixture(scope='session',autouse=True)
def log_init():
    filename = os.path.dirname(__file__)+'\\logging\\test.log'
    # 初始化日志
    init_log_config(filename)
    logging.debug(
        '=============================================log_init================================================')

@pytest.fixture(scope='class', autouse=True)
# 每个测试类（test class）中调用一次 fixture。适合那些需要在整个测试类范围内共享状态或资源的情况。
def get_init(request):
    # request.cls 来访问和设置测试类的属性
    logging.debug(
        '=============================================begin================================================')
    # 设置class的变量session
    request.cls.session = requests.Session().request
    
    # 设置class的base_url
    # request.cls.BASE_URL = request.config.getoption('base_url')

    yield
    # 请求后
    logging.debug(
        '=============================================end================================================')

# crud
@pytest.fixture(scope='function', autouse=False)
def delete_test(yaml_conf):
    # logging.debug(f'前：{yaml_conf}')
    TEL = yaml_conf['request']['params']['phonenumber']
    DBUtils.my_crud(f'delete from `c` where `phonenumber`={TEL}')
    yield
    # logging.debug(f'后：{yaml_conf}')
    DBUtils.my_crud(f'delete from `c` where `phonenumber`={TEL}')
