from django.urls import path

from payment import views

urlpatterns = [
    # p://127.0.0.1:8000/payment/jump/
    path('jump/', views.JumpView.as_view()),
]