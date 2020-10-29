import time
from time import sleep

while True:
    tuple_time = time.localtime()
    with open('my.log', 'a+') as file:
        file.seek(0, 0)
        number = len(file.readlines()) + 1
        date = time.strftime('%Y-%m-%d %H:%M:%S', tuple_time)
        file.write(f"{number}. {date}\n")
        file.flush()
    sleep(2)
