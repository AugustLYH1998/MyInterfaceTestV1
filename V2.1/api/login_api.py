
class LoginApi:

    @classmethod
    def login(cls,session, datas):
        print(datas)
        return session.post(url='http://localhost:3333/api/login', json=datas)
