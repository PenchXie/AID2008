"""
    根据父母身高预测孩子身高
"""
# get the father and mother's heights
father_height = float(input("Enter father's height:"))
mother_height = float(input("Enter mother's height:"))

# calculate the child's height
child_height = (father_height + mother_height) * 0.54

# print the child's height
print("Child's height:" + str(child_height))