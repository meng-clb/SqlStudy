from pymongo import MongoClient

# 连接到本地数据库
conn = MongoClient('localhost')
db = conn.meng

# 查询所有
data = db.meng.find()
print(data)  # 返回一个游标对象, 使用迭代获取数据
for i in data:
	print(i)

# 查询所有的男性
print('--------------根据条件查找----------------')
data = db.meng.find({'sex': 'man'}, {'_id': 0, 'name': 1, 'age': 1})
for i in data:
	print(i)

print('--------------根据条件排序----------------')
data = db.meng.find({'sex': 'man'}, {'_id': 0, 'name': 1, 'age': 1}).sort({'age': -1})
for i in data:
	print(i)

# # 查询数据条数
# num = db.meng.find().count()
# print(num)
