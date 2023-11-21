from django.urls import path
from .views import Index, AddCourse, GetCourse


url_patterns = [
    path('', Index.as_view(), name='home'),
    path('createcourse', AddCourse.as_view(), name='create_course'),
    path('course/<int:course_id>', GetCourse.as_view(), name='course-display'),
]
