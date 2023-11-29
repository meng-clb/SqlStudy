from pymongo import MongoClient

# 连接到本地数据库
conn = MongoClient('localhost')
db = conn.meng

# 修改一条数据
# data = db.meng.update_one({'name': 'zz'}, {'$set': {'age': 24}})
# print(data.modified_count)  # 修改数据的数量

# 修改多条数据
data = db.meng.update_many({}, {'$inc': {'age': 3}})  # $inc 累加数据
print(data.modified_count)
