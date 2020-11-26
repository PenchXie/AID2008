import redis
import time

r = redis.Redis(password='123456')


def double_account(user_id):
    key = 'account_%s' % user_id
    with r.pipeline(transaction=True) as pipe:
        while True:
            try:
                pipe.watch(key)
                value = int(r.get(key))
                value *= 2
                print('new value is %s' % value)
                print('sleep start')
                time.sleep(10)
                print('sleep end')
                pipe.multi()
                pipe.set(key, value)
                pipe.execute()
                break
            except redis.WatchError:
                print(r.get(key))
                print("--value changed--")
                continue

    return int(r.get(key))

if __name__ == '__main__':
    print(double_account('tedu'))
