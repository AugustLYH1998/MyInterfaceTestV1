# 请求封装;统一发送请求

import requests

class RequestUtils:

    req = requests.session()

    def all_req(self,**args):
        return RequestUtils.req.request(**args)