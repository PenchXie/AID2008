"""
自定义线程类
"""
import time
from threading import Thread

class MyThread(Thread):
    def __init__(self, song):
        self.song = song
        super().__init__() # 加载父类方法

    def run(self) -> None:
        for i in range(3):
            print("playing %s:%s" % (self.song, time.ctime()))
            time.sleep(2)

t = MyThread("凉凉")
t.start() # 运行run方法, 作为一个线程执行
t.join()