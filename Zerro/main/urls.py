from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]

urlpatterns = [
    path('data', views.data)
]

urlpatterns = [
    path('test', views.test)
]