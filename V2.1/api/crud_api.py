class MyCRUD:

    @classmethod
    def add_user(cls,session,datas):
        return session.get('http://localhost:3333/api/createUser',params=datas)
