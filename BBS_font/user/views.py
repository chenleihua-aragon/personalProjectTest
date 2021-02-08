from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
import hashlib
from .models import *
# Create your views here.


def userinfo_view(request, name):
    # if request.method == 'GET':
    #     return render(request, 'userinfo.html')
    pass


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == "POST":
        username = request.POST.get("username")
        if username == '':
            username_error = "用户名不能为空"
            return render(request, 'login.html', {"username_error": username_error,
                                                  "username": username})
        try:
            user = User.objects.get(name=username, is_active=True)

        except Exception as e:
            username_error = "账户:"+username+"不存在"
            return render(request, 'login.html', {"username_error": username_error,
                                                  "username": username})

        else:
            password = request.POST.get("password")
            if password == '':
                password_error = "密码不能为空"
                return render(request, 'login.html', {"password_error": password_error,
                                                      "username": username})
            salt = username + '&*^54#6?>mnj'
            m = hashlib.md5(salt.encode())
            m.update(password.encode())
            password = m.hexdigest()

            if password != user.password:
                account_error = '账户名或者密码错误'
                return render(request, 'login.html', {"account_error": account_error,
                                                      "username": username})

            else:
                username = user.name
                request.session['user'] = {'user': username}
                return HttpResponseRedirect("/article/news")

    else:
        return Http404("对不起，操作错误")


def logout_view(request):
    if 'user' in request.session:
        del request.session['user']
    return HttpResponseRedirect("/article/news")

def register_view(request):
    reg_form = RegisterForm()
    if request.method == 'GET':
        return render(request, 'register.html', {"reg_form": reg_form})

    elif request.method == "POST":
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            userinfo_dic = reg_form.cleaned_data
            username = userinfo_dic['username']
            password = userinfo_dic['password']
            salt = username + '&*^54#6?>mnj'
            m = hashlib.md5(salt.encode())
            m.update(password.encode())
            password = m.hexdigest()
            try:
                user = User(name=username,
                            password=password)
                user.save()
            except Exception as e:

                return Http404("服务器错误，请重试")

            return HttpResponseRedirect('/user/login/')

        else:
            return HttpResponse("注册信息有误")

    else:
        return HttpResponse("请求类型错误")

# def register_view(request):
#     if request.method == 'GET':
#         return render(request, 'register.html')
#
#     elif request.method == "POST":
#         pass


def inform_view(request):
    if request.method == 'GET':
        return render(request, 'inform.html')
