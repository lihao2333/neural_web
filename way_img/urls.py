from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),        
    path('gen_img',views.gen_img,name='gen_img'),        
    path('list_img',views.list_img,name='list_img'),        

]
