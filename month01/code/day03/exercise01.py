"""
    逻辑运算符练习
"""
# # input age and height
# age = int(input("Age:"))
age = int(input("Age:")) > 25
# height = int(input("Height:"))
height = int(input("Height:")) < 170


# print
# print(age > 25 and height < 170)
print(age and height)

# input position and salary
position = input("Position:")
salary = int(input("Yearly salary:"))

# print
print(position == "高管" or salary > 500000)