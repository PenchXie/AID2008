f = open('file.txt', 'wb+')

f.write(b"Fate Grand Order")
f.flush()

print(f.tell())
# 操控文件偏移量
f.seek(-10, 1)
f.write(b"R")
f.seek(0, 0)
data = f.read().decode()
print(data)

f.close()