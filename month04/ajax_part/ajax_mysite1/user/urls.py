from django.urls import path

from user import views

urlpatterns = [
    path('all', views.get_users),
    path('index', views.index_users),
]