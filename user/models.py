from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50,              # Название
                            verbose_name='Имя')
    surname = models.CharField(max_length=50,           # Фамилия
                               verbose_name='Фамилия')
    email = models.EmailField(unique=True,              # Почта
                              verbose_name='почта')
    phone_number = models.CharField(unique=True,        # Поле и длина под вопросом
                                    max_length=20,
                                    verbose_name='Номер тел.')
    photo = models.ImageField(verbose_name='Фото',      # Фото пользоваьтеля upload_to
                              blank=True, null=True)
    subs = models.ManyToManyField('user.User',          # Подписки
                                  verbose_name='Подписки',
                                  blank=True)
    likes = models.ManyToManyField('lesson.Lesson',             # Лайки урокам
                                   related_name='liked_lessons',
                                   verbose_name='Лайки',
                                   blank=True)
    favorites = models.ManyToManyField('lesson.Lesson',         # Избраное уроки
                                       related_name='favorite_lessons',
                                       verbose_name='Избранное',
                                       blank=True)
    username = models.SlugField(verbose_name='Имя пользователя')          # Уникальное имя пользователя

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.pk} {self.surname} {self.name}'


class History(models.Model):
    date = models.DateTimeField(auto_now_add=True,      # Дата
                                verbose_name='Дата')
    user = models.ForeignKey(User,                      # ID_ пользователя
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    lesson = models.ForeignKey('lesson.Lesson',         # ID_ Урока
                               on_delete=models.CASCADE,
                               verbose_name='Лекция')

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История просмотров'

    def __str__(self):
        return f'{self.date} ({self.user}) ({self.lesson})'
