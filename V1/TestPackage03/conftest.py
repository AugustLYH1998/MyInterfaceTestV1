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