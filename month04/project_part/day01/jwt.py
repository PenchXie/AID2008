import json
import base64
import time
import hmac
import copy


class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def encode(payload, key, exp=300):
        # 生成token
        # 1. header
        header = {'alg': 'HS256', 'typ': 'JWT'}
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        print(header_json)
        # header_bs = base64.urlsafe_b64encode(header_json.encode())
        header_bs = Jwt.b64encode(header_json.encode())
        print(header_bs)
        # 2. payload
        payload_data = copy.deepcopy(payload)
        payload_data['exp'] = time.time() + int(exp)
        payload_json = json.dumps(payload_data, separators=(',', ':'), sort_keys=True)
        payload_bs = Jwt.b64encode(payload_json.encode())
        print(payload_bs)
        # 3. 签名
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        hm_bs = Jwt.b64encode(hm.digest())
        print(hm_bs)
        return header_bs + b'.' + payload_bs + b'.' + hm_bs

    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')

    @staticmethod
    def b64decpde(b_s):
        rem = len(b_s) % 4
        if rem > 0:
            b_s += b'=' * (4 - rem)
        return base64.urlsafe_b64decode(b_s)

    @staticmethod
    def decode(token, key):
        header_bs, payload_bs, sign = token.split(b'.')
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        if sign != Jwt.b64encode(hm.digest()):
            raise
        payload_bs = Jwt.b64decpde(payload_bs)
        payload = json.loads(payload_bs)
        exp = payload['exp']
        now = time.time()
        if now > exp:
            raise
        return payload

if __name__ == '__main__':
    token = Jwt.encode({'username': 'lvze'}, '123456', 3)
    print(token)
    time.sleep(4)
    print(Jwt.decode(token, '123456'))
