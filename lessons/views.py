from django.shortcuts import render
from django.views.generic import ListView
from .models import Lesson


class LessonsList(ListView):
    model = Lesson
    template_name = 'lessons/lessons_list.html'
    context_object_name = 'lessons'
