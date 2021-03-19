from django.contrib import admin
from django.urls import path,include,re_path
from . import views


urlpatterns=[
    re_path(r'catalog^$',views.catalog,name='catalog'),
    
]