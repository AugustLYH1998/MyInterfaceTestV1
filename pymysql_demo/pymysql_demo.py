""" 
1. 导包 import pymysql
2. 创建连接。 conn = pymysql.connect(host，port, user, password, database, charset)
3. 获取游标。 cursor = conn.cursor()
4. 执行 SQL。 cursor.execute( 'sql语句')

查询语句（select）
处理结果集（提取数据 fetch*）
增删改语句（insert、update、delete）
成功：提交事务 conn.commit()
失败：回滚事务 conn.rollback()
5. 关闭游标。cursor.close()
6. 关闭连接。conn.close()

"""

""" 
==建立连接方法==
conn = pymysql.connect(host="", port=0, user="", password="", database="", charset="")
host：数据库所在主机 IP地址 - string
port：数据库使用的 端口号 - int
user：连接数据库使用的 用户名 - string
password：连接数据库使用的 密码 - string
database：要连接的那个数据库的名字 - string
charset：字符集。常用 utf8 - string
conn：连接数据库的对象。
"""
# 1. 导包
import pymysql
import yaml
# 2. 建立连接

with open('./conf.yaml', encoding="utf-8", mode='r') as file:
    rs = yaml.load(file, yaml.FullLoader)
    # print(rs) # {'host': 'localhost', 'port': 3306, 'user': 'root', 'password': '123456', 'database': 'test003', 'charset': 'utf8'}
    host = rs['host']
    port = rs['port']
    user = rs['user']
    password = rs['password']
    database = rs['database']
    charset = rs['charset']

cursor = None
my_conn = None

try:
    my_conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset=charset)

    # 3. 获取游标
    cursor = my_conn.cursor()

    # 4. 执行 sql 语句（查询）
    cursor.execute("select * from c")

    # 5. 获取结果
    """ 
    fetchone()：从结果集中，提取一行。
    fetchmany(size)：从结果集中，提取 size 行。
    fetchall()：提取所有结果集。
    属性rownumber：可以设置游标位置。
    """
    res = cursor.fetchone()
    print("res =", res)

    print(cursor.fetchone())
    # 修改游标位置：回零
    cursor.rownumber = 0
    print(cursor.fetchone())
    # 获取结果 - 提取前 2 条
    print(cursor.fetchmany(2))
    print(cursor.fetchone())

except Exception as err:
    print("查询语句执行出错:", str(err))
finally:
    # 6. 关闭游标
    cursor.close()
    # 7. 关闭连接
    my_conn.close()
