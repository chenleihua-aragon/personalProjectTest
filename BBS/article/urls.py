from django.urls import path
from .views import *

urlpatterns = [
    path('<str: article_type>', get_article_view)
]