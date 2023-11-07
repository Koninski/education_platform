from django.urls import path

from .views import RegisterView

url_patterns = [
    path('register', RegisterView.as_view(), name='register')
]