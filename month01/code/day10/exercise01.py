list01 = list(range(100))

while True:
    for num in list01:
        if num % 2:
            list01.remove(num)
            break #此处break应在if条件句内
    else:
        break

print(list01)