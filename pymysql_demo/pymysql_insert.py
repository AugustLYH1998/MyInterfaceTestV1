# 插入数据：
import pymysql
import yaml

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

try:
    my_conn = pymysql.connect(host=host, port=port, user=user,
                              password=password, database=database, charset=charset)
    # 3. 获取游标
    cursor = my_conn.cursor()

    # 4. 执行 sql 语句（查询）
    cursor.execute("insert into c(id) values(175)")
    # 查看 sql执行，影响多少行
    print("影响的行数：", my_conn.affected_rows())

    # 5. 提交事务
    my_conn.commit()

except Exception as err:
    print("插入数据错误：", str(err))
    # 回滚事务
    my_conn.rollback()
finally:
    # 6. 关闭游标
    cursor.close()
    # 7. 关闭连接
    my_conn.close()
