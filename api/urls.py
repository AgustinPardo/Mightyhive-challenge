from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns =[
    url('getData/', views.getdata, name='getdata'),
]