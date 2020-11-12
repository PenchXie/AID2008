from django.http import HttpResponse


def page1_view(request):
    return HttpResponse('<h1>页面1, 吕泽是菜逼</h1>')


def page2_view(request):
    return HttpResponse('<h1>页面2</h1>')


def index_view(request):
    return HttpResponse('<h1>想念吕泽玛利亚</h1>')


def pagen_view(request, num):
    return HttpResponse(f'<h1>想念吕泽玛利亚的第{num}天</h1>')
    # return HttpResponse('<h1>想念吕泽玛利亚的第%s天</h1>' % num)


def page_str(request, info):
    return HttpResponse('<h1>%s</h1>' % info)


def op_num(request, a, op, b):
    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    else:
        return HttpResponse('<h1>不支持此操作</h1>')

    return HttpResponse('<h1>Result: %s</h1>' % result)


def birthday(request, y, m, d):
    return HttpResponse('生日:%s年%s月%s日' % (y, m, d))


def test_get(request):

    # /test_get
    # print(request.path_info)

    # 'GET'
    # print(request.method)
    # 包含了查询字符串的path
    print(request.get_full_path())

    # <QueryDict: {'a': ['100'], 'b': ['200'], 'c': ['300']}>
    # 类字典结构, 包含了查询字符串中的名称和值
    # print(request.GET)
    
    return HttpResponse('--吕泽菜逼--')
