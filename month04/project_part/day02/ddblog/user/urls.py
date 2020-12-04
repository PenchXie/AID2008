from django.urls import path

from user import views

urlpatterns = [
    # http://127.0.0.1:8000/v1/users/tedu
    path('<str:username>', views.UsersView.as_view()),
    # http://127.0.0.1:8000/v1/users/tedu/avatar
    path('<str:username>/avatar', views.user_avatar),
]