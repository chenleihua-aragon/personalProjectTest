from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def rank_view(request):
    if request.method == 'GET':
        return render(request, 'rank.html')


def article_detail_view(request):
    if request.method == 'GET':
        return render(request, 'article.html')


def new_article_view(request):
    if request.method == 'GET':
        return render(request, 'new_article.html')