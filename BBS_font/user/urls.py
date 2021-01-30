from . import views
from django.urls import path


urlpatterns = [
    path('userinfo/', views.userinfo_view, name="userinfo"),
    path('token/', views.login_view, name="login"),
    path('newuser/', views.register_view, name="register"),
    path('information/', views.inform_view, name="inform")
]