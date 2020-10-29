from threading import Thread
from time import sleep


# 含有参数的线程函数
def func(sec, name):
    print("含有参数的线程函数")
    sleep(sec)
    print("%s线程执行完成" % name)


# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=func, args=(2,), kwargs={"name": "T%d" % i})
    jobs.append(t)
    t.start()

# 回收线程
[i.join() for i in jobs]
