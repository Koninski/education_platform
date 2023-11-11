from django.urls import path

from .views import LessonsList

url_patterns = [
    path('', LessonsList.as_view(), name='lessons_list'),
]