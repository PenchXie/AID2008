import hashlib

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import User


def login_view(request):
    if request.method == 'GET':
        # 获取页面前, 判断用户以前是否登录过
        if 'uname' in request.session and 'uid' in request.session:
            return HttpResponse('您已登录过')
        # 判断cookie中是否有数据
        uname = request.COOKIES.get('uname')
        uid = request.COOKIES.get('uid')
        if uname and uid:
            # 将cookie的数据回写session
            request.session['uname'] = uname
            request.session['uid'] = uid
            # 免登录
            return HttpResponse('您已登录过')
        return render(request, 'user/login.html')
    elif request.method == 'POST':

        # 打印表单数据
        print(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        # 为空判断
        if not username or not password:
            return HttpResponse('用户名和密码不能为空')
        # 检查用户是否存在
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('Error is', e)
            return HttpResponse('用户名或密码错误!')
        # 检查密码
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != user.password:
            return HttpResponse('用户名或密码错误!')
        # 在session中保存用户信息
        request.session['uname'] = user.username
        request.session['uid'] = user.id
        # 在cookie中也保存用户信息
        resp = HttpResponse('用户登录成功!')
        if 'remember' in request.POST:
            resp.set_cookie('uname', user.username, 7 * 3600 * 24)
            resp.set_cookie('uid', user.id, 7 * 3600 * 24)
        return resp


def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        # 为空验证
        if not username or not password_1:
            return HttpResponse('用户名或密码不能为空')
        # 密码一致验证
        if password_1 != password_2:
            return HttpResponse('两次输入的密码不一致!')
        # 用户名是否被占用
        old_user = User.objects.filter(username=username)
        if old_user:
            return HttpResponse('此用户已存在!')
        # 4.生成密码hash值
        md5 = hashlib.md5()
        # update参数要求是字节串
        md5.update(password_1.encode())
        # 得到hash值, 是16进制的字符串
        password_h = md5.hexdigest()
        # 添加数据
        try:
            User.objects.create(username=username, password=password_h)
        except Exception as e:
            print('error is', e)
            return HttpResponse('此用户已存在!')
        # 响应
        return HttpResponse('用户注册成功')


def logout_view(request):
    # 清除session
    if 'uname' in request.session:
        del request.session['uname']
    if 'uid' in request.session:
        del request.session['uid']
    # 清除cookie
    resp = HttpResponse('用户退出成功')

    if 'uname' in request.COOKIES:
        resp.delete_cookie('uname')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp
