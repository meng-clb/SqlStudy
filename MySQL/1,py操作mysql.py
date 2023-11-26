import pymysql

# 连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='meng')
# 设置字符编码
db.set_charset('utf8')
# 创建游标对象, 用于执行sql语句
cursor = db.cursor()

# sql语句执行
# 查询
sql = 'select * from user'
# 执行sql语句
cursor.execute(sql)
# 获取数据库中的内容
# 获取所有, 返回元组形式
# print(cursor.fetchall())
# 获取一行数据
# print(cursor.fetchone())
# 获取几行数据
# print(cursor.fetchmany(3))
try:
	# 插入数据
	sql = 'insert into user values(null, "clb", 1, 21)'
	cursor.execute(sql)
	print(cursor.rowcount)  # 受影响的行数
	# 修改数据
	sql = 'update user set id=7 where name="clb"'
	cursor.execute(sql)
	# 执行sql查询语句
	sql = 'select * from user'
	cursor.execute(sql)
	print(cursor.fetchall())
	db.commit()  # 提交事务 -> 没有报错就提交到数据库
except:
	db.rollback()  # 回滚事务 -> 报错后回滚到输入指令之前
