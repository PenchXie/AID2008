from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index_view(request):
    name = "吕泽玛莉亚"
    return render(request, 'base.html', locals())


def news_view(request):
    return render(request, 'news.html')


def sports_view(request):
    return render(request, 'sports.html')


def military_view(request):
    url = reverse('pgn', args=[200])
    print(url)
    # return render(request, 'military.html')
    return HttpResponseRedirect(url)

def pagen_view(request, n):
    return HttpResponse('pagen:%s' % n)


def test_static(request):
    return render(request, 'test_static.html')