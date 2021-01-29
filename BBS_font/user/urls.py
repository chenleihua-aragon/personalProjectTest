from . import views
from django.urls import path


urlpatterns = [
    path('userinfo/', views.userinfo_view),
    path('token/', views.login_view),
    path('newuser/', views.register_view),
    path('information/', views.inform_view)
]