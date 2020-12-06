from ddblog.celery import app
from tools.sms import YunTongXin
from django.conf import settings

@app.task
def send_sms(phone, code):
    x = YunTongXin(settings.SMS_ACCOUNT_ID, settings.SMS_AUTH_TOKEN,
                   settings.SMS_APP_ID, settings.SMS_TEMPLATES_ID)
    # 发送短信
    res = x.run(phone, code)
    return res