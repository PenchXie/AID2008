"""
    返回字符串中第一个不重复的字符
"""


def get_single_char(string):
    for i in range(len(string)):
        # if string[i] not in string[i + 1 :]:
        #     return string[i]
        if string.count(string[i]) == 1:
            return string[i]


print(get_single_char('dabababcab'))