import json

from django.conf import settings
from django.core import mail
from django.http import HttpResponse, JsonResponse


def send_email(requests):
    if requests.method != 'POST':
        return HttpResponse('现在还没有这个功能哦')
    json_str = requests.body
    json_obj = json.loads(json_str)
    name = json_obj['name']
    phone = json_obj['phone']
    email = json_obj['email']
    message = json_obj['message']
    subject = "{}_{}_{}".format(name, phone, email)
    mail.send_mail(subject, json_str, settings.EMAIL_HOST_USER, settings.EMAIL_TARGET)
    return JsonResponse({'code': 200})
