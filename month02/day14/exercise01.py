"""
模拟一个售票系统程序
一共500张票 --> T1---T500
编写10个线程模拟10个售票窗口机器 记为　W1-W10
10个窗口同时售票直到所有票都卖出为止
票按照顺序出售
每个窗口卖出一张后  W2----T346
卖出一张需要0.1s
"""

from threading import Thread
from time import sleep

tickets = ["T%d" % i for i in range(1, 501)]
print(tickets)

def sell_ticket(window):
    # while len(tickets) > 0:
    while tickets:
        # ticket = tickets.pop(0)
        # print("Sell ticket: %s- ---%s" % (window, ticket))
        print("Sell ticket: %s- ---%s" % (window, tickets.pop(0)))
        sleep(0.1)

jobs = []
for i in range(1, 11):
    t = Thread(target=sell_ticket, args=("W%d" % i,))
    jobs.append(t)
    t.start()

for t in jobs:
    t.join()
