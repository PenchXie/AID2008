from threading import Thread

def spider():
    print('正在请求 解析 处理数据中')

t_list = []
for i in range(5):
    t = Thread(target=spider)
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()