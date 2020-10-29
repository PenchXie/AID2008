"""
创建两个线程同时执行
一个线程负责打印1---52  52个数字
另一个线程打印A--Z  26个字母
要求打印结果为 12A34B...5152Z
"""
from threading import Thread, Event

e1 = Event()
e2 = Event()

def print_num(num, step):
    for i in range(1, num + 1, step):
        print(i, end="")
        print(i + 1, end="")
        e2.set()
        e1.clear()
        e1.wait()

# A:65
def print_letter():
    for i in range(65, 91):
        e2.wait()
        print(chr(i), end="")
        e2.clear()
        e1.set()


t1 = Thread(target=print_num, args=(52, 2))
t2 = Thread(target=print_letter)

t1.start()
t2.start()
t1.join()
t2.join()