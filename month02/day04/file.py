"""
os模块　文件处理小函数
"""
import os

# 获取文件大小 bytes
print(os.path.getsize('../day03/my.log'))

# 获取目录下的内容
print(os.listdir('..'))

# 判断文件是否存在　True False
print(os.path.exists('1.txt'))

# 判断一个文件是否为普通文件
print(os.path.isfile('..'))

# 删除文件
os.remove('../day03/time.txt')