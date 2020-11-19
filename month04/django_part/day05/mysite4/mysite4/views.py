from django.http import HttpResponse


def set_cookie(request):
    resp = HttpResponse('set cookies ok!')
    resp.set_cookie('username', 'tedu', 600)
    return resp


def get_cookie(request):
    username = request.COOKIES.get('username', 'NoValue')
    return HttpResponse('username is %s' % username)


def delete_cookie(request):
    resp = HttpResponse('delete cookies ok!')
    resp.delete_cookie('username')
    return resp


def set_session(request):
    # 设置session
    request.session['uname'] = 'tarena'
    return HttpResponse('set session is OK!')

def get_session(request):
    uname = request.session.get('uname', 'no-value')
    return HttpResponse('uname is %s' % uname)


def delete_session(request):
    if request.session['uname']:
        del request.session['uname']
    return HttpResponse('delete session is OK!')