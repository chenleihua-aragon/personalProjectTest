import hashlib
from django.http import JsonResponse
from .. import jwt_test
import json
from .models import *
# Create your views here.


def make_token(username, exp=259200) :
    jwt = jwt_test.Jwt()
    token = jwt.jwt_encode(key=b'6*/M?df*/\s', payload={'username': username}, exp=exp)
    return token


def login_view(request):
    """
    用户登录，生成token
    """
    if request.method == 'POST':
        data = json.loads(request.body.decode())

        if not data:
            return JsonResponse({'code': 101, 'error': '用户数据不能为空'})

        username = data.get('username')
        if not username:
            return JsonResponse({'code': 102, 'error': '用户名不能为空'})

        password = data.get('password')
        if not password:
            return JsonResponse({'code': 103, 'error': '密码不能为空'})

        try:
            user = User.objects.get(username=username, is_active=1)
        except Exception as e:
            return JsonResponse({'code': 104, 'error': '用户名或密码不正确'})

        salt = user.username+"k_L*&nb%$vd#_k"
        m = hashlib.md5(salt.encode())
        m.update(password.encode())
        password = m.hexdigest()

        if password != user.password:
            return JsonResponse({'code': 105, 'error': '用户名或密码不正确'})

        token = make_token(username)
        avatar = str(user.avatar)
        return JsonResponse({'code': 100, 'username': username, 'sign': user.sign, 'data': {'token': token.decode(),
                                                                                            'avatar': avatar
                                                                                            }})