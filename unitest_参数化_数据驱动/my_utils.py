class MyUtils:

    @classmethod
    def get_token(cls, myself):
        return myself.session.get(
            zurl='http://localhost:3333/api/access_token', params={'grant_type': 1, 'secret': 1, 'appid': 1}).json()['access_token']

    @classmethod
    def login(cls, myself,data):
        return myself.session.post(url=data['url'], data={'token': myself.token, 'username': 'admin', 'password': '123456'})

    @classmethod
    def common_assert(cls, myself, code, res):
        print(res.status_code)
        myself.assertEqual(code, res.status_code)
