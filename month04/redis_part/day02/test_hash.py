import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
r.hsetnx('pyh1', 'uname', 'lvze')
print(r.hget('pyh1', 'uname'))
r.hmset('pyh1', {
    'age': 32,
    'gender': 'M',
    'desc': 'idiet',
})
print(r.hmget('pyh1', 'uname', 'age'))
print(r.hgetall('pyh1'))
r.delete('pyh1')