import os
import sys
from multiprocessing import Process
from time import sleep


def func01():
    sleep(2)
    print("func01执行喽")
    print(os.getppid(), "->", os.getpid())
def func02():
    sleep(4)
    print("func02执行喽")
    print(os.getppid(), "->", os.getpid())
def func03():
    sys.exit("func03进程退出啦")
    sleep(3)
    print("func03执行喽")
    print(os.getppid(), "->", os.getpid())

funcs_list = [func01, func02, func03]
jobs = []
# 循环创建进程
for func in funcs_list:
    p = Process(target=func)
    jobs.append(p)
    p.start()

for job in jobs:
    job.join()