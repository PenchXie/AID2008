import redis

# 创建redis对象, 连接之前确定连接哪个库, 进入之后不能再修改
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

# 遍历所有的键
key_list = r.keys('*')
# 从函数中拿到的结果一般是字节串
print(key_list)
print(r.exists('k1'))
print(r.exists('lk1'))
print(r.type('lk1'))
r.set('name', 'lvze', 100)
print(r.get('name'))
# 设置获取多个值
r.mset({'a': 100, 'b': 200, 'c': 300})
print(r.mget('a', 'b', 'c'))
# 列表操作
r.delete('pyl1')
# 从头部添加
r.lpush('pyl1', 'a', 'b', 'c', 'd', 'e')
print(r.lrange('pyl1', 0, -1))
# 从尾部弹出元素
r.rpop('pyl1')
print(r.lrange('pyl1', 0, -1))