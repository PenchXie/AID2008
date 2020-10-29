list01 = list(range(10))

iterator01 = list01.__iter__()

while True:
    try:
        print(iterator01.__next__())
    except StopIteration:
        break

dict01 = {
    1: 11,
    2: 22,
    3: 33,
}

# iterator02 = dict01.items().__iter__()
# while True:
#     try:
#         print(iterator02.__next__())
#     except StopIteration:
#         break

iterator02 = dict01.keys().__iter__()
while True:
    try:
        key = iterator02.__next__()
        print(key, dict01[key])
    except StopIteration:
        break