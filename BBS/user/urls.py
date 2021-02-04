from django.urls import path
from .views import *

urlpatterns = [
    path('token/', login_view),
    path('attention', follow_author_view)
]