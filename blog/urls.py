from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'blog'

urlpatterns = [
    path('<str:stat>/<int:post_id>/', views.Index.as_view(), name='index'),
    path('list/', views.BlogList.as_view(), name='list'),
    path('<str:stat>/', views.Sample.as_view(), name='sample'),
    #path('example/', views.Example.as_view(), name='example'),
    path('article', views.Article.as_view(), name='article'),
]
