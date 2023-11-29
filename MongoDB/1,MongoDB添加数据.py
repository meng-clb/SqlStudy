from pymongo import MongoClient

# 需要先开启本地服务, 使用电脑终端开始MongoDB服务
# mongod.exe --dbpath=(数据库存储的路径)
# mongod.exe --dbpath = C:\Users\clb14\Desktop\mongodb

# 连接本地MongoDB
conn = MongoClient('localhost')

# 选择数据库
db = conn.meng

# 插入一条数据
# data = db.meng.insert_one({'name': 'zz', 'age': 13, 'sex': 'man'})
# 返回插入数据的id
# print(data.inserted_id)

# 插入多条数据
data = db.meng.insert_many(
	[{'name': 'ew', 'age': 34, 'sex': 'men'},
	 {'name': 'as', 'age': 44, 'sex': 'man'},
	 {'name': 'ga', 'age': 14, 'sex': 'man'},
	 {'name': 'hw', 'age': 54, 'sex': 'men'}])
# 返回插入数据的id
print(data.inserted_ids)