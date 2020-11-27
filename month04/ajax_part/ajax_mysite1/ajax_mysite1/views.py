from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def test_xhr(request):
    return render(request, 'test_xhr.html')


def test_xhr_get(request):
    return render(request, 'test_xhr_get.html')


def test_xhr_get_server(request):
    return HttpResponse('this is Ajax Data')


def test_jq_get(request):
    return render(request, 'test_jq_get.html')


def test_json(request):
    return render(request, 'test_json.html')


def make_json_server(request):
    # 字典
    map1 = {
        'name': 'lvze',
        'age': 34,
    }
    # return JsonResponse(list1, safe=True)
    # 列表
    list1 = [
        {"name": "qtx", "age": 32},
        {"name": "mzg", "age": 45},
    ]
    return JsonResponse(list1, safe=False)