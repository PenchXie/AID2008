from django.urls import path

from note import views

urlpatterns = [
    path('add', views.add_view),
    path('', views.list_view),
]