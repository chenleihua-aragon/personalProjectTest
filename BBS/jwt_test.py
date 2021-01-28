import hmac
import json
from base64 import *
import time
from copy import deepcopy


class Expired(Exception):
    def __init__(self, info):
        self.info = info


class Unlog(Exception):
    def __init__(self, info):
        self.info = info


class Jwt(object):
    def __init__(self):
        super(Jwt, self).__init__()

    @staticmethod
    def b64encode(s):
        return urlsafe_b64encode(s).replace(b'=', b'')

    @staticmethod
    def b64decode(s):
        length = len(s) % 4
        if length > 0:
            s += (4-length)*b'='
        return urlsafe_b64decode(s)

    @staticmethod
    def jwt_encode(key, payload, exp):
        header = {'alg': 'HS256', 'typ': 'JWT'}
        payload_dc = deepcopy(payload)
        if isinstance(exp, int):
            payload_dc['exp'] = exp + time.time()
        encode_str_header = Jwt.b64encode(json.dumps(header, separators=(',', ':'), sort_keys=True).encode())
        encode_str_payload = Jwt.b64encode(json.dumps(payload_dc, separators=(',', ':'), sort_keys=True).encode())
        s = encode_str_header + b'.' + encode_str_payload

        ha = hmac.new(key, s, digestmod='SHA256')
        ha_res = Jwt.b64encode(ha.digest())

        return s + b'.' + ha_res

    @staticmethod
    def jwt_decode(token, key):
        if isinstance(key, str):
            key = key.encode()
        header_bs64, payload_bs64, signature = token.split(b'.')
        s = header_bs64 + b'.' + payload_bs64
        h = hmac.new(key, s, digestmod='SHA256')
        sign = Jwt.b64encode(h.digest())
        length = len(payload_bs64)
        # 判断浏览器传过来的签名是否是用约定的密钥和算法计算出来的
        if sign == signature:
            payload_js = Jwt.b64decode(payload_bs64).decode()
            payload = json.loads(payload_js)
            # 判断payload中是否有过期时间的选项
            # 有的话，判断token是否过期
            if 'exp' in payload:
                t = time.time()
                if payload['exp'] > t:
                    return payload
                else:
                    raise Expired('Please relogin')
        else:
            raise Unlog('Please login')


if __name__ == '__main__':
    jwt_test = Jwt()
    res = jwt_test.jwt_encode(key=b'aragon_test_bbs', payload={'username': 'chenleihua'}, exp=259200)
    print('token:', res)
    # print('**********')
    # print('**********')
    # res = b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNoZW5sZWlodWEifQ.8hiPpF7tiOls0OZK1B11uiUS_AFb_snrIaSdknxUyo8'
    pay = jwt_test.jwt_decode(res, 'aragon_test_bbs')
    print(pay)
