from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('log', views.register_page, name='log'),
    path('register_user', views.register, name='register_user'),
    path('login', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
]
