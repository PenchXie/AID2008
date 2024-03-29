import jwt
from django.conf import settings
from django.http import JsonResponse

from user.models import UserProfile


def login_check(func):
    def wrapper(request, *args, **kwargs):
        # 从请求头中获取token
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code': 403, 'error': '请登录'}
            return JsonResponse(result)
        # 校验token
        try:
            payload = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithm='HS256')
        except Exception as e:
            print('check login error is', e)
            result = {'code': 403, 'error': '请登录'}
            return JsonResponse(result)
        # 从载荷中获取私有声明
        username = payload['username']
        # 根据用户名称获取用户对象
        user = UserProfile.objects.get(username=username)
        # 将用户对象保存到request对象中
        request.myuser = user
        return func(request, *args, **kwargs)

    return wrapper

def get_user_by_request(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        res = jwt.decode(token, settings.JWT_TOKEN_KEY)
    except Exception as e:
        print("get user jwt error is", e)
        return None
    return res['username']