def func01(p1, p2):
    p1 = "孙悟空"
    p2["八戒"] += 50
a = "悟空"
b = {"八戒": 100}
func01(a, b)
print(a) # ?
print(b) # ?


def func01(p1, p2):
    p1 = [100, 200]
    p2[:] = [300, 400]


a = [10, 20]
b = [30, 40]
func01(a, b)
print(a)  # ?
print(b)  # ?

# list01 = list(range(10))
# list02 = list01[5:]
# print(list01)
# print(list02)
# list01[8] = 10
# print(list01)
# print(list02)