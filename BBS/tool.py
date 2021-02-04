from django.http import JsonResponse
from jwt_test import *
from user import models


# 涉及到信息修改等敏感操作的验证，严格验证用户
def auth(*methods):
    def wrapper(func):
        def login(request, *args, **kwargs):
            token = request.META.get('HTTP_BBSAUTHORIZATION')
            if request.method not in methods:
                return func(request, *args,  **kwargs)
            if not token or token == 'null':
                return JsonResponse({'code': 1, 'error': '请先登录，错误码001'})
            _jwt = Jwt()
            try:
                payload = _jwt.jwt_decode(token.encode(), b'6*/M?df*/\s')

            except Unlog:
                return JsonResponse({'code': 2, 'error': '请登录，错误码002'})
            except Expired:
                return JsonResponse({'code': 3, 'error': '请重新登陆，错误码003'})

            except Exception as e:
                raise e
                # return JsonResponse({'code': 110, 'error': 'Please try again'})
            username = payload.get('username')

            user = models.User.objects.filter(username=username)
            if user[0].is_active:
                request.user = user[0]

            else:
                return JsonResponse({'code': 4, 'error': '请输入有效用户名，错误码004'})

            return func(request, *args,  **kwargs)
        return login
    return wrapper
