from django.conf.urls import url

from article import views

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^rank$', views.rank_view),
    url(r'^detail$', views.article_detail_view),
    url(r'^newarticle$', views.new_article_view)
]