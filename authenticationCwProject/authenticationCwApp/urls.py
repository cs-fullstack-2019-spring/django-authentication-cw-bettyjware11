from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createUser/', views.createUser, name='createUser'),
    path('confirmUser/', views.confirmUser, name='confirmUser'),
]