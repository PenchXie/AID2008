"""
    列表字符串转换练习, 字符串-->列表
"""
# 初始语句
sentence = "To have a government that is of people by people for people"
# 将语句中的单词存储至列表
words = sentence.split(" ")
# 将列表反向连接成字符串
print(" ".join(words[::-1]))