from django.contrib import admin
from .models import Lesson, Comment
# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'chapter', 'category', 'author')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'category', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'User', 'lesson')
    list_display_links = ('id', 'date', 'User', 'lesson')
    search_fields = ('id', 'date', 'User', 'lesson')


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment, CommentAdmin)
