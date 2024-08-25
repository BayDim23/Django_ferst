from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('m', views.m, name='m'),
    path('s', views.s, name='s'),
    path('f', views.f, name='f'),
    path('g', views.g, name='g'),

]