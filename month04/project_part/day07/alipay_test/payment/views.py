import json

from django.shortcuts import render
from django.views import View


# Create your views here.
class MyAliPay(View):
    # 构造函数, 与支付相关参数的初始化
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 创建一个AliPay对象
        self.alipay = AliPay(
            appid=,
            app_notify_url=None,
            # 用户私钥
            app_private_key_string=,
            # 支付宝公钥
            alipay_public_key_string=,
            # 指定签名算法RAS256
            sign_type='RSA2',
            # 指明为测试, 请求会发送到沙箱服务器
            debug=True
        )

class JumpView(View):
    def get(self, request):
        return render(request, 'ajax_alipay.html')
    def post(self, request):
        json_obj = json.loads(request.body)
        order_id = json_obj['order_id']
        # 