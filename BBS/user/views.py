import hashlib
from django.http import JsonResponse
import json
import jwt_test
from models import *
import datetime
from tool import *

"""
time = datetime.datetime.now()
再把time赋值给需要的DatetimeField字段即可
"""

# Create your views here.


def make_token(username, exp=259200):
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


# 关注用户
@auth("POST")
def follow_author_view(request):
    if request.method != 'POST':
        return JsonResponse({'code': 106, 'error': '请求类型错误，错误码106'})

    data = json.loads(request.body.decode())
    if not data:
        return JsonResponse({'code': 107, 'error': '请求数据错误，错误码107'})
    author_name = data.get("author_name")
    if not author_name:
        return JsonResponse({'code': 108, 'error': '作者信息不能为空，错误码108'})

    # 根据作者名查找出对应的用户
    try:
        user = User.objects.get(username=author_name,
                                is_active=True)
    except Exception as e:
        return JsonResponse({'code': 109, 'error': '请求用户信息错误，错误码109'})

    try:
        ctime = datetime.datetime.now()
        new_friend = Friends(master=request.user,
                             guest=user,
                             as_friend_at=ctime)
        new_friend.save()
    except Exception as e:
        return JsonResponse({'code': 110, 'error': '服务器错误，错误码110'})

    else:
        return JsonResponse({'code': 100, 'data': '关注成功'})

