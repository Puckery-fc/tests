# -*- coding: utf-8 -*-
# File  : connect.py
# # Date  : 2018/9/20

import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "678268",charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print ("Database version : %s " % data)
db.close()
#
# import pymysql  # 导入 pymysql
#
# # 打开数据库连接
# db = pymysql.connect(host = "localhost", user = "root",
#                      password = "678268",  port = 3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
# sql = "select * from USER"
# try:
#     cur.execute(sql)  # 执行sql语句
#
#     results = cur.fetchall()  # 获取查询的所有记录
#     print("id", "name", "password")
#     # 遍历结果
#     for row in results:
#         id = row[0]
#         name = row[1]
#         password = row[2]
#         print(id, name, password)
# except Exception as e:
#     raise e
# finally:
#     db.close()  # 关闭连接