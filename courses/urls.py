from django.urls import path
from .views import Index


url_patterns = [
    path('', Index.as_view(), name='home'),
]
