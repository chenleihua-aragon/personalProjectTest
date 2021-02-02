from django.urls import path
from .views import *

urlpatterns = [
    path('<str:article_type>', get_article_list_view),
    path('<int:id>', get_article_detail_view),
]