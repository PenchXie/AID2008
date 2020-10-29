"""
    if选择语句练习、调试
"""
# 输入阶段数，显示课程名称
stage = input("请输入阶段数：")

# 根据阶段显示课程名称
if stage == "1":
    print("Python语言核心课程")
elif stage == "2":
    print("Python高级软件技术")
elif stage == "3":
    print("Web全栈")
elif stage == "4":
    print("网络爬虫")
elif stage == "5":
    print("数据分析、人工智能")
else:
    print("不正确的阶段数")