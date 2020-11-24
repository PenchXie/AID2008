import redis

r = redis.Redis(password='123456')
while True:
    task = r.brpop('pylt1', 10)
    # (b'pylt1', b'sendEmail_lvze@163.com_tedu@163.com_miss lvze')
    print(task)
    if task:
        task_data = task[1]
        task_str = task_data.decode()
        task_list = task_str.split('_')
        print('-收到任务, 任务类型是:%s-' % task_list[0])
        # 执行发送邮件的任务
    else:
        print('-no task!!!-')
