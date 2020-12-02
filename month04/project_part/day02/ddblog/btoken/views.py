import hashlib
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from user.models import UserProfile
from user.views import make_token


# Create your views here.
class TokenView(View):
    def post(self, request):
        json_str = request.body
        json_body = json.loads(json_str)
        username = json_body['username']
        password = json_body['password']
        print(username, password)

        # 校验用户名和用户名
        try:
            user = UserProfile.objects.get(username=username)
        except Exception as e:
            print('error is', e)
            result = {'code': 10200, 'error': '用户名或密码错误'}
            return JsonResponse(result)

        md5 = hashlib.md5()
        md5.update(password.encode())
        if md5.hexdigest() != user.password:
            result = {'code': 10201, 'error': '用户名或密码错误'}
            return JsonResponse(result)
        # 签发token
        token = make_token(username)
        token = token.decode()

        result = ({'code': 200, 'username': username,
                             'data': {'token': token}})
        return JsonResponse(result)