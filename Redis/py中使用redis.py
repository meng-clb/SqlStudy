import redis

# 链接redis
# r = redis.StrictRedis(host='127.0.0.1', port=6379, password='root', decode_responses=True)
r = redis.StrictRedis(password='root', decode_responses=True)
'''
redis简单, 但是命令多, 配合参考手册食用
抓取的数据一般不存放到redis中
命令 -> redis参考手册: https://redis.com.cn/commands.html
'''

# 设置
# r.set('name', 'clb')
# print(r.get('name'))

# 批量设置
# r.mset({'name': 'lucky', 'age': 12, 'sex': 'man'})
# print(r.mget('name', 'age', 'sex'))

print(r.getset('name', 'love'))
