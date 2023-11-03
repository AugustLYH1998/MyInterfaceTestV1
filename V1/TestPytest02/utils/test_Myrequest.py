import requests
class TestCommen:
    req = requests.session()

    def api_req(self,**args):
        return TestCommen.req.request(**args)