from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:post_id>', views.Index.as_view(), name='index'),
    path('list', views.BlogList.as_view(), name='list'),
]
