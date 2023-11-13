"""
新增一条图书数据（id:5 title:西游记 pub_date:1986-01-01 ）
insert into t_book(id, title, pub_date) values(5, '西游记', '1986-01-01');
1. 导包
2. 创建连接
3. 获取游标
4. 执行 insert 语句
5. 提交/回滚事务
6. 关闭游标
7. 关闭连接
"""

# 1. 导包
import pymysql

# 定义全局变量
conn = None
cursor = None

try:
    # 2. 创建连接
    conn = pymysql.connect(host="211.103.136.244", port=7061, user="student", password="iHRM_student_2021",
                           database="test_db", charset="utf8")
    # 3. 获取游标
    cursor = conn.cursor()

    # 4. 执行 insert 语句
    cursor.execute("insert into t_book(id, title, pub_date) values(175, '西游记', '1986-01-01');")

    # 查看 sql执行，影响多少行
    print("影响的行数：", conn.affected_rows())

    # 5. 提交事务
    conn.commit()

except Exception as err:
    print("插入数据错误：", str(err))
    # 回滚事务
    conn.rollback()

finally:
    # 6. 关闭游标
    cursor.close()
    # 7. 关闭连接
    conn.close()
