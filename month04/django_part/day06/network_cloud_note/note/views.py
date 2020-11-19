from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from note.models import Note


def login_check(func):
    def wrapper(request, *args, **kwargs):
        if 'uname' not in request.session or 'uid' not in request.session:
            c_uname = request.COOKIES.get('uname')
            c_uid = request.COOKIES.get('uid')
            if not c_uname or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                # session中没有数据, cookie中有数据
                request.session['uname'] = c_uname
                request.session['uid'] = c_uid
        # session有数据, 继续
        return func(request, *args, **kwargs)
    return wrapper

# Create your views here.
# 只有登录用户才可以操作
@login_check
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        uid = request.session['uid']
        Note.objects.create(title=title, content=content, user_id=uid)
        # 完善后可重定向到列表
        return HttpResponse('添加笔记成功!')

def list_view(request):
    return None