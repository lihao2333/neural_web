from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),        
    path('gen_video',views.gen_video,name='gen_video'),        
    path('list_video',views.list_video,name='list_video'),        
]
