import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User


def get_users(request):
    users = User.objects.all()
    # # 方式一
    # users_json = serializers.serialize('json', users)
    # # return JsonResponse(users_json, safe=False)
    # return HttpResponse(users_json, content_type='application/json')

    # 方式二
    res = []
    for user in users:
        u_data = {}
        u_data['username'] = user.username
        u_data['age'] = user.age
        res.append(u_data)
    # res_json = json.dumps(res)
    # return HttpResponse(res_json, content_type='application/json')
    return JsonResponse(res, safe=False)


def index_users(request):
    return render(request, 'user_index.html')