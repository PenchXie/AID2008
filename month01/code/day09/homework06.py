"""
    根据每人的金条数量,对字典进行升序排列
"""
dict01 = {"金海": 32, "徐天": 15, "田丹": 0, "柳如丝": 500, "铁林": 20}

temp_list = [(key, value) for key, value in dict01.items()]

for i in range(len(temp_list) - 1):
    for j in range(i + 1, len(temp_list)):
        if temp_list[i][1] > temp_list[j][1]:
            temp_list[i], temp_list[j] = temp_list[j], temp_list[i]

dict01 = dict(temp_list)
print(dict01)
