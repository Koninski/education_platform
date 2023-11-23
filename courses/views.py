from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from .models import Course
from .forms import CreateCourse
from django.urls import reverse_lazy


# Главная страница, выводит все курсы в порядке создания.
class Index(ListView):
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'


# Класс-контроллер для создания курса, LoginRequiredMixin - ограничение доступа к странице
class AddCourse(LoginRequiredMixin, CreateView):
    form_class = CreateCourse
    template_name = 'courses/createcourse.html'

    # Переопределение метода проверки формы перед сохранением, для присвоения id-пользователя к полю id-автор
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author_id = self.request.user.pk
        obj.save()
        return super(AddCourse, self).form_valid(form)


# Класс-контроллер для обзора курса
class GetCourse(DetailView):
    model = Course
    pk_url_kwarg = 'course_id'
    template_name = 'courses/course.html'
    context_object_name = 'courses'