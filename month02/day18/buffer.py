"""
缓冲区
"""

f = open('file.txt', 'wb', buffering=3)

while True:
    print("hello world")
    data = input("Enter:") + "\n"
    if not data:
        break
    f.write(data.encode())

f.close()