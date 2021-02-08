from django.urls import path

from . import views

urlpatterns = [
    path('<str:article_type>', views.index_view, name="index"),
    path('<str:article_type>?sort_method=<str:sort_method>', views.index_view, name="index"),
    path('detail/<int:article_id>', views.article_detail_view, name="article_detail"),
    path('detail/<int:article_id>/delete', views.article_delete_view, name="delete"),
    path('1/newarticle', views.new_article_view, name="new_article"),
    path('2/comment/<int:article_id>', views.article_comment_view, name="comment")
]