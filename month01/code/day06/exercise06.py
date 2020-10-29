"""
    集合练习
"""
# 创建字典
positions = {
    '经理': {'曹操', '刘备', '孙权'},
    '技术': {'曹操', '刘备', '张飞', '关羽'}
}
# 是经理也是技术
print(positions['经理'] & positions['技术'])
# 是经理不是技术
print(positions['经理'] - positions['技术'])
# 不是经理是技术
print(positions['技术'] - positions['经理'])
# 身兼一职
print(positions['经理'] ^ positions['技术'])
# 公司总共有多少人数
print(len(positions['经理'] | positions['技术']))