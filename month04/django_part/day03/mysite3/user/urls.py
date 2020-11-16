from django.urls import path

from user import views

urlpatterns = [
    # http://127.0.0.1:8000/user/add
    path('add', views.add_user),
    # http://127.0.0.1:8000/user/add
    path('index', views.index_view),
]