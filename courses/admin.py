from django.contrib import admin
from .models import Category, Course, Chapter, Review
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'author', 'price', 'overall_rating')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'category', 'author')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'name', 'order')
    list_display_links = ('id', 'course', 'name', 'order')
    search_fields = ('id', 'name', 'category')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'date', 'user', 'value')
    list_display_links = ('id', 'course', 'date', 'user')
    search_fields = ('id', 'course', 'date', 'user')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Review, ReviewAdmin)
