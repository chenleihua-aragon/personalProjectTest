from . import views
from django.urls import path


urlpatterns = [
    path('userinfo/<str:name>', views.userinfo_view, name="userinfo"),
    path('cookies/', views.login_view, name="login"),
    path('newuser/', views.register_view, name="register"),
    path('out/', views.logout_view, name="out")
]