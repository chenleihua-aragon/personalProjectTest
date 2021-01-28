from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^userinfo/$', views.userinfo_view),
    url(r'^token/$', views.login_view),
    url(r'^newuser/$', views.register_view),
    url(r'information/$', views.inform_view)
]