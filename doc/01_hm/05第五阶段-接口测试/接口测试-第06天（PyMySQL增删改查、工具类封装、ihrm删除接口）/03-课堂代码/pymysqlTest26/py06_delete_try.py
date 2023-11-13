"""
删除名称为‘西游记’的图书
delete from t_book where title = '西游记';

1. 导包
2. 建立连接
3. 获取游标
4. 执行 delete 语句
5. 提交、回滚事务
6. 关闭游标
7. 关闭连接
"""
# 1. 导包
import pymysql

conn = None
cursor = None

try:
    # 2. 建立连接
    conn = pymysql.connect(host="211.103.136.244", port=7061, user="student", password="iHRM_student_2021",
                           database="test_db", charset="utf8")
    # 3. 获取游标
    cursor = conn.cursor()

    # 4. 执行 delete语句。
    cursor.execute("delete from t_book where id = 151;")

    print("影响的行数：", conn.affected_rows())

    # 5. 提交、回滚事务
    conn.commit()

except Exception as err:
    print("更新失败：", str(err))
    # 回滚事务
    conn.rollback()

finally:
    # 6. 关闭游标
    cursor.close()
    # 7. 关闭连接
    conn.close()