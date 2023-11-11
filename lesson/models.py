from django.db import models
from django.contrib.auth import get_user_model


class Lesson(models.Model):
    name = models.CharField(max_length=100,                     # Название
                            verbose_name='Наименование лекции')
    video = models.FileField(verbose_name='Видео', blank=True)  # Файл видео, upload_to
    description = models.TextField(verbose_name='Описание')     # Описание, max_length
    date_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата создания')            # Дата создания
    date_publication = models.DateTimeField(verbose_name='Дата публикации',     # Дата публикации, Реализовать логику заполнения
                                            blank=True)
    status = models.BooleanField(verbose_name='Публикация')     # Статус, публикуется или нет, пока непонятно кто этим статусом управляет
    author = models.ForeignKey(get_user_model(),                     # ID_ Пользователь
                               on_delete=models.DO_NOTHING,
                               verbose_name='Автор')
    chapter = models.ForeignKey('course.Chapter',               # ID_ Глава
                                on_delete=models.SET_NULL,
                                null=True, blank=True,
                                verbose_name='Глава')
    category = models.ForeignKey('course.Category',             # Категория
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name='Категория')
    overall_rating = models.DecimalField(max_digits=5,          # Рейтинг, У нас рейтинг складывается из оценок.
                                         decimal_places=2,
                                         verbose_name='Рейтинг', default=0)

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'

    def __str__(self):
        return f'{self.name} ({self.author})'


# Модель Отзывы уроков\
class Comment(models.Model):
    text = models.TextField(max_length=2000,                # Текст
                            verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True,          # Дата
                                verbose_name='Дата')
    user = models.ForeignKey(get_user_model(),                   # ID_ пользователя
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    lesson = models.ForeignKey('lesson.Lesson',             # ID_ Урока
                               on_delete=models.CASCADE,
                               verbose_name='Лекция')
    answer = models.ForeignKey('lesson.Comment',            # ID_ Отзыва2
                               on_delete=models.CASCADE,
                               null=True, blank=True,
                               verbose_name='Ответ на отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"{self.lesson} {self.date} {self.user}"
