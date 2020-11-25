import redis
from django.http import HttpResponse
from django.shortcuts import render

from user.models import User

r = redis.Redis(password='123456')


# Create your views here.
def user_detail(request, uid):
    cache_key = 'user_%s' % uid
    if r.exists(cache_key):
        # 从缓存获取数据
        data = r.hgetall(cache_key)
        # {b'username': b'lvze', b'age': b'32'}
        print(data)
        # 将字典中的字节串转换为字符串
        str_data = {k.decode(): v.decode() for k, v in data.items()}
        # {'username': 'lvze', 'age': '32'}
        print(str_data)
        username = str_data['username']
        age = str_data['age']
        html = 'cache data: username is %s, age is %s' % (username, age)
        return HttpResponse(html)
    else:
        # 获取数据写入缓存, 返回响应
        try:
            user = User.objects.get(id=uid)
        except Exception as e:
            print('Error is', e)
            return HttpResponse('--no such user--')
        # 写入缓存, 返回响应
        r.hmset(cache_key, {
            'username': user.username,
            'age': user.age,
        })
        r.expire(cache_key, 10)
        # 返回响应
        html = 'mysql data: username is %s, age is %s' % (user.username, user.age)
        return HttpResponse(html)


def user_update(request, uid):
    # 修改数据后, 清缓存
    age = request.GET.get('age', 0)
    try:
        user = User.objects.get(id=uid)
    except Exception as e:
        return HttpResponse('--no such user--')
    user.age = age
    user.save()
    # 清除缓存
    cache_key = 'user_%s' % uid
    r.delete(cache_key)
    return HttpResponse('更新用户信息成功!')
