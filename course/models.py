from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')   # Наименование главы
    slug = models.SlugField(verbose_name='Slug')                        # Вспомогательное поле для индексации

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Наименование курса')  # Название
    description = models.TextField(verbose_name='Описание')      # описани
    overall_rating = models.DecimalField(max_digits=5,          # Рейтинг
                                         decimal_places=2, default=0,
                                         verbose_name='Рейтинг')
    author = models.ForeignKey(get_user_model(),                     # ID_ Пользователь
                               on_delete=models.DO_NOTHING,
                               verbose_name='Автор')
    category = models.ForeignKey('course.Category',             # Категория,
                                 on_delete=models.DO_NOTHING,
                                 verbose_name='Категория')
    price = models.DecimalField(max_digits=5,                   # Цена
                                decimal_places=2,
                                verbose_name='Цена', default=0)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.pk} {self.name} ({self.author})'


class Chapter(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Наименование главы')              # Название
    description = models.TextField(verbose_name='Описание')                 # Описание, max_length
    order = models.PositiveSmallIntegerField(verbose_name='Номер главы')    # Номер главы
    course = models.ForeignKey('course.Course',                             # ID_ Курса
                               on_delete=models.DO_NOTHING,
                               verbose_name='Курс')

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return f'{self.pk} {self.name} ({self.course})'


#  Модель Отзывы на курс (Review)
# *****************           !!!!!!   ВНИМАНИЕ    !!!!!!       **********************
# Общий вопрос по отзывам, как ограничить количество оценок на урок, курс дляодного пользователя
class Review(models.Model):
    user = models.ForeignKey(get_user_model(),                       # ID_ пользователя
                             on_delete=models.CASCADE,
                             verbose_name='Имя пользователя')
    course = models.ForeignKey('course.Course',                 # ID_ Курса
                               on_delete=models.CASCADE,
                               verbose_name='Курс')
    text = models.TextField(max_length=2000, null=True, blank=True,
                            verbose_name='Текст отзыва')        # Текст, комментарий
    value = models.PositiveSmallIntegerField(verbose_name='Оценка')     # Оценка
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата отзыва')     # Дата отзыва

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['date']

    def __str__(self):
        return f'{self.course} {self.date} ({self.user})'
