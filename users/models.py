from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True,        # Поле под вопросом
                                    max_length=20,
                                    verbose_name='Номер тел.',
                                    blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото',      # upload_to
                              blank=True, null=True)
    subs = models.ManyToManyField('users.User',          # Подписки
                                  verbose_name='Подписки',
                                  blank=True)
    likes = models.ManyToManyField('lessons.Lesson',             # Лайки урокам
                                   related_name='liked_lessons',
                                   verbose_name='Лайки',
                                   blank=True)
    favorites = models.ManyToManyField('lessons.Lesson',         # Избраное уроки
                                       related_name='favorite_lessons',
                                       verbose_name='Избранное',
                                       blank=True)


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.pk} {self.last_name} {self.first_name}'


class History(models.Model):
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата')
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    lesson = models.ForeignKey('lessons.Lesson',
                               on_delete=models.CASCADE,
                               verbose_name='Урок')

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История просмотров'

    def __str__(self):
        return f'{self.date} ({self.user}) ({self.lesson})'
