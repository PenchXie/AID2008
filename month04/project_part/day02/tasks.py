import time

from celery import Celery

# 1. 创建Celery对象, 并配置broker(消息队列)
app = Celery('demo1', broker='redis://@127.0.0.1:6379/1', backend='redis://@127.0.0.1:6379/2')


# 2. 创建任务函数
@app.task
def task_test(a):
    print('task is running...')
    time.sleep(10)
    print('task is finished')
    return a ** 2
