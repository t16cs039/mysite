from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('home/', views.Home.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('passord_change/', views.PasswordChange.as_view(), name='password_change'),
    path('passord_change_done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('complete/', views.Complete.as_view(), name='complete'),
    path('play/', views.Play.as_view(), name='play'),
]
