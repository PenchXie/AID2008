import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .tasks import task_test


# Create your views here.
def test_celery(request):
    task_test.delay()
    now = datetime.datetime.now()
    html = 'result at %s' % now.strftime('%H:%M:%S')
    return HttpResponse(html)
