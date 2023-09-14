from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('log', views.register_page, name='log'),
    path('register_user', views.register, name='register_user'),
    path('login', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logout, name='logout'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
]
