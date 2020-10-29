import os
from multiprocessing import Pool, Queue

# print(os.listdir("."))
# 创建消息队列对象
q = Queue()

def copy_file(filepath, dir):
    new_name = dir + filepath.split("/")[-1]
    file = open(filepath, "rb")
    new_file = open(new_name, "wb")

    file_size = os.path.getsize(filepath)

    while file_size >= 1024:
        new_file.write(file.read(1024))
        q.put(1024)
        print("hei")
        print(q.empty())
        file_size -= 1024

    new_file.write(file.read(file_size))
    q.put(file_size)

# 创建进程池
pool = Pool()
# 文件目录
dir = "copyday12/"
os.mkdir(dir)
# 要复制的文件列表
filepath_list = ["day12/" + filename for filename in os.listdir("day12")]
# 要复制的文件总大小
total_file_size = 0
for filepath in filepath_list:
    total_file_size += os.path.getsize(filepath)
print(total_file_size)
# 向进程池队列添加事件
for filepath in filepath_list:
    pool.apply_async(func=copy_file, args=(filepath, dir))

current_file_size = 0
while True:
    print("进度: %f%%" % (current_file_size / total_file_size * 100))
    if current_file_size >= total_file_size:
        break
    print(q.empty())
    current_file_size += q.get()
    print(current_file_size)

pool.close()
pool.join()