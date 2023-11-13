# 1. 导包
import pymysql

# 2. 建立连接
conn = pymysql.connect(host="211.103.136.244", port=7061, user="student",
                       password="iHRM_student_2021", database="test_db", charset="utf8")

# 3. 获取游标
cursor = conn.cursor()

# 4. 执行 sql 语句（查询）
cursor.execute("select version()")

# 5. 获取结果
res = cursor.fetchone()
print("res =", res[0])

# 6. 关闭游标
cursor.close()

# 7. 关闭连接
conn.close()
