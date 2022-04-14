from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='Inicio'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),
]
