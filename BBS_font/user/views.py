from django.shortcuts import render

# Create your views here.


def userinfo_view(request):
    if request.method == 'GET':
        return render(request, 'userinfo.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')


def inform_view(request):
    if request.method == 'GET':
        return render(request, 'inform.html')