from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.vista_login, name='login'),
    path('register/', views.vista_registro, name='register'),
    path('logout/', views.vista_logout, name='logout'),
]
