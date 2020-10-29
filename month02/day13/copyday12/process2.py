"""
含有参数的进程函数示例
"""

from multiprocessing.context import Process
from time import sleep
from signal import *


# 含有参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working")


# 位置传参args = ()
# p = Process(target=worker, args=(2, "Levi"))
signal(SIGCHLD, SIG_IGN)
# 关键字传参
p = Process(target=worker, kwargs={"name": "Tom", "sec": 2})
# p.daemon = True
p.start()
print("Name:", p.name)
print("PID:", p.pid)
print("is alive:", p.is_alive())
# p.join(3)  # 最多等待3秒
print("===========================")
while True:
    pass
