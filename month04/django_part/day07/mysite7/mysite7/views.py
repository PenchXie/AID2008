import time

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(15)
def test_cache(request):
    t1 = time.time()
    # time.sleep(3)
    print('--test_cache view--')
    return HttpResponse('t1 is %s' % t1)


def test_mw(request):
    print('--mw view in--')
    return HttpResponse('my mw view')


def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('post is success!')


def test_page(request):
    list01 = ['a', 'b', 'c', 'd', 'e']
    # 创建分页器
    paginator = Paginator(list01, 2)
    cur_page = request.GET.get('page', 1)  # 得到默认的当前页
    page = paginator.page(cur_page)
    return render(request, 'test_page.html', locals())