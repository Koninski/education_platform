# Generated by Django 3.2 on 2023-11-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_alter_lesson_overall_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='overall_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Рейтинг'),
        ),
    ]