from django.urls import path

from .views import LessonsList, AddLesson

url_patterns = [
    path('lessons_list', LessonsList.as_view(), name='lessons_list'),
    path('create-lesson/<int:course_id4>/<int:chapter_id>', AddLesson.as_view(), name='create_lesson'),
]
