from pymongo import MongoClient

# 连接到本地数据库
conn = MongoClient('localhost')
db = conn.meng

# 删除一条数据
# data = db.meng.delete_one({'name': 'zz'})
# print(data.deleted_count)  # 删除数据的数量

# 删除多条数据
data = db.meng.delete_many({'age': {'$lt': 30}})
print(data.deleted_count)  # 删除数据的数量

# 删除整个文档
db.meng.drop()
