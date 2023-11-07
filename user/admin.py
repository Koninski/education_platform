from django.contrib import admin
from .models import User, History
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'phone_number', 'username')
    list_display_links = ('id', 'name', 'surname', 'username')
    search_fields = ('id', 'name', 'surname', 'email', 'phone_number', 'username')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'user', 'lesson')
    list_display_links = ('id', 'date', 'user', 'lesson')
    search_fields = ('id', 'date', 'user', 'lesson')


admin.site.register(User, UserAdmin)
admin.site.register(History, HistoryAdmin)

