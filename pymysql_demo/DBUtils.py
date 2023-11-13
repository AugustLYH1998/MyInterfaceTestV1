import yaml
import pymysql

# 封装数据库工具类
class DBUtils:

    with open('./conf.yaml', encoding="utf-8", mode='r') as file:
        rs = yaml.load(file, yaml.FullLoader)
        host = rs['host']
        port = rs['port']
        user = rs['user']
        password = rs['password']
        database = rs['database']
        charset = rs['charset']

    cursor = None
    my_conn = None

    @classmethod
    def __get_connect(cls):
        if cls.my_conn is None:
            cls.my_conn = pymysql.connect(host=cls.host, port=cls.port, user=cls.user,password=cls.password, database=cls.database, charset=cls.charset)
            return cls.my_conn

    @classmethod
    def close_connect(cls):
        if cls.my_conn is not None:
            cls.my_conn.close()
            cls.my_conn = None

    # 查
    @classmethod
    def my_select(cls, sql):
        try:
            my_conn = cls.__get_connect()
            # 3. 获取游标
            cursor = my_conn.cursor()
            # 4. 执行 sql 语句（查询）
            cursor.execute(sql)
            rs = cursor.fetchall()
            return rs

        except Exception as err:
            print("错误：", str(err))
        finally:
            # 6. 关闭游标
            cursor.close()
            # 7. 关闭连接
            # my_conn.close()
            cls.close_connect()

    #增删改 
    @classmethod
    def my_crud(cls, sql):
        try:
            my_conn = cls.__get_connect()
            # 3. 获取游标
            cursor = my_conn.cursor()

            # 4. 执行 sql 语句（查询）
            cursor.execute(sql)
            # 查看 sql执行，影响多少行
            print("影响的行数：", my_conn.affected_rows())

            # 5. 提交事务
            my_conn.commit()

        except Exception as err:
            print("错误：", str(err))
            # 回滚事务
            my_conn.rollback()
        finally:
            # 6. 关闭游标
            cursor.close()
            # 7. 关闭连接
            # my_conn.close()
            cls.close_connect()


if __name__ == '__main__':
    rs = DBUtils.my_crud('insert into `c`(id) values(175)')
    print(rs)
    rs = DBUtils.my_select('select * from `c`')
    print(rs)
