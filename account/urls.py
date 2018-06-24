from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.index,name='index'),        
    url(r"^login/$", auth_views.login, {"template_name":"account/login.html"},name="user_login"),
    url(r'^logout/$', auth_views.logout,{"template_name":"account/logout.html"}, name='user_logout'),
]
