from django.urls import path

from news import views

urlpatterns = [
    path('index', views.news_index),
]