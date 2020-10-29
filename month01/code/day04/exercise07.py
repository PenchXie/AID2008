"""
    编码练习, 循环录入编码值打印文字，知道录入空字符串停止
"""
# 循环
# while True:
#     number = input("请输入数字：")
#     if number:
#         print(chr(int(number)))
#     else:
#         break

# 更好的写法
while True:
    number = input("请输入数字：")
    if number == 0:
        break
    print(char(int(number)))