from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from .models import Course, Chapter
from lessons.models import Lesson
from .forms import CreateCourse, CreateChapter
from django.urls import reverse_lazy


# Главная страница, выводит все курсы в порядке создания
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


# Класс-контроллер для обзора курса
class EditCourse(DetailView):
    model = Course
    pk_url_kwarg = 'course_id2'                 #
    template_name = 'courses/edit_course.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        contecxt = super().get_context_data(**kwargs)
        obj = Chapter.objects.filter(course__pk=self.kwargs['course_id2'])
        contecxt['chapter'] = Chapter.objects.filter(course__pk=self.kwargs['course_id2'])
        lessons = {}
        k = 0
        for i in obj:
            list_a = []
            namechapter = f'chapter_{k}'
            list_a.append(Chapter.objects.filter(pk=i.pk))
            list_a.append(Lesson.objects.filter(chapter__pk=i.pk))
            lessons[namechapter] = list_a
            k = 1 + k
        contecxt['lessons'] = lessons
        return contecxt


# Класс-контроллер для создания главы, LoginRequiredMixin - ограничение доступа к странице
class AddChapter(LoginRequiredMixin, CreateView):
    form_class = CreateChapter
    template_name = 'courses/createchapter.html'

    def get_success_url(self):
        return reverse_lazy('edit_course', args=[self.kwargs['course_id3']])

    # Переопределение метода проверки формы перед сохранением, для присвоения id-пользователя к полю id-автор
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.course_id = self.kwargs['course_id3']
        obj.save()
        return super().form_valid(form)


