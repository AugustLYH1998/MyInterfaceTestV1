"""
基础服务类：创建 dubboclient 实例
"""
from dubboclient import DubboClient


class BaseService(object):
    def __init__(self):
        self.dubbo_client = DubboClient("211.103.136.244", 6502)