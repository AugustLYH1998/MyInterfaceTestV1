
class TpshopLoginApi(object):
    # 发送验证码请求
    @classmethod
    def get_verify(cls, session):
        session.get(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.21519623710645064")

    # 发送登录请求
    @classmethod
    def login(cls, session, login_data):
        resp = session.post(
            url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
            data=login_data)
        return resp
