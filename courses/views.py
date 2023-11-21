from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from .models import Course
from .forms import CreateCourse
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


class Index(ListView):
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'


class AddCourse(LoginRequiredMixin, CreateView):
    form_class = CreateCourse
    template_name = 'courses/createcourse.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author_id = self.request.user.pk
        obj.save()
        return super(AddCourse, self).form_valid(form)


class GetCourse(DetailView):
    model = Course
    pk_url_kwarg = 'course_id'
    template_name = 'courses/course.html'
    context_object_name = 'courses'