import csv

# windows系统下需要加上newline=''属性, 否则得到表格数据行与行之间会有空行
with open('lvze.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['lvze', '菜逼'])
    writer.writerow(['步惊云', '绝世好剑'])
