"""
正则表达式　re  示例
"""

import re

s = "Alex:1996,Sunny:1997"
pattern = r"(\w+):(\d+)"

result = re.findall(pattern, s)
print(result)

result = re.split("\W+", s, 1)
print(result)

result = re.sub("\W+", "@", s, 1)
print(result)