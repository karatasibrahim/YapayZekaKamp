from django.contrib import admin
from django.urls import path
from django.urls import include,re_path
from . import views

urlpatterns = [
   re_path(r'^$',views.home,name='home'),
   re_path(r'imageprocess',views.imageprocess,name='imageprocess')
     
]