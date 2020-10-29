import os
from multiprocessing import Process

def copy_half_1(filename: str):
    suffix = filename.split(".")[-1]
    new_name = "file1." + suffix
    file = open(filename, "rb")
    new_file = open(new_name, "wb")

    file_size = os.path.getsize(filename)

    copy_size = file_size // 2

    while copy_size > 1024:
        data = file.read(1024)
        new_file.write(data)
        copy_size -= 1024

    data = file.read(copy_size)
    new_file.write(data)

    file.close()
    new_file.close()

def copy_half_2(filename:str):
    suffix = filename.split(".")[-1]
    new_name = "file2." + suffix
    file = open(filename, "rb")
    new_file = open(new_name, "wb")

    file_size = os.path.getsize(filename)

    file.seek(file_size // 2)
    while True:
        data = file.read(1024)
        if not data:
            break
        new_file.write(data)

    file.close()
    new_file.close()

p1 = Process(target=copy_half_1,args=("timg.jpeg",))
p2 = Process(target=copy_half_2,args=("timg.jpeg",))

jobs_list = [p1, p2]

for job in jobs_list:
    job.start()

for job in jobs_list:
    job.join()