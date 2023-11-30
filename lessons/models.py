from django.db import models
from django.contrib.auth import get_user_model


class Lesson(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название урока')
    video = models.FileField(verbose_name='Видео', null=True, blank=True)  # upload_to
    description = models.TextField(max_length=2000,
                                   verbose_name='Описание')
    date_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата создания')
    date_publication = models.DateTimeField(verbose_name='Дата публикации',  # Реализовать логику заполнения
                                            null=True, blank=True)
    status = models.BooleanField(
        verbose_name='Публикация',
        default=False)  # Статус, публикуется или нет, пока непонятно кто этим статусом управляет
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.DO_NOTHING,
                               verbose_name='Автор')
    chapter = models.ForeignKey('courses.Chapter',
                                on_delete=models.SET_NULL,
                                null=True, blank=True,
                                verbose_name='Глава')
    category = models.ForeignKey('courses.Category',
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name='Категория')
    likes_amount = models.DecimalField(max_digits=5,
                                       decimal_places=2,
                                       verbose_name='Количество лайков', default=0)

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'

    def __str__(self):
        return f'{self.name} ({self.author})'


class Comment(models.Model):
    text = models.TextField(max_length=2000,
                            verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата публикации')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    lesson = models.ForeignKey('lessons.Lesson',
                               on_delete=models.CASCADE,
                               verbose_name='Урок')
    answer = models.ForeignKey('lessons.Comment',
                               on_delete=models.CASCADE,
                               null=True, blank=True,
                               verbose_name='Ответ на отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"{self.lesson} {self.date} {self.user}"
