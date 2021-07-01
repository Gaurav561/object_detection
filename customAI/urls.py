from django.contrib import admin
from django.urls import include,path
from . import views
urlpatterns = [

    path('', views.index , name='index'),
    path('dataset/', views.create_data , name='db')
]
