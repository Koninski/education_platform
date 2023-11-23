from django.urls import path

from .views import LessonsList

url_patterns = [
    path('lessons_list', LessonsList.as_view(), name='lessons_list'),
]