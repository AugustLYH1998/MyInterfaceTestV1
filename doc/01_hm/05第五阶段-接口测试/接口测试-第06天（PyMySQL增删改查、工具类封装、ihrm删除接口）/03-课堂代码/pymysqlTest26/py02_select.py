# 1. 导包
import pymysql

# 2. 建立连接
conn = pymysql.connect(host="211.103.136.244", port=7061, user="student",
                       password="iHRM_student_2021", database="test_db", charset="utf8")

# 3. 获取游标
cursor = conn.cursor()  # 指向 0 号位置。

# 4. 执行 sql 语句（查询）--- t_book
cursor.execute("select * from t_book;")

# 5. 获取结果 - 提取第一条
res1 = cursor.fetchone()
print("res1 =", res1)

# 修改游标位置：回零
cursor.rownumber = 0

# 5. 获取结果 - 提取前 2 条
res2 = cursor.fetchmany(2)
print("res2 =", res2)

# 修改游标位置：回零
cursor.rownumber = 0
res3 = cursor.fetchall()
print("res3 =", res3)


# 修改游标位置：指向第 2 条记录
cursor.rownumber = 2
res4 = cursor.fetchmany(2)
print("res4 =", res4)

# 6. 关闭游标
cursor.close()

# 7. 关闭连接
conn.close()
