from django.urls import path
from apps.accounts import views

urlpatterns = [
    path('setup/', views.setup),
    path('join/', views.join),
    path('login/', views.login),
]
