import redis

r = redis.Redis(password='123456')

# 模拟将任务放到队列中
# 任务类别_发件人_收件人_内容
task = '%s_%s_%s_%s' % ('sendEmail', 'lvze@163.com', 'tedu@163.com', 'miss lvze')
# 将任务发送到队列中
r.lpush('pylt1', task)
