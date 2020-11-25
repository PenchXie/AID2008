import redis

r = redis.Redis(password='123456')

# '武将': '张飞', '周瑜', '赵云', '马超'
# '文臣':
r.sadd('commander', '张飞', '周瑜', '赵云', '马超')
r.sadd('officer', '诸葛亮', '司马懿', '周瑜', '荀彧')
# 纯武将
for item in r.sdiff('commander', 'officer'):
    print(item.decode())

print("======")
# 纯文臣
for item in r.sdiff('officer', 'commander'):
    print(item.decode())
print("======")
# 文物双全
for item in r.sinter('commander', 'officer'):
    print(item.decode())
print("======")
# 全部
for item in r.sunion('commander', 'officer'):
    print(item.decode())
