"""
正则表达式　re  示例
"""
import re

# 目标字符串
s = "Alex:1996,Sunny:1997"
pattern = r"(?P<name>\w+):(\d+)"

# 匹配到的内容形成一个可迭代的对象
result = re.finditer(pattern, s)
# 每次迭代取出一处内容
for i in result:
    print("匹配内容对应位置:", i.span())
    print("匹配到的内容:", i.group())  # i为match对象

# 匹配目标字符串, 必须在开始位置
result = re.match(pattern, s)
print(result.group())

# 匹配目标字符串, 只匹配第一处
result = re.search(pattern, s)
print(result.group())
# 获取捕获组名为键, 对应内容为值的字典, 如没有组名则字典为空
print(result.groupdict())