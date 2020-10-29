"""
多进程编程
"""
import multiprocessing as mp

# 进程的执行函数
from time import sleep

print("##############################")

a = 1


def func():
    print("func执行喽")
    global a
    print(a)
    a = 100
    print(a)
    sleep(3)
    print("func执行了3秒")


# 创建进程对象 绑定函数
p = mp.Process(target=func)

# 启动进程  这时进程产生, 进程执行func函数
p.start()
print("我这也执行了")
sleep(2)
print("2秒")
# 阻塞等待回收进程　将创建的进程资源释放
p.join()

print(a)
