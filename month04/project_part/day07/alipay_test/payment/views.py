import json

from alipay import AliPay
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.
app_private_key_string = open(settings.ALIPAY_KEY_DIR + 'app_private_key.pem').read()
alipay_public_key_string = open(settings.ALIPAY_KEY_DIR + 'alipay_public_key.pem').read()

ORDER_STATUS = 1  # 1 unpaid 2 payment successful 3 payment fail


class MyAliPay(View):
    # 构造函数, 与支付相关参数的初始化
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 创建一个AliPay对象
        self.alipay = AliPay(
            appid=settings.ALIPAY_APP_ID,
            app_notify_url=None,
            # 用户私钥
            app_private_key_string=app_private_key_string,
            # 支付宝公钥
            alipay_public_key_string=alipay_public_key_string,
            # 指定签名算法RAS256
            sign_type='RSA2',
            # 指明为测试, 请求会发送到沙箱服务器
            debug=True
        )

    def get_trade_url(self, order_id, amount):
        base_url = 'https://openapi.alipaydev.com/gateway.do'
        # create a query string of an order
        order_string = self.alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,
            total_amount=amount,
            # order title
            subject=order_id,
            # after the user pays, tell alipay the url to go to
            return_url=settings.ALIPAY_RETURN_URL,
            # url used to receive the payment result
            notify_url=settings.ALIPAY_NOTIFY_URL
        )
        return base_url + '?' + order_string

    def get_verify_result(self, data, sign):
        return self.alipay.verify(data, sign)

    def get_trade_result(self, order_id):
        result = self.alipay.api_alipay_trade_query(out_trade_no=order_id)
        if result.get('trade_status') == 'TRADE_SUCCESS':
            return True
        else:
            return False

class JumpView(MyAliPay):
    def get(self, request):
        return render(request, 'ajax_alipay.html')

    def post(self, request):
        json_obj = json.loads(request.body)
        order_id = json_obj['order_id']
        #
        pay_url = self.get_trade_url(order_id, 999)
        return JsonResponse({'pay_url': pay_url})


class ResultView(MyAliPay):
    def get(self, request):
        # return HttpResponse('payment successful')
        request_data = {k: request.GET[k] for k in request.GET.keys()}
        # get the order id
        order_id = request_data['out_trade_no']
        if ORDER_STATUS == 2:
            return HttpResponse('Payment Successful!')
        elif ORDER_STATUS == 1:
            # the server receiving post request fails, need to query the order status
            result = self.get_trade_result(order_id)
            if result:
                # update the order status from unpaid to payment successful
                return HttpResponse('query order & payment successful')
            else:
                # update the order status from unpaid to payment fail
                return HttpResponse('query order & payment fail')

    # post request sent by alipay server to a server with an IP
    def post(self, request):
        # receive the payment result from alipay
        # convert the post data to a dictionary structure
        request_data = {k: request.POST[k] for k in request.POST.keys()}
        # get the sign
        sign = request_data.pop('sign')
        # verify the sign
        is_verify = self.get_verify_result(request_data, sign)
        if is_verify:
            # get order id from request_data
            trade_status = request_data['trade_status']
            if trade_status == 'TRADE_SUCCESS':
                # update the order info from unpaid to payment successful in database
                return HttpResponse('ok')
            else:
                # update the order info from unpaid to payment fail in database
                return HttpResponse('ok')
        else:
            return HttpResponse('illegal request')
