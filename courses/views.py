from django.shortcuts import render
from django.views.generic import ListView
from .models import Course


class Index(ListView):
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'

