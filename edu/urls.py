from django.contrib import admin
from django.urls import path, include

import user.urls
import lesson.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(user.urls.url_patterns)),
    path('', include(lesson.urls.url_patterns))
]
