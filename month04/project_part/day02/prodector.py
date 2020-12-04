from tasks import task_test

def getResult(r):
    while True:
        if r.ready():
            print(r.result)
            break

if __name__ == '__main__':
    # 1. 直接返回, 不阻塞
    r = task_test.delay(4)
    print(r)
    # 2. 在以后的某个时候, 获取结果
    getResult(r)