"""
    占位符练习
"""
confirmed = 67802
cure = 63326
message = "湖北确诊%d人, 治愈%d人, 治愈率%.2f" % (confirmed, cure, cure / confirmed)
print(message)