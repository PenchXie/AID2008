"""
    列表字符串转换练习, 列表-->字符串
"""
# 初始化字符串列表
strings = []
# 输入字符串
while True:
    string = input("请输入内容：")
    if not string:
        break
    strings.append(string)

print("_".join(strings))

