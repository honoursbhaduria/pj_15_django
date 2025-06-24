from django.urls import path , include
from .views import *
from django.contrib  import admin

urlpatterns = [

    path('get_item/',get_item),
]