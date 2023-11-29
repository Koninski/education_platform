from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Lesson
from .forms import CreateLesson
from django.urls import reverse_lazy
from courses.models import Course, Chapter


class LessonsList(ListView):
    model = Lesson
    template_name = 'lessons/lessons_list.html'
    context_object_name = 'lessons'


# Класс-контроллер для создания уроков, LoginRequiredMixin - ограничение доступа к странице
class AddLesson(LoginRequiredMixin, CreateView):
    form_class = CreateLesson
    template_name = 'lessons/createlesson.html'
    pk_url_kwarg = 'course_id4'
    context_object_name = 'lessons'

    def get_context_data(self, **kwargs):
        contecxt = super().get_context_data(**kwargs)
        contecxt['chapter'] = Chapter.objects.filter(pk=self.kwargs['chapter_id'])
        contecxt['course'] = Course.objects.filter(pk=self.kwargs['course_id4'])
        return contecxt

    def get_success_url(self):
        return reverse_lazy('edit_course', args=[self.kwargs['course_id4']])

    # Переопределение метода проверки формы перед сохранением, для присвоения id-пользователя к полю id-автор
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author_id = self.request.user.pk
        obj.course_id = self.kwargs['course_id4']
        obj.chapter_id = self.kwargs['chapter_id']
        obj.save()
        return super().form_valid(form)

