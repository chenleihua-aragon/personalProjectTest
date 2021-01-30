from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path('rank', views.rank_view, name="rank"),
    path('detail', views.article_detail_view, name="article_detail"),
    path('newarticle', views.new_article_view, name="new_article")
]