from django.urls import path
from . import views

app_name="mondaiapp"
urlpatterns = [
    path("", views.index),
    path("C",views.compos),
    path("compos/",views.compos,name="compos"),
    path("index/",views.index,name='index'),
    path("result/",views.result,name='result'),
]