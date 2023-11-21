from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(verbose_name='Slug')                        # Вспомогательное поле для индексации

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание')
    overall_rating = models.DecimalField(max_digits=5,
                                         decimal_places=2, default=0,
                                         verbose_name='Рейтинг',
                                         blank=True, null=True)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.DO_NOTHING,
                               verbose_name='Автор')
    category = models.ForeignKey('courses.Category',
                                 on_delete=models.DO_NOTHING,
                                 verbose_name='Категория')
    price = models.DecimalField(max_digits=5,
                                decimal_places=2,
                                verbose_name='Цена', default=0,
                                blank=True, null=True)

    def __str__(self):
        return f'{self.pk} {self.name} ({self.author})'

    def get_absolute_url(self):
        return reverse('course_display', kwargs={'course_id': self.pk})

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Chapter(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название главы')
    description = models.TextField(verbose_name='Описание')                 # max_length
    order = models.PositiveSmallIntegerField(verbose_name='Порядковый номер главы')
    course = models.ForeignKey('courses.Course',
                               on_delete=models.DO_NOTHING,
                               verbose_name='Курс')

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return f'{self.pk} {self.name} ({self.course})'


#  Модель Отзывы на курс (Review)
# *****************           !!!!!!   ВНИМАНИЕ    !!!!!!       **********************
# Общий вопрос по отзывам, как ограничить количество оценок на урок, курс для одного пользователя
class Review(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             verbose_name='Имя пользователя')
    course = models.ForeignKey('courses.Course',
                               on_delete=models.CASCADE,
                               verbose_name='Курс')
    text = models.TextField(max_length=2000, null=True, blank=True,
                            verbose_name='Текст отзыва')
    value = models.PositiveSmallIntegerField(verbose_name='Оценка')
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата отзыва')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['date']

    def __str__(self):
        return f'{self.course} {self.date} ({self.user})'
