from py07_数据库工具类封装 import DBUtil

res = DBUtil.select_one("select * from t_book;")
print(res)

DBUtil.uid_db('delete from t_book where id = 1111;')