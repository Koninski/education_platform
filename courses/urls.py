from django.urls import path
from .views import Index, AddCourse, GetCourse, EditCourse, AddChapter


url_patterns = [
    path('', Index.as_view(), name='home'),
    path('createcourse', AddCourse.as_view(), name='create_course'),
    path('course/<int:course_id>', GetCourse.as_view(), name='course_display'),
    path('edit-course/<int:course_id2>', EditCourse.as_view(), name='edit_course'),
    path('course/<int:course_id3>/create-chapter', AddChapter.as_view(), name='create_chapter')
]
