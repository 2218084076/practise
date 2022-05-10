from django.urls import path
from . import views

urlpathterns = [
    path('',views.index,name='index')
]