"""
编写一个函数, 传入一个文件夹, 删除掉该文件夹中　小于　100kb的普通文件
"""
import os

def del_lt_100b_file(directory):
    file_list = os.listdir(directory)
    for file_name in file_list:
        if os.path.isfile(f"{directory}/{file_name}") and \
            os.path.getsize(f"{directory}/{file_name}") < 1024:
            os.remove(f"{directory}/{file_name}")

if __name__ == '__main__':
    del_lt_100b_file('../exercise')

