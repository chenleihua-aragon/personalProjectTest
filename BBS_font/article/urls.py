from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view),
    path('rank', views.rank_view),
    path('detail', views.article_detail_view),
    path('newarticle', views.new_article_view)
]